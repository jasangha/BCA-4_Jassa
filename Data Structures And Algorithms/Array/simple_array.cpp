#include <iostream>
int main(){
    int arr[5];

    for(int i=0;i<5;i++)/*writing an array*/{
        arr[i]=i;    
    }

    std::cout<<"Values in Array: ";

    for(int i=0;i<5;i++)/*reading an array*/{
        std::cout<<arr[i]<<" ";
    }
    std::cout<<"\n";
    return 0;
}