/**
 * @File Name: bubble.c
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-10-27 13:10:53
 * @Last Modified: 2017-10-27 17:10:40
 * @Description:
**/
#include <stdio.h>
#include <time.h>

void printList(int* list, int len) {
    int i;
    printf("[");
    for (i = 0; i < len; ++i) {
        printf("%2d ", list[i]);
    }
    printf("]\n");
    return;
}

/**
 * @Synopsis bubbleSort 
 *
 * @Param list
 * @Param len
 *
 * @Returns 
 */
void bubbleSort(int* list, int len) {
    int i;
    int j;
    for (i = 0; i < len; ++i) {
        for (j = 0; j < len - 1 - i; ++j) {
            if (list[j] > list[j + 1]) {
                int temp = list[j + 1];
                list[j + 1] = list[j];
                list[j] = temp;
            }
        }
    }
}

/**
 * @Synopsis improvedBubble 
 * 设置一标志变量 pos，用于记录每趟排序中最后一次交换的位置。由于 pos 位置之后的记录均已交换到位，故在进行下一轮排序时只要扫描到 pos 位置即可。
 *
 * @Param list
 * @Param len
 */
void improvedBubble(int* list, int len) {
    int pos;
    int i;
    int end = len - 1;
    while (end > 0) {
        pos = 0;
        for (i = 0; i < end; ++i) {
            if (list[i] > list[i + 1]) {
                pos = i;
                int temp = list[i + 1];
                list[i] = list[i + 1];
                list[i + 1] = temp;
            }
        }
        end = pos;
    }
}

/**
 * @Synopsis doubleBubble
 * 传统冒泡一趟只能找一个最大最小值，但其实可以每趟
 * 双向冒泡，一次得到最大和最小值，从而使排序循环减
 * 少近一半
 *
 * @Param list
 * @Param len
 */
void doubleBubble(int* list, int len) {
    int pos = 0;
    int neg = len - 1;
    int tmp;
    int i;
    while (pos < neg) {
        for (i = pos; i < neg; ++i) {
            if (list[i] > list[i + 1]) {
                tmp = list[i + 1];
                list[i + 1] = list[i];
                list[i] = tmp;
            }
        }
        --neg;
        for (i = neg; i > pos; --i) {
            if (list[i] < list[i - 1]) {
                tmp = list[i];
                list[i] = list[i - 1];
                list[i - 1] = tmp;
            }
        }
        ++pos;
    }
}

struct timespec diff(struct timespec start, struct timespec end)
{
    struct timespec temp;
    if ((end.tv_nsec-start.tv_nsec)<0) {
        temp.tv_sec = end.tv_sec-start.tv_sec-1;
        temp.tv_nsec = 1000000000+end.tv_nsec-start.tv_nsec;
    } else {
        temp.tv_sec = end.tv_sec-start.tv_sec;
        temp.tv_nsec = end.tv_nsec-start.tv_nsec;
    }
    return temp;
}

typedef void (*pFunc)(int*, int);
void process(int* list, int len, pFunc pf) {
    struct timespec begin, end;
    double duration;
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &begin);
    pf(list, len);
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &end);
    printf("执行时间：%fms\n", diff(begin, end).tv_nsec * 10e-6);
    printList(list, len);
}

int main() {
    int list[] = {3,44,38,5,47,15,36,26,27,2,46,4,19,50,48};
    int listi[] = {3,44,38,5,47,15,36,26,27,2,46,4,19,50,48};
    int listd[] = {3,44,38,5,47,15,36,26,27,2,46,4,19,50,48};
    int len;

    len = sizeof(list) / sizeof(list[0]);
    printList(list, len);

    printf("冒泡");
    process(list, len, &bubbleSort);

    printf("改进冒泡");
    process(list, len, &improvedBubble);

    printf("双冒泡");
    process(list, len, &doubleBubble);

    return 0;
}
