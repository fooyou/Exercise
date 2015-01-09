/* 
* @Author: joshua
* @Date:   2014-10-21 14:43:49
* @Last Modified by:   joshua
* @Last Modified time: 2014-10-23 11:08:42
*/

#include <stdio.h>
#include <libavcodec/avcodec.h>
#include <libavformat/avformat.h>
#include <libswresample/swresample.h>
#include <libavutil/opt.h>
#include <libavutil/channel_layout.h>
#include <libavutil/samplefmt.h>

/*************************************************************
*
*  符号函数，>= 0的返回1，否则返回-1
*  @param  short s       要处理的数
*  @return int   result  返回值
*  @access private
*
*************************************************************/
int sign(float s)
{
    if ( s >= 0 )
        return 1;
    else
        return -1;
}   


/*************************************************************
*
*  计算短时能量
*  @param  void *data  要处理的所有帧的数据
*  @param  int   size  要处理的帧的个数，即nb的采样频率
*  @return int   STE   短时能量STE
*  @access private
*
*************************************************************/
long STE(void* data, int size)
{
    int i = 0;
    long sum = 0;

    short *pData = (short*)data;
    for ( i = 0; i < size; i++ )
    {
        sum += pData[i] * pData[i];
    }

    return sum;
}

/*************************************************************
*
*  计算过零率
*  @param  void *data  要处理的所有帧的数据
*  @param  int   size  要处理的帧的个数，即nb的采样频率
*  @return int   Zn    过零率Zn
*  @access private
*
*************************************************************/
long ZN(void *data, int size)
{
    int i = 0;
    long sum = 0;

    short *pData = (short*)data;
    for ( i = 1; i < size; i++ )
    {
        sum += abs(sign(pData[i]) - sign(pData[i-1]));
    }

    return sum / 2;
}

/*************************************************************
*
*  计算音频帧的能零积
*  @return int     RESULT  成功与否的标识
*  @access private
*
*************************************************************/
int ProcessAudio(char* fileName)
{
    int              audioStreamIndex = -1;
    AVFormatContext *pFCtx = NULL;
    AVCodecContext  *audioCCtx = NULL;
    AVCodec         *audioCdc  = NULL;
    int i = 0;

    av_register_all();

    pFCtx = avformat_alloc_context();
    if(avformat_open_input(&pFCtx, fileName, NULL,NULL) != 0)
    {
        printf("Couldn't open file\n");
        return -1;
    }

    if(avformat_find_stream_info(pFCtx, NULL) < 0)
    {
        printf("Couldn't find stream information\n");
        return -1;
    }

    //找到音视频流
    //av_dump_format(pFCtx, 0, fileName, 0);
    int streamNum = pFCtx->nb_streams;
    for(i = 0; i < streamNum; i++)
    {
        if(pFCtx->streams[i]->codec->codec_type == AVMEDIA_TYPE_AUDIO && audioStreamIndex < 0)
        {
            audioStreamIndex = i;
            break;
        }
    }

    if(-1 == audioStreamIndex)
    {
        printf("Couldn't find the stream\n");
        return -1;
    }

    //得到音视频的解码结构
    audioCCtx = pFCtx->streams[audioStreamIndex]->codec;
    audioCdc = avcodec_find_decoder(audioCCtx->codec_id);

    if(!audioCdc)
    {
        printf("Unsupported codec!\n");
        return -1;
    }

    if(avcodec_open2(audioCCtx, audioCdc, NULL) < 0)
    {
        printf("Can not open decoders!\n");
        return -1;
    }

    //得到音视频帧的timebase
    double audio_timebase = av_q2d(pFCtx->streams[audioStreamIndex]->time_base);
    printf("audio timebase = %f\n", audio_timebase);

    AVPacket  packet;
    AVFrame  *audioFrame = av_frame_alloc();

    av_init_packet(&packet);

    while(av_read_frame(pFCtx, &packet) >= 0)
    {
        if(packet.stream_index == audioStreamIndex) //处理音频帧
        {
            AVPacket decodingPacket = packet;
            while(decodingPacket.size > 0)
            {
                int frameFinished = 0, result = 0;
                result = avcodec_decode_audio4(audioCCtx, audioFrame, &frameFinished, &packet);//解码
                if ( result < 0 )
                {
                    printf("bad audio frame\n");
                    return -1;
                }

                decodingPacket.size -= result;
                decodingPacket.data += result;
                
                int sample_num = audioFrame->nb_samples;
                if(sample_num > 0)
                {
                    // printf("audio frame nb_samples = %d\n", sample_num);
                    long ste = STE((short*)audioFrame->data[0], audioFrame->nb_samples);
                    long zn = ZN((short*)audioFrame->data[0], audioFrame->nb_samples);
                    long sz = ste * zn;//能零积
                    // printf("ste = %ld\n", ste);
                    // printf("zn = %ld\n", zn);
                    printf("sz = %ld\n", sz);
                    //TODO 此处使用sz即可。                    
                }
            }
        }

        av_free_packet(&packet);
    }

    av_free(audioFrame);
    avcodec_close(audioCCtx);
    avformat_close_input(&pFCtx);

    return 0;
}


int main() {
    ProcessAudio("1.wav");
    return 0;
}
