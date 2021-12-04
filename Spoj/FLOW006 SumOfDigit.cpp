





#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, n, sum_total;
	cin >> t;

	while(t--){
		sum_total = 0;
		cin >> n;

		while (n>0){
			sum_total +=  n % 10;
			n /= 10;
		}

		cout << sum_total << endl;

	}

}