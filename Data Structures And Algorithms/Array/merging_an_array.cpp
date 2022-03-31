#include<iostream>
#define n 5
int main(){
    
    int arr[n],arr2[n];
    for(int i=0;i<n;i++)/*writing 1st array*/{    arr[i]=i+1;    }
     
    for(int i=0;i<n;i++)/*writing 2nd array*/{    arr2[i]=(i+1)*2;    }

    std::cout<<"\n1st Array: ";
    for(int i=0;i<n;i++)/*reading 1st array*/{    std::cout<<arr[i];    }
    std::cout<<"\n";

    std::cout<<"2nd Array: ";
    for(int i=0;i<n;i++)/*reading 2nd array*/{    std::cout<<arr2[i];    }
    std::cout<<"\n";
    
    for(int i=0;i<n;i++)/*Merging Two Arrays*/{    arr[i]=arr[i]+arr2[i];    }
    
    std::cout<<"Merged Array: ";
    for(int i=0;i<n;i++)/*reading merged array*/{    std::cout<<arr[i];    }
    std::cout<<"\n\n";

}