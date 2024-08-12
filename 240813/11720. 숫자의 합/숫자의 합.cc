#include <iostream>
using namespace std;

int main() {
   string str;
   int n;
   int sum = 0;

   cin >> n >> str;
   for(int i = 0; i < n; i++){
        sum += (int)str[i] - 48;
   }
   cout << sum;

    
}