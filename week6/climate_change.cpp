#include <iostream>
#include <vector>
#include <queue>
#include <set>
using namespace std;

// Define directions (up, down, left, right)
const int dr[] = { -1, 1, 0, 0 };
const int dc[] = { 0, 0, -1, 1 };
vector<pair<int, int>> directions = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };

// Check if a cell is valid and not visited
bool isValid(int rows, int cols, int r, int c, const std::vector<std::vector<int>>& matrix, std::vector<std::vector<bool>>& visited) {
	return (r >= 0 && r < rows && c >= 0 && c < cols && matrix[r][c] == 0 && !visited[r][c]);
}

// Perform BFS on the matrix
set<pair<int, int>> bfs(int time, int rows, int cols, const std::vector<std::vector<int>>& matrix, std::vector<std::vector<bool>>& visited, int startRow, int startCol) {
	std::queue<std::pair<int, int>> q;
	set<pair<int, int>> nontrapped;
	// Enqueue the starting cell
	q.push({ startRow, startCol });
	visited[startRow][startCol] = true;

	while (!q.empty()) {
		// Dequeue a cell and process it
		int currentRow = q.front().first;
		int currentCol = q.front().second;
		q.pop();
		int rim;
		// Print coordinates of '0' cells
		if (matrix[currentRow][currentCol] == 0) {
			if (currentRow > 0+time && currentCol > 0 + time && currentRow < rows-1-time && currentCol < cols-1-time) {
				rim = 0;
				for (const auto& around : directions) {
					int x = currentRow+around.first;
					int y = currentCol+around.second;
					if (matrix[x][y] == 1) {
						rim = 1;
					}
				}
				if (rim) {
					std::cout << "(" << currentRow << ", " << currentCol << ")" << std::endl;
					nontrapped.insert({ currentRow,currentCol });
				}
				
			}
		}

		// Enqueue valid neighbors (only '0' cells)
		for (int i = 0; i < 4; ++i) {
			int newRow = currentRow + dr[i];
			int newCol = currentCol + dc[i];

			if (isValid(rows, cols, newRow, newCol, matrix, visited)) {
				q.push({ newRow, newCol });
				visited[newRow][newCol] = true;
			}
		}
	}
	cout << "visited: " << endl;
	for (int i = 0;i < rows;i++) {
		for (int j = 0; j < cols;j++) {
			cout << visited[i][j];
		}
		cout << endl;
	}
	cout << "----------------------------------" << endl;
	return nontrapped;
}

int glacier_melting_time(int rows, int cols, vector<vector<int>>& cur) {
	
	vector<std::vector<int>> nxt = cur;
	set<pair<int, int>> untrapped;
	int time = 0;
	cout << "Year: " << time << endl;
	for (int i = 0;i < rows;i++) {
		for (int j = 0; j < cols;j++) {
			cout << cur[i][j];
		}
		cout << endl;
	}
	cout << "----------------------------------" << endl;
	int finished = 0;
	while (1) {
		//changed = 0;
		/*
		for (int i = 2+time; i < rows - 2-time; i++) {
			for (int j = 2+time; j < cols - 2-time; j++) {
				if (cur[i][j] == 0) {
					if (cur[i][j - 1] == 1 && cur[i - 1][j] == 1 && cur[i][j + 1] == 1 && cur[i + 1][j] == 1) {
						trapped.insert({ i,j });
						cur[i][j] = 1;
						cout << "(" << i << "," << j << ")" << endl;
					}
					else {
						
					}
				}
			}
		}
		*/
		std::vector<std::vector<bool>> visited(rows, std::vector<bool>(cols, false));

		untrapped=bfs(time, rows, cols, cur, visited, time, time);
		finished = 1;
		for (int i = 0; i < rows; i++) {
			for (int j = 0;j < cols; j++) {
				if (cur[i][j] == 1) {
					finished = 0;
				}
			}
		}
		if (finished) {
			break;
		}
		int x;
		int y;
		/*
		for (int i = 1 + time; i < rows-1-time;i++) {
			for (int j = 1 + time; j < cols-1-time;j++) {
				nxt[i][j] = 1;
			}
		}
		*/
		for (int j=time+1;j < cols - 1 - time; j++) {
			nxt[time + 1][j] = 0;
		}
		for (int j=time+1;j < cols - 1 - time; j++) {
			nxt[rows-2-time][j] = 0;
		}
		for (int i=time+1;i < rows - 1 - time; i++) {
			nxt[i][time+1] = 0;
		}
		for (int i=time+1;i < rows - 1 - time; i++) {
			nxt[i][cols-2-time] = 0;
		}
		for (const auto& rim : untrapped) {
			x = rim.first;
			y = rim.second;
			//nxt[x][y] = 0;
			for (const auto& around : directions) {
				int temp_x = x+around.first;
				int temp_y = y+around.second;
				nxt[temp_x][temp_y] = 0;
			}
		}

		untrapped.clear();
		/*
		for (int i = 1 + time; i < rows - 1 - time; i++) {
			for (int j = 1 + time; j < cols - 1 - time; j++) {
				if (cur[i][j] == 1) {
					changed = 1;
					if (cur[i][j - 1] == 0 || cur[i - 1][j] == 0 || cur[i][j + 1] == 0 || cur[i + 1][j] == 0) {
						
						for (const auto& searchPair : directions) {
							found = 0;
							auto it = trapped.find({i+searchPair.first,j + searchPair.second});
							if (it != trapped.end()) {
								cout << "Pair is in the set." << endl;
								cout << "(" << i + searchPair.first << "," << j + searchPair.second << ")" << endl;
								found = 1;
							}
							else {
								//std::cout << "Pair is not in the set." << std::endl;
								
							}
							
						nxt[i][j] = 0;
						}
					
						if (found) {
							nxt[i][j] = 1;
						}
						else {
							nxt[i][j] = 0;
						}
						
					else {
						nxt[i][j] = 1;
						}
					}
					
				}
			}
		
		for (const auto& special : trapped){
			int i = special.first;
			int j = special.second;
			nxt[i][j] = 0;
		}
		*/
		
		cur.assign(nxt.begin(), nxt.end());
		time++;
		
		cout << "Year: " << time <<endl;
		for (int i = 0;i < rows;i++) {
			for (int j = 0; j < cols;j++) {
				cout << cur[i][j];
			}
			cout << endl;
		}
		cout << "----------------------------------" << endl;
		
	}//while


	return time;
}

int main() {
	// Read input
	int rows, cols;
	cin >> rows >> cols;
	char* buf = new char[cols];
	vector<vector<int>> grid(rows, vector<int>(cols, 0));
	//cout << "matrix made" << endl;
	for (int i = 0; i < rows; ++i) {
		cin >> buf;
		for (int j = 0; j < cols; ++j) {
			grid[i][j] = *(buf + j)-'0';
		}
		//cout << "row" << i << endl;
	}
	//cout << "matrix initialized" << endl;

	// Calculate and print the result
	int result = glacier_melting_time(rows, cols, grid);
	cout << result << endl;
	cin >> rows;

	return 0;
}
