#include "Stack.h"


int main(int argc, const char* argv[])
{
    Linklist stack;
    Init_Stack(&stack);
    Push_Stack(&stack, 1);
    Push_Stack(&stack, 2);
    Push_Stack(&stack, 3);
    Top_Stack(stack);
    Pop_Stack(&stack);
    Push_Stack(&stack, 1);
    Push_Stack(&stack, 2);
    Push_Stack(&stack, 3);
    // printf("main:%x\n", stack);
    // printf("main:%d\n", stack.data);
    // printf("main:%x\n", stack.next);
    Linknode p = stack.next;
    while(p != NULL)
    {
        printf("main-x:%d\n", p->data);
        p = p->next;
    }


    return 0;
}
