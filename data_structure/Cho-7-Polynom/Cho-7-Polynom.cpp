#include <iostream>
#include <array>
#include <algorithm>
using namespace std;
#define PRINT_MONOMIALS(COEFFICIENT,EXPONENT) cout<<COEFFICIENT<<" "<<EXPONENT<<endl
#define MAX 1001

void addPolynoms(array<int, MAX> &polynom, int N){
    int polynomSize, coefficent, exponent;
    for( int i=0; i<N; i++ ){
        cin >> polynomSize;
        for( int j=0; j<polynomSize; j++ ){
            cin >> coefficent >> exponent;
            polynom[exponent] += coefficent;
        }
    }
}

void printPolynom(array<int, MAX> &polynom, int counter){
    for( int i=MAX-1; i>=0; i-- ){
        if( polynom[i] != 0 ){
            PRINT_MONOMIALS(polynom[i], i);
            counter--;
            if( counter == 0 ) break;
        }
    }
}

int main(){
    array<int, MAX> polynom = {0};
    int N;
    cin >> N;

    addPolynoms(polynom, N);

    int counter = count_if(polynom.begin(), polynom.end(), [](int i){return i != 0;}); 
    if( counter == 0 ){
        PRINT_MONOMIALS(0, 0);
        return 0;
    }

    cout << counter << endl;
    printPolynom(polynom, counter);
}