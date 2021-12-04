


#include <iostream>
using namespace std;

bool is_prime(int n){

    if ( (n == 0) || (n == 1) ){
        return false;
    }
    else if( n == 2 ) {
        return true;
    }
    else if(n % 2 == 0){
        return false;
    }

    for (int i = 3; i < n/2; i+=2){
        if (n%i == 0){
            return false;
            break;
        }
    }

    return true;
}

// nth prime number
int main(){
    int n, i;
    int prime_counter = 0;
    cin >> n;

    cout << n << " " << is_prime(n) << endl;

    for(int i=1; i > 0 ; ++i){
        
        if (is_prime(i)){
            prime_counter += 1;
            if (prime_counter == n){
                cout << i << endl;
                break;
            }
        }
    }
}
