/* 
* @Author: Joshua
* @Date:   2014-10-24 14:52:59
* @Last Modified by:   joshua
* @Last Modified time: 2014-10-27 15:22:23
*/

#include <Python.h>
#include <libavcodec/avcodec.h>
#include <libavformat/avformat.h>
#include <libswresample/swresample.h>
#include <libavutil/opt.h>
#include <libavutil/channel_layout.h>
#include <libavutil/samplefmt.h>

static int sign(float s)
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
static long STE(void* data, int size)
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
static long ZN(void *data, int size)
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
static int ProcessAudio(const char* fileName, PyObject* pList)
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

    // 得到音视频的解码结构
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

    // //得到音视频帧的timebase
    // double audio_timebase = av_q2d(pFCtx->streams[audioStreamIndex]->time_base);
    // printf("audio timebase = %f\n", audio_timebase);

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
                    
                    // double pts = (audioFrame->pts/* - pFCtx->streams[audioStreamIndex]->start_time*/) / audioFrame->sample_rate;
                    double pkt_pts = (double)audioFrame->pkt_pts / (double)audioFrame->sample_rate;

                    printf("pts = %ld pkt_pts = %ld sample rate = %dHz\n", audioFrame->pts, audioFrame->pkt_pts, audioFrame->sample_rate);

                    PyObject* pDict = PyDict_New();
                    PyDict_SetItem(pDict, PyUnicode_FromString("time"), PyFloat_FromDouble(pkt_pts));
                    PyDict_SetItem(pDict, PyUnicode_FromString("energy"), PyLong_FromLong(sz));
                    PyList_Append(pList, pDict);
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

static PyObject* wave_analyze(PyObject* self, PyObject* args)
{
    const char* wavePath;

    if (!PyArg_ParseTuple(args, "s", &wavePath))
        return NULL;

    printf("construct dict object %s\n", wavePath);


    // Create list object.
    PyObject* pList = PyList_New(0);
    // PyObject* pDict = PyDict_New();

    // Add items.
    if (NULL != pList)
    {
        ProcessAudio(wavePath, pList);
        // PyDict_SetItem(pDict, PyLong_FromLong(1), PyLong_FromLong(1233435));
        // PyDict_SetItem(pDict, PyLong_FromLong(2), PyLong_FromLong(233435));
    }

    return pList;
}

static PyMethodDef wavepointMethods[] = 
{
    {"analyze", wave_analyze, METH_VARARGS, "Analyze wave points."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef wavepointmodule = {
    PyModuleDef_HEAD_INIT,
    "wavepoint",
    NULL,
    -1,
    wavepointMethods
};

PyMODINIT_FUNC PyInit_wavepoint(void)
{
    return PyModule_Create(&wavepointmodule);
}
