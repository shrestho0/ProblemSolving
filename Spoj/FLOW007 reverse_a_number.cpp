
#include <iostream>
using namespace std;

int main(int argc, char const *argv[]){

	int t, n;
	cin >> t;

	while(t--){
		int reversed_number = 0;
		cin >> n;
		while (n > 0){
			int last_digit = n % 10;

			reversed_number = reversed_number * 10 + last_digit;
			n /= 10;
		}
		cout << reversed_number <<  endl;
	}

}