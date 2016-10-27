/**
 * @File Name: a.c
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2016-10-27 15:10:30
 * @Last Modified: 2016-10-27 16:10:15
 * @Description:
 */

#include <stdio.h>
#include <stdlib.h>

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode head;
    struct ListNode* lHead = &head;
    struct ListNode* lCursor = lHead;
    struct ListNode* lRest = NULL;
    int jump = 0;
    int tmp = 0;
    while (l1 && l2) {
        struct ListNode* pNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        tmp = l1->val + l2->val + jump;
        pNode->val = tmp % 10;
        pNode->next = NULL;
        jump = tmp / 10;
        lCursor->next = pNode;
        lCursor = lCursor->next;
        l1 = l1->next;
        l2 = l2->next;
    }
    lRest = (NULL == l1) ? l2 : l1;
    while (lRest) {
        struct ListNode* pNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        tmp = lRest->val + jump;
        pNode->val = tmp % 10;
        pNode->next = NULL;
        jump = tmp / 10;
        lCursor->next = pNode;
        lCursor = lCursor->next;
        lRest = lRest->next;
    }
    if (jump) {
        struct ListNode* pNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        pNode->val = jump;
        pNode->next = NULL;
        lCursor->next = pNode;
    }
    return lHead->next;
}

struct ListNode* buildNode(int* l, int size) {
    struct ListNode head;
    struct ListNode* lHead = &head;
    struct ListNode* lCursor = lHead;
    int i;
    for (i = 0; i < size; ++i) {
        struct ListNode* pNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        pNode->val = l[i];
        pNode->next = NULL;
        lCursor->next = pNode;
        lCursor = lCursor->next;
    }
    return lHead->next;
}

void printNodes(struct ListNode* l) {
    while (l) {
        printf("%d ", l->val);
        l = l->next;
    }
    printf("\n");
}

int main() {
    int a1[] = {2, 4, 3};
    int a2[] = {5, 6, 4};
    struct ListNode* l1 = buildNode(a1, sizeof(a1) / sizeof(a1[0]));
    printNodes(l1);
    struct ListNode* l2 = buildNode(a2, sizeof(a2) / sizeof(a2[0]));
    printNodes(l2);
    struct ListNode* la = addTwoNumbers(l1, l2);
    printNodes(la);
}
