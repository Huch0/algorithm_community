// Add any additional header files freely
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

// Returns menu serving time of each menu
int getMenuTime(char menu){
	switch(menu){
		case 'A': return 1;
		case 'B': return 2;
		case 'C': return 3;
		case 'D': return 4;
		case 'E': return 5;
		case 'F': return 7;
		case 'G': return 10;
		case 'H': return 12;
		case 'I': return 14;
		case 'J': return 15;
	}
}

// Your program here
int main() {
		int n;
		cin >> n;

		priority_queue<pair<int, char>, vector<pair<int, char>>, greater<pair<int, char>>> pq; // Min-heap

		for (int i = 0; i < n; i++) {
				int time;
				char menu;
				cin >> time >> menu;
				pq.push({time, menu});
		}

		vector<int> tables;  //각 테이블에 대한 서빙 종료 시간을 저장

		while (!pq.empty()) {
				pair<int, char> reservation = pq.top(); //가장 일찍 예약된것
				pq.pop();

				int menuTime = getMenuTime(reservation.second);
				bool assigned = false;

				for (int i = 0; i < tables.size(); i++) {
						if (tables[i] <= reservation.first) {
								tables[i] = reservation.first + menuTime;
								assigned = true;
								break;
						}
				}

				if (!assigned) {
						tables.push_back(reservation.first + menuTime);
				}
		}

		cout << tables.size() << endl;

		return 0;
}