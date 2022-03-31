#include<iostream>
#define n 5
int main(){
    int arr[n],loc,item;

    for(int i=0;i<n;i++)/*writing an array*/{
        arr[i]=i;    
    }
    std::cout<<"\nValues In Array Before Inserting: ";
    for(int i=0;i<n;i++)/*reading an array*/{
        std::cout<<arr[i]<<" ";
    }

    std::cout<<"\nEnter the location to be Deleted: ";
    std::cin>>loc;

    if (loc>n){
        std::cout<<"Invalid location\n";
    }
    else{
        for(int i=loc;i<n;i++){
            arr[i]=arr[i+1];
        }
    }

    std::cout<<"\nValues In Array After Inserting: ";
    for(int i=0;i<n-1;i++)/*reading an array*/{
        std::cout<<arr[i]<<" ";
    }
    std::cout<<"\n";
}

