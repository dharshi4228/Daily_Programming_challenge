#include<iostream>
using namespace std;
int main(){
	int arr[] = {0, 1, 2, 1, 0, 2, 1, 0};
	int s= size(arr);
	for (int i=0 ; i<s-1 ;i++){
		for (int j=0; j<s-i-1;j++){
			if (arr [j] >arr[j+1]){
				swap(arr[j],arr[j+1]);
	        }
	    }
	}
	
	for(int i =0; i<s;i++){
		cout<< arr[i];
		if (i!= s-1){
		    cout<<",";
		}
	}
	cout<<endl;
}
	
		