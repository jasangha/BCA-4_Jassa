#include<iostream>
int main(){
    int arr[3][3];
    for(int i=0;i<3;i++)/*writing 2d array*/{
        for(int j=0;j<3;j++){
            arr[i][j]=i*j;
        }
    }
    for(int i=0;i<3;i++)/*reading 2d array*/{
        for(int j=0;j<3;j++){
            std::cout<<arr[i][j]<<" ";
        }
        std::cout<<"\n";
    }
}
