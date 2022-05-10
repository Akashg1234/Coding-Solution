#include<stdio.h>
#include<iostream>

class Solution{
 public:
  int findPivotElement(int arr[], int low, int high){
    
    if (high==low){
      return low;
    }
    
    if (high < low){
      return -1;
    }
    
    int mid = (low+high)/2;
    
    if(mid < high && arr[mid]>arr[mid+1]){
      return mid;
    }
    
    if(mid > low && arr[mid] < arr[mid-1]){
      return mid-1;
    }
    
    if (arr[low] >= arr[mid]){
      return findPivotElement(arr,low,mid-1);
    }
    return findPivotElement(arr,mid+1,high);
  }
  
 int binarySearch(int arr,int low,int high, int val){
   
   int mid=(low+high)/2;
   
   if (arr[mid]==val)
     return mid;
   
   if ( val > arr[mid] ){
     return binarySearch(arr,mid+1,high,val);
   }
   else{
     return binarySearch(arr,low,mid-1,val);
   }
 }
  
 int rotatedBinarySearch(int arr[],int n,int val){
   
   int pivot = findPivotElement(arr,0,n);
   
   if (arr[pivot]==val)
     return pivot;
   if (arr[0]<=val){
     return binarySearch(arr,0,pivot-1,val);
   }
   return binarySearch(arr,pivot+1,n-1,val);
 }
  
}
