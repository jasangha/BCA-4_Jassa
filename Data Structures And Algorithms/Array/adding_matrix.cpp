#include<iostream>
int main(){
    int arr[3][3], arr2[3][3];
    for(int i=0;i<3;i++)/*writing 1st 2d array*/{ for(int j=0;j<3;j++){ arr[i][j]=i*j; }}    
   
    for(int i=0;i<3;i++)/*writing 2nd 2d array*/{ for(int j=0;j<3;j++){ arr2[i][j]=(i+1)*j; }}
    std::cout<<"\n1st Array:\n";
    for(int i=0;i<3;i++)/*reading 1st 2d array*/{ for(int j=0;j<3;j++){ std::cout<<arr[i][j]<<" ";  } std::cout<<"\n"; }
    
    std::cout<<"2nd Array:\n";
    for(int i=0;i<3;i++)/*reading 2nd 2d array*/{ for(int j=0;j<3;j++){ std::cout<<arr2[i][j]<<" "; } std::cout<<"\n"; }

    for(int i=0;i<3;i++)/*adding matrix*/{ for(int j=0;j<3;j++){ arr[i][j]=arr[i][j]+arr2[i][j]; }}

    std::cout<<"Matrix After Addition:\n";
    for(int i=0;i<3;i++)/*reading matrix after addition*/{ for(int j=0;j<3;j++){ std::cout<<arr[i][j]<<" ";  } std::cout<<"\n"; }
   

}