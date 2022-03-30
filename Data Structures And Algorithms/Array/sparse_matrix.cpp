#include<iostream>
int main(){
    int arr[5][5], arr2[5][5];

    std::cout<<"\nEnter the no. of rows and columns of 1st matrix: ";
    std::cin>>arr[0][0]>>arr[0][1];

    std::cout<<"Enter the no. of non zero items: ";
    std::cin>>arr[0][2];

    for(int i=1;i<=arr[0][2];i++){ 
        std::cout<<"Enter the "<<i<<" non zero value: ";
        std::cin>>arr[i][2];

        std::cout<<"Enter the row and column for "<<arr[i][2]<<": ";
        std::cin>>arr[i][0]>>arr[i][1];
    }
    std::cout<<"Sparsed Matrix:\n";
    for(int i=0;i<=arr[0][2];i++){ for(int j=0;j<3;j++){ std::cout<<arr[i][j]<<" "; } std::cout<<"\n"; }
    std::cout<<"\n\n";
}