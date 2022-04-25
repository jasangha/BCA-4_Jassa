// create a program that insert values into linked list

#include<iostream>
using namespace std;
struct Node
{
    int info;
    struct Node * link;
};
class node{
    public:
    int info;
    node * link;
};
void printList(Node * n){
    cout<<"\n";
    while(n != NULL)
    {
        cout<<n->info<<" ";
        n = n->link;
    }
}

