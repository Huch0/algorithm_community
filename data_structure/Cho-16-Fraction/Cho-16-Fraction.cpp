#include <iostream>
#include <stack>
#include <algorithm>
using namespace std;

struct Fraction {
    int numerator;
    int denominator;
};

stack<char> brackets;

Fraction calcultate(Fraction a, Fraction b, Fraction c) {
    Fraction result;
    int numerator = a.numerator * b.denominator * c.numerator + a.denominator * b.numerator * c.denominator;
    int denominator = a.denominator * b.denominator * c.numerator;

    int gcd = __gcd(numerator, denominator);

    result.numerator = numerator / gcd;
    result.denominator = denominator / gcd;

    return result;
}

Fraction totalFraction() {
    char bracket = brackets.top();
    if( bracket == ')' ) {
        brackets.pop();
        stack<Fraction> numbers;
        for (int i=0; i<3; i++) {
            Fraction toPush = totalFraction();
            if( toPush.numerator == -1 ) {
                cout << -1 << endl;
                exit(0);
            }
            numbers.push(toPush);
        }
        if( totalFraction().numerator != -1 ) {
            cout << -1 << endl;
            exit(0);
        }
        Fraction a = numbers.top(); numbers.pop();
        Fraction b = numbers.top(); numbers.pop();
        Fraction c = numbers.top(); numbers.pop();
        return calcultate(a, b, c);
    }
    else if ( bracket == '(' ) {
        brackets.pop();
        return {-1, -1};
    }
    else {
        Fraction result;
        result.numerator = bracket - '0';
        result.denominator = 1;
        brackets.pop();
        return result;
    }
}
int main() {
    int n; cin >> n;
    stack<char> checker;
    for (int i=0; i<n; i++) {
        char element; cin >> element;
        brackets.push(element);
        if( element == '(' ) checker.push(element);
        else if ( element == ')' ) {
            if( checker.empty() ) {
                cout << -1 << endl;
                exit(0);
            }
            checker.pop();
        }
    }
    

    Fraction result = totalFraction();
    cout << result.numerator << ' ' << result.denominator << endl;

    return 0;
}