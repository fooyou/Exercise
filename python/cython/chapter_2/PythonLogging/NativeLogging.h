/**
 * @File Name: NativeLogging.h NativeLogging.c
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-11-11 11:11:00
 * @Last Modified: 2017-11-11 12:11:08
 * @Description:
**/

#ifndef __NATIVELOGGING_H__
#define __NATIVELOGGING_H__

#define printflike __attribute__ ((format (printf, 3, 4)))

extern void printflike native_logging_info(const char*, unsigned, const char*, ...);
extern void printflike native_logging_debug(const char*, unsigned, const char*, ...);
extern void printflike native_logging_error(const char*, unsigned, const char*, ...);


#define info(...) native_logging_info(__FILE__, __LINE__, __VA_ARGS__)
#define error(...) native_logging_debug(__FILE__, __LINE__, __VA_ARGS__)
#define debug(...) native_logging_error(__FILE__, __LINE__, __VA_ARGS__)

extern void SetupNativeLogging(const char* logFileName);
extern void CloseNativeLogging();

#endif // __NATIVELOGGING_H__

