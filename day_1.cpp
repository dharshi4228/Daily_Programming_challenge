
#include <iostream>
using namespace std;
void sort(int arr[], int s) {
 int l= 0, mid = 0, h = s - 1;
 
 while (mid <= h) {
 if (arr[mid] == 0) {
 
 swap(arr[l], arr[mid]);
 l++;
 mid++;
 } else if (arr[mid] == 1) {
 mid++;
 
 } else if (arr[mid] == 2) {
 swap(arr[mid], arr[h]);
 h--;
 }
 }
}

void toprint(int arr[], int s) {
    
    for (int i =0 ; i<s ;i++) {
        cout<<arr[i]<<" ";
 }
 cout << endl;
}

int main(){
 
 int arr[] = {0, 1, 2, 1, 0, 2, 1, 0};
 int n = sizeof(arr)/ sizeof(arr[0] );

 cout << "Input: ";
 toprint(arr, n);

 sort(arr, n);

 cout << "Output: ";
 toprint(arr, n);


}
	
		
