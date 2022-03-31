#include<iostream>
int main(){
    int arr_row=3,arr_column=3,arr2_column=3;
    int arr[3][3], arr2[3][3], arr3[arr_row][arr2_column];
    // Rows of first matrix and Columns of second matrix must be same.
    for(int i=0;i<3;i++)/*writing 1st 2d array*/{ for(int j=0;j<3;j++){ arr[i][j]=i*j; }}    
   
    for(int i=0;i<3;i++)/*writing 2nd 2d array*/{ for(int j=0;j<3;j++){ arr2[i][j]=(i+1)*j; }}
    
    std::cout<<"\n1st Array:\n";
    for(int i=0;i<3;i++)/*reading 1st 2d array*/{ for(int j=0;j<3;j++){ std::cout<<arr[i][j]<<" ";  } std::cout<<"\n"; }
    
    std::cout<<"2nd Array:\n";
    for(int i=0;i<3;i++)/*reading 2nd 2d array*/{ for(int j=0;j<3;j++){ std::cout<<arr2[i][j]<<" "; } std::cout<<"\n"; }

    for(int i=0;i<arr_row;i++)/*Multiplying matrix*/{ 
        for(int j=0;j<arr2_column;j++){
            arr3[i][j]=0;
            for(int k=0;k<arr_column;k++){
                arr3[i][j]+=arr[i][k]*arr2[k][j]; 
                }}}
   
    std::cout<<"Matrix After Multiplication:\n";
    for(int i=0;i<3;i++)/*reading matrix after Multiplying*/{ for(int j=0;j<3;j++){ std::cout<<arr3[i][j]<<" ";  } std::cout<<"\n"; }
}