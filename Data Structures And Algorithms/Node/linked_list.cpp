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
int main(){
    Node * head = NULL;
    Node * second = NULL;
    Node * third = NULL;

    head = new Node();
    second = new Node();
    third = new Node();

    head->info = 1;
    head->link = second;
    second->info = 2;
    second->link = third;
    third->info = 3;
    third->link = NULL;

    printList(head);
    cout<<"\n\n";
}