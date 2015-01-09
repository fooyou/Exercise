/* 
* @Author: joshua
* @Date:   2014-11-03 16:34:04
* @Last Modified by:   joshua
* @Last Modified time: 2014-11-04 18:08:26
*/

#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string>
#include <vector>
#include <string.h>

using namespace std;

list<string> split(const string& src, const string& delimiter) {
    list<string> result;

    size_t pos = 0;
    string token;
    string s = src;
    while ((pos = s.find(delimiter)) != string::npos) {
        token = s.substr(0, pos);
        result.push_back(token);
        s.erase(0, pos + delimiter.length());
    }
    return result;
}

int GetFileSize(char* host, const int port, char* file, string* error, int& headersize)
{
    int sock_id;
    struct hostent* ht;
    int size = -1;

    if ((ht = gethostbyname(host)) == NULL) {
        if (error)
            error.append("Error at gethostbyname(\"%s\"), error code = %d\n", host, h_errno);
        return size;
    }

    if ((sock_id = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
        if (error)
            error.append("Error at connect socket, error code = %d\n", h_errno);
        return size;
    }

    // 建立连接
    struct sockaddr_in servaddr;
    memset(&servaddr, 0, sizeof(servaddr));
    memcpy((char*)&servaddr.sin_addr.s_addr, (char*)ht->h_addr, ht->h_length);
    servaddr.sin_port = htons(port);
    servaddr.sin_family = AF_INET;
    if (connect(sock_id, (struct sockaddr*)&servaddr, sizeof(servaddr)) != 0) {
        printf("Couldn't connect!\n");
        return -3;
    }

    string request;
    request.append("HEAD ");
    request.append(file);
    request.append(" HTTP/1.1\n");
    request.append("Host:");
    request.append(host);
    request.append("\r\n\r\n");
    write(sock_id, request.c_str(), request.length());

    // 读取响应
    char message[1024 * 1024] = { 0 };
    int msglen = read(sock_id, message, 1024 * 1024);
    string info;
    info.append(message, 0, msglen);

    // 关闭socket
    close(sock_id);

    printf("%s\n", message);

    // vector<string> property
    // vector<string> properties;
    // properties = Split(info, "\r\n", true);
    // vector<string>::iterator it;
    // string PName, PValue;


    // for (it = properties.begin(); it < properties.end(); ++it) {
    //     property = Split(*it, ":", true);
    //     SplitProperty(property, &PName, &pValue);
    //     if (PName == "Content-Length") {
    //         size = atoi(pValue.c_str());
    //         break;
    //     }
    // }

    // if (size == -1) {
    //     error->append("Resource Not Found!");
    // }

    // printf("File length = %d\n", size);
}

void DownloadFile(char* host, int port, char* file, char* savefile, float size, int& progress, int hsize)
{

}

int main(){
    int port = 8082;
    const char* host = "localhost";
    const char* file = "1.wav";

    return 0;
}
