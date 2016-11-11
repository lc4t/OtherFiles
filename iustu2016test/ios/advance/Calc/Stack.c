#include <stdio.h>
#include <malloc.h>

#ifndef STACK_H
#define STACK_H

#define bool int
#define true 1
#define false 0

typedef struct node
{
    int data;
    struct node* next;
}node, *Linknode, Linklist;

void Init_Stack(Linklist* linklist)
{
    linklist->next = NULL;
    linklist->data = 0;  // may be length, not use here
}

bool Empty_Stack(Linklist linklist)
{
    if (linklist.next == NULL)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool Push_Stack(Linklist* linklist, int x)
{
    Linknode pre = linklist;
    while (pre->next != NULL)   // search status
    {
        pre = pre->next;
    }
    Linknode p;         // push
    p = (node*)malloc(sizeof(node));
    p->data = x;
    p->next = NULL;
    pre->next = p;
    return true;
}

int Pop_Stack(Linklist* linklist)
{
    Linknode pre = linklist;
    Linknode last = NULL;   // save status
    while (pre->next != NULL)
    {
        last = pre;
        pre = pre->next;
    }
    int x = pre->data;  // save data && delete the pop one
    free(pre);
    last->next = NULL;
    return x;
}

int Top_Stack(Linklist linklist)
{
    if (Empty_Stack(linklist))
    {
        printf("null\n");
        return -1;
    }
    else
    {
        Linknode pre = linklist.next;
        while (pre->next != NULL)   // search status
        {
            pre = pre->next;
        }
        return pre->data;
    }
}

#endif
