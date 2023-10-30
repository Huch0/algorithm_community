#include <iostream>
#include <string>
#include <vector> //Vector in C++
using namespace std;

string WB[8] = {//It's easier to compare the boards with pre-made boards
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW"
};
string BW[8] = {
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB"
};
string board[50];

int WB_cnt(int x, int y) {
    int cnt = 0;
    for (int i = 0; i < 8; i++)
    {
        for (int j = 0; j < 8; j++) {
            if (board[x + i][y + j] != WB[i][j])
                cnt++;
        }
    }
    return cnt;
}

int BW_cnt(int x, int y)
{
    int cnt = 0;
    for (int i = 0; i < 8; i++)
    {
        for (int j = 0; j < 8; j++)
        {
            if (board[x + i][y + j] != BW[i][j])
                cnt++;
        }

    }
    return cnt;
}

int main() {
    int cnt;
    int min_val = 12345;
    pair<int, int> p1; // included in the vector header file
    cin >> p1.first >> p1.second;
    for (int i = 0; i < p1.first; i++)
        cin >> board[i];
    for (int i = 0; i + 8 <= p1.first; i++) {//access with .first .second for pairs
        for (int j = 0; j + 8 <= p1.second; j++) {
            int tmp;
            tmp = min(WB_cnt(i, j), BW_cnt(i, j));
            if (tmp < min_val) {
                min_val = tmp;
            }
        }
    }
    cout << min_val;
    return 0;
}