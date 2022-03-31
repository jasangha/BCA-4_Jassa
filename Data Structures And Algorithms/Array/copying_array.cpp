#include<iostream>
#define n 5
int main(){
    int arr[n],arr2[n];
    for(int i=0;i<n;i++)/*writing an array*/{
        arr[i]=i;    
    }
    for(int i=0;i<n;i++)/*copying an array*/{
        arr2[i]=arr[i];
    }

    for(int i=0;i<n;i++)/*reading an array*/{
        std::cout<<arr2[i];
    }
    std::cout<<"\n";


}