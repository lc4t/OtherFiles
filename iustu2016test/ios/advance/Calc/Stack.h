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

void Init_Stack(Linklist* linklist);
bool Empty_Stack(Linklist linklist);
bool Push_Stack(Linklist* linklist, int x);
int Pop_Stack(Linklist* linklist);
int Top_Stack(Linklist linklist);


#endif
