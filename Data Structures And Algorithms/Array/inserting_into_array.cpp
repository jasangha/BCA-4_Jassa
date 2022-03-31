#include<iostream>
#define n 5
int main(){
    int arr[n],loc,item;

    for(int i=0;i<n;i++)/*writing an array*/{
        arr[i]=i;    
    }
    std::cout<<"Values In Array Before Inserting: ";
    for(int i=0;i<n;i++)/*reading an array*/{
        std::cout<<arr[i]<<" ";
    }

    std::cout<<"\nEnter the location: ";
    std::cin>>loc;
    std::cout<<"Enter the item: ";
    std::cin>>item;

    if (loc>n){
        std::cout<<"Invalid location\n";
    }
    else{
        for(int i=n-1;i>=loc;i--){
            arr[i+1]=arr[i];
        }i
        arr[loc]=item;
    }

    std::cout<<"Values In Array After Inserting: ";
    for(int i=0;i<n;i++)/*reading an array*/{
        std::cout<<arr[i]<<" ";
    }
    std::cout<<"\n";

}