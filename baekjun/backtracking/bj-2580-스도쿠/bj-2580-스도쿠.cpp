#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> board(9, vector<int>(9));

void backtracking(int row, int column) {
    if( row == 9 ) {
        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) cout << board[i][j] << ' ';
            cout << '\n';
        }
        exit(0);
    }

    if( column == 9 ) backtracking(row+1, 0);
    else {
        if( board[row][column] == 0 ) {
            for (int i=1; i<=9; i++) {
                bool promising = true;
                for (int j=0; j<9; j++) {
                    if( board[row][j] == i || board[j][column] == i ) {
                        promising = false;
                        break;
                    }
                }
                if( promising ) {
                    int startRow = (row/3)*3;
                    int startColumn = (column/3)*3;
                    for (int j=startRow; j<startRow+3; j++) {
                        for (int k=startColumn; k<startColumn+3; k++) {
                            if( board[j][k] == i ) {
                                promising = false;
                                break;
                            }
                        }
                    }
                    if( promising ) {
                        board[row][column] = i;
                        backtracking(row, column+1);
                        board[row][column] = 0;
                    }
                }
            }
        } else backtracking(row, column+1);
    }   
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    for (int i=0; i<9; i++)
        for (int j=0; j<9; j++) cin >> board[i][j];

    
    backtracking(0, 0);
}