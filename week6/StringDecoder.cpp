#include <iostream>
#include <string>
#include <stack>

using namespace std;
class StringDecoder{
	private:
		string data_;
public:
string HEX_VALID = "0123456789ABCDEF";
    StringDecoder() {
		}
~StringDecoder(){
}
    stack<int> myStack;
    friend istream& operator >> (istream& is, StringDecoder& sd);
    friend ostream& operator << (ostream& os, StringDecoder& sd);
    string print() {
        int start = 0;
        int end = 0;
        string repeated_str = "";
        string decoded = "";
        string encoded = this->data_;

        int len = encoded.length();
        for (int i = 0;i < len;i++) {
            if ((myStack.empty()) && (encoded[i + 1] != '{') && (encoded[i] != '{') && (encoded[i] != '}')) {
                //if there's nothing im myStack and the next character isn't a bracket and the current character isn't a bracket
                decoded += encoded[i];//decode it 
            }
            if (encoded[i] == '{') {//if the current chraacter is a bracket
                int num = HEX_VALID.find(encoded[i - 1]);//get how many times you want to repeat the string inside the bracket

                if (num == string::npos) {//but if the character in front is not a valid Hex number, error
                    decoded = "ERROR: Invalid input";
                    return decoded;
                }
                myStack.push(num);//else, put in the stack how much you want to repeat the string inside the bracket
                start = i + 1;//set the start indest to after the bracket
            }
            if (encoded[i] == '}' && !myStack.empty()) {//if the current character is a bracket, and the stack isn't empty
                if (encoded[i - 1] != '}') {//if the previous element isn't a closing bracket
                    end = i - 1;//set the character before the closing bracket to the end index
                    repeated_str = encoded.substr(start, end - start + 1);
                    while(!myStack.empty()) {
                        string temp = "";
                        for (int x = 0; x < myStack.top();x++) {//repeat num times
                            temp += repeated_str;
                        }
                        myStack.pop();
                        repeated_str = temp;
                    }
                    decoded += repeated_str;
                    repeated_str = "";
                }
            }
        }
        return decoded;
    }
};

istream& operator >> (istream& is, StringDecoder& sd) {
    is >> sd.data_;
    return is;
}
ostream& operator << (ostream& os, StringDecoder& sd) {
    os << sd.print();
    return os;
}
int main(){
	StringDecoder sd;
	
	// Note:
	// encoded input strings are read from an input file using operator>>
	// your class may store a decoded string in data_ to print it using operator<<
	while(cin >> sd){
		cout << sd << endl;
	}
	
	return 0;
}