#include <bits/stdc++.h>
using namespace std;

int main(){
    int tmp;
    stack<int> s;
    
    for(int i = 0; i < 3; i++){
        cin >> tmp;
        stack<int> tmp_stack;
        while(!s.empty() && s.top() < tmp){
            tmp_stack.push(s.top());
            s.pop();
        }
        s.push(tmp);
        while(!tmp_stack.empty()){
            s.push(tmp_stack.top());
            tmp_stack.pop();
        }
    }
    
    while(!s.empty()){
        cout << s.top() << " ";
        s.pop();
    }
    
    return 0;
}
