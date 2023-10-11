#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>
#include <cctype>
using namespace std;

void get_function_statements(vector<string> functions[], int numof_func) {
	for (int i=0; i<numof_func; i++) {
		string statement;
		while (statement.compare("$") != 0) {
			cin >> statement;
			functions[i].push_back(statement);
		}
	}
}
void call_function(vector<string> functions[], int numof_func, stack<string>& call_stack, char func_name, vector<char>& deadlock_check) {
	if (find(deadlock_check.begin(), deadlock_check.end(), func_name) != deadlock_check.end()) {
		cout << "DEADLOCK";
		exit(0);
	}
	deadlock_check.push_back(func_name);

	int findex;
	for (int i=0; i<numof_func; i++) {
		if (functions[i][0][0] == func_name) {
			findex = i;
			break;
		}
	}
	for (int i=1; i<functions[findex].size()-1; i++) {
		if (functions[findex][i].length() == 1 && (isalpha(int(functions[findex][i][0])) == 1)) {
			call_function(functions, numof_func, call_stack, functions[findex][i][0], deadlock_check);
			continue;
		}
		string strname = string(1, func_name);
		call_stack.push(strname + "-" + functions[findex][i]);
	}
	deadlock_check.pop_back();
}
void print_nth_statement(int n, stack<string> call_stack) {
	if (n < 0) n += call_stack.size() + 1;
	if (n < 0 || n > call_stack.size()) {
		cout << "NONE\n";
		return;
	}
	int pop_count = call_stack.size() - n;
	for (int i=0; i < pop_count; i++) call_stack.pop();
	cout << call_stack.top() << "\n";
}

int main() {
	int numof_func, k1, k2, numof_statement;
	cin >> numof_func >> k1 >> k2;
	vector<string> functions[numof_func];
	vector<char> deadlock_check;
	stack<string> call_stack;

	get_function_statements(functions, numof_func);
	call_function(functions, numof_func, call_stack, 'M', deadlock_check);
	print_nth_statement(k1, call_stack);
	print_nth_statement(k2, call_stack);
}
