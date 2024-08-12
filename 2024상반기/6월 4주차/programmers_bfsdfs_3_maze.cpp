//https://school.programmers.co.kr/learn/courses/30/lessons/1844 게임 맵 최단거리 

//dfs코드 - 시간초과
#include <vector>
#include <iostream>
#include <cmath>
using namespace std;
int answer = 999999999;
void dfs(vector<vector<int>>& map, vector<vector<int>>& record, int row, int col, int count) {
    if (count >= answer + abs((int)(map.size()-1-row)) + abs(int(map[0].size()-1-col))) return;
    if (map.size()-1 == row && map[0].size()-1 == col) {
        answer = min(answer, count);
        return;
    }
    record[row][col] = count;

    map[row][col] = 0;
    if (map.size()-1 >= row+1 && map[row+1][col] == 1) dfs(map, record, row+1, col, count+1);
    if (map[0].size()-1 >= col+1 && map[row][col+1] == 1) dfs(map, record, row, col+1, count+1);
    if (row-1 >= 0 && map[row-1][col] == 1) dfs(map, record, row-1, col, count+1);
    if (col-1 >= 0 && map[row][col-1] == 1) dfs(map, record, row, col-1, count+1);
    map[row][col] = 1;
}

int solution(vector<vector<int>> maps)
{
    vector<vector<int>> record(maps);
    for (int i=0; i<record.size(); i++) {
        for (int j=0; j<record[0].size(); j++) {
            record[i][j] = 999999999;
        }
    }
    dfs(maps, record, 0, 0, 1);
    if (answer == 999999999) return -1;
    return answer;
}


//bfs코드 - 최단거리는 bfs가 더 좋다
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

int solution(vector<vector<int>> maps)
{
    int answer = 0;
    vector<vector<int>> visited(maps);
    for (int i=0; i<visited.size(); i++) 
        for (int j=0; j<visited[0].size(); j++)
            visited[i][j] = 0;

    queue<pair<int, int>> q;
    q.push({0,0});
    visited[0][0] = 1;
    while(!q.empty()) {
        answer++;
        int nodenum = q.size();
        for (int i=0; i<nodenum; i++) {
            auto [row, col] = q.front();
            if (row == maps.size()-1 && col == maps[0].size()-1) return answer;
            q.pop();
            
            if (row+1 <= maps.size()-1 && visited[row+1][col] == 0 && maps[row+1][col] == 1) {
                q.push({row+1, col});
                visited[row+1][col] = 1;
            }
            if (col+1 <= maps[0].size()-1 && visited[row][col+1] == 0 && maps[row][col+1] == 1) {
                q.push({row, col+1});
                visited[row][col+1] = 1;
            }
            if (row-1 >= 0 && visited[row-1][col] == 0 && maps[row-1][col] == 1) {
                q.push({row-1, col});
                visited[row-1][col] = 1;
            }
            if (col-1 >= 0 && visited[row][col-1] == 0 && maps[row][col-1] == 1) {
                q.push({row, col-1});
                visited[row][col-1] = 1;
            }
        }
    }
    
    return -1;
}