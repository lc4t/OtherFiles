#include <iostream>
#include <string>

typedef int type;
typedef struct node
{
    type data;
    struct node* prev;
    struct node* next;
} Node, *Linknode, Linklist;

void PrintNode(Linknode node, std::string comment)
{
    std::cout << "------" << comment << std::endl;

    std::cout << node << std::endl;
    if (node != NULL)
    {
        std::cout << "data:" << node->data << std::endl;
        std::cout << "prev:" << node->prev << std::endl;
        std::cout << "next:" << node->next << std::endl;
    }
    std::cout << "------" << std::endl;

}

void PrintList(Linklist linklist)
{
    Linknode node = new Node;
    int i = 0;
    for (node = linklist.next; node != NULL; node = node->next, i ++)
    {
        std::cout << i << ":" << node->data << std::endl;
    }
}

void InitList(Linklist& linklist)
{
    linklist.data = 0;
    linklist.prev = NULL;
    linklist.next = NULL;
}

Linknode GetNodeByPos(Linklist& linklist, int pos)
{
    Linknode node = new Node;
    node = (Linknode)&linklist;

    for (int i = 0; i < pos && node != NULL; i++)
    {
        node = node->next;
    }
    return node;
}

Linknode GetNodeByValue(Linklist& linklist, type value)
{
    Linknode node = new Node;
    for (node = linklist.next; node != NULL; node = node->next)
    {
        if (node->data == value)
        {
            return node;
        }
    }
}

bool Insert(Linklist& linklist, int pos, type data)
{
    Linknode newNode = new Node;
    Linknode preNode = new Node;

    preNode = GetNodeByPos(linklist, pos - 1);

    newNode->data = data;
    newNode->prev = preNode;
    newNode->next = preNode->next;

    if (newNode -> next != NULL)
    {
        newNode->next->prev = newNode;
    }
    preNode->next = newNode;
    return true;
}

bool DeleteNodeByPos(Linklist& linklist, int pos)
{
    Linknode delNode = new Node;
    delNode = GetNodeByPos(linklist, pos);
    // PrintNode(delNode, "delete me");
    if (delNode != NULL)
    {
        if (delNode->next == NULL)
        {
            delNode->prev->next = NULL;
        }
        else
        {
            delNode->prev->next = delNode->next;
            delNode->next->prev = delNode->prev;
        }
        delete delNode;
    }
    // PrintNode(GetNodeByPos(linklist, pos - 1), "deletes prev");
    // PrintNode(GetNodeByPos(linklist, pos), "deletes next");

    return true;
}

int main(int argc, const char* argv[])
{
    // %X  0 1 2 3
    // pos L 1 2 3
    Linklist list;
    InitList(list);
    // test
    Insert(list, 1, 1);
    Insert(list, 2, 2);
    Insert(list, 3, 3);
    PrintList(list);

    PrintNode(GetNodeByValue(list, 2), "find 2 result");
    PrintNode(GetNodeByValue(list, 10), "find 10 result");
    PrintNode(GetNodeByPos(list, 100), "pos 100");
    DeleteNodeByPos(list, 2);
    PrintList(list);
    return 0;
}
