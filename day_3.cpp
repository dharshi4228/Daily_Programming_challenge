
#include<iostream>
#include<vector>
#include<unordered_map>
#include<sstream>
using namespace std;

int main(){
	unordered_map<int,int>freqMap;
	string input,temp;
	getline(cin,input);
	stringstream ss(input);
	vector<int> a;
	int count =1;
	
	while(getline(ss,temp,',')){
		a.push_back(stoi(temp));
		count++;
	}
	
	for(int num:a){
		freqMap[num]++;
	}
	for (const auto& pair:freqMap){
		if(pair.second >1){
			cout<< pair.first<<endl;
	}}
    
	 return 0;
}