#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool compare(string &str1, string &str2){
   if(str1.length() != str2.length()){
      return str1.length() < str2.length();
   } else {
      return str1 < str2;
   }
}

int main() {
   int n;
   cin >> n;

   string arr[n];

   for(int i = 0; i < n; i++){
      cin >> arr[i];
   }

   sort(arr, arr + n, compare);

   for(int i = 0; i < n; i++){
      if(i > 0 && arr[i] == arr[i - 1]){ 
         continue;
      }

      cout << arr[i] << endl;
   }

   
}