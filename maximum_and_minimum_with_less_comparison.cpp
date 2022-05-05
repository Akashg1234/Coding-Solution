#include <stdio.h>

struct Pair{
	int min;
	int max;
}

struct Pair getMinMax(int arr[] , int low, int high){
	int mid;
	struct Pair MinMax , minmaxl, minmaxr;
	
	// if only one element is left
	
	if (high==low){
		MinMax.min = arr[low];
		MinMax.max = arr[low];
		return MinMax;
	}
	
// 	if two element are present
	if (low+1 == high){
		if(arr[low] > arr[high]){
			MinMax.min = arr[high];
			MinMax.max = arr[low];
		}
		else if(arr[low] < arr[high]){
			MinMax.max = arr[high];
			MinMax.min = arr[low];
		}
		return MinMax;
	}
	
// 	else recur left part and the right part
	mid = (low+high) / 2;
	minmaxl = getMinMax(arr , low , mid );
	minmaxr = getMinMax(arr , mid +1 , high );
	
	if (minmaxl.min < minmaxr.min ){
		MinMax.min  = minmaxl.min;
	}
	else{
		MinMax.min = minmaxr.min;
	}
	
	if (minmaxl.max < minmaxr.max ){
		MinMax.max  = minmaxl.max;
	}
	else{
		MinMax.max = minmaxr.max;
	}
	
	return MinMax;
}

int main()
{
	int arr[10];
	for(int i=0;i<10;i++)
		cin>>&arr[i];
	struct Pair p= getMinMax(arr,0,6);
	cout << p.min << p.max;
	return 0;
}
