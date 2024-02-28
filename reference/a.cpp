#include <iostream>
using namespace std;

int main() {
   int stop;
   int result;
   int a;
   int b;

   cin >> stop;
   result = 0;

   for (a = 1; a < 5; ++a) {
      cout << a << ": "; // a = 1
      
      for (b = 0; b < 4; ++b) {
         result += a; // result = 1 2 3 4
         
         if (result > stop) {
            cout << "_ ";
            continue;
         }
         
         cout << result << ","; // 1 2 3 4 
      }
      
      cout << endl;
   }

   return 0;
}