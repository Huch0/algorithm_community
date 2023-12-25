#include <iostream>
#include <queue>
#include <set>
#include <queue>

using namespace std;

typedef vector<vector<char>> Grid;
typedef pair<int, int> Point;
typedef queue<Point> PairQueue;
typedef set<Point> Visited;

bool isTrapped(Grid &earth, int i, int j, size_t rows, size_t cols, Visited &v);

bool isAdjacentToWater(Grid &earth, int i, int j, size_t rows, size_t cols, Visited &v);

void meltGlacier(Grid &earth, size_t rows, size_t cols, PairQueue &q, Visited &v, int y, int x);

void exploreWater(Grid &earth, size_t rows, size_t cols, PairQueue &q, Visited &v, int y, int x);

int main() {
    size_t rows, cols;
    cin >> rows >> cols;

    Grid earth(rows, vector<char>(cols));
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cin >> earth[i][j];
        }
    }

    PairQueue q;
    Visited v;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            // Mark water cells as visited except for trapped ones.
            if (earth[i][j] == '0' && !isTrapped(earth, i, j, rows, cols, v))
                v.insert({i, j});

                // Push and Mark glacier cells adjacent to water cells.
            else if (isAdjacentToWater(earth, i, j, rows, cols, v)) {
                q.emplace(i, j);
                v.insert({i, j});
            }
        }
    }

    int years = 0;

    while (!q.empty()) {
        size_t size = q.size();

        // For each glacier cells in queue
        for (int i = 0; i < size; i++) {
            Point p = q.front();
            q.pop();

            int y = p.first;
            int x = p.second;

            meltGlacier(earth, rows, cols, q, v, y, x);
        }
        years++;
    }

    cout << years;

    return 0;
}

bool isTrapped(Grid &earth, int i, int j, size_t rows, size_t cols, Visited &v) {
    // Base case: If the current cell is outside the grid boundaries or is a glacier cell, return false
    if (i <= 1 || j <= 1 || i >= rows - 2 || j >= cols - 2 || earth[i][j] == '1') {
        return false;
    }

    queue<Point> q;
    set<Point> checked;
    q.emplace(i, j);
    checked.insert({i, j});

    while (!q.empty()) {
        Point current = q.front();
        q.pop();

        if (current.first <= 1 || current.second <= 1 || current.first >= rows - 2 || current.second >= cols - 2) {
            return false;
        }

        int dx[] = {-1, 1, 0, 0};
        int dy[] = {0, 0, -1, 1};

        for (int k = 0; k < 4; ++k) {
            int newY = current.first + dy[k];
            int newX = current.second + dx[k];

            // if a group of water cell adjacent to water cell (visited) it is not trapped.
            if (earth[newY][newX] == '0' && v.count({newY, newX})) {
                return false;
            }

            // If the cell is a water cell (not visited), and not checked
            // push it onto the q for further exploration.
            else if (earth[newY][newX] == '0' && !v.count({newY, newX})
                     && checked.find({newY, newX}) == checked.end()) {
                q.emplace(newY, newX);
                checked.insert({newY, newX});
            }
        }
    }

    return true;
}


bool isAdjacentToWater(Grid &earth, int i, int j, size_t rows, size_t cols, Visited &v) {
    if (earth[i][j] == '1') {
        // Check left
        if (j > 0 && earth[i][j - 1] == '0' && !isTrapped(earth, i, j - 1, rows, cols, v)) {
            return true;
        }
        // Check right
        if (j < cols - 1 && earth[i][j + 1] == '0' && !isTrapped(earth, i, j + 1, rows, cols, v)) {
            return true;
        }
        // Check up
        if (i > 0 && earth[i - 1][j] == '0' && !isTrapped(earth, i - 1, j, rows, cols, v)) {
            return true;
        }
        // Check down
        if (i < rows - 1 && earth[i + 1][j] == '0' && !isTrapped(earth, i + 1, j, rows, cols, v)) {
            return true;
        }
    }
    return false;
}

void meltGlacier(Grid &earth, size_t rows, size_t cols, PairQueue &q, Visited &v, int y, int x) {
    // Melt the glacier cell and Mark as visited
    earth[y][x] = '0';
    v.insert({y, x});

    exploreWater(earth, rows, cols, q, v, y, x);
}

void exploreWater(Grid &earth, size_t rows, size_t cols, PairQueue &q, Visited &v, int y, int x) {
    // Check if the current position is out of bounds
    if (y <= 0 || y >= rows - 1 || x <= 0 || x >= cols - 1) {
        return;
    }

    // Check left, right, up, down for adjacent glaciers and unvisited water cells
    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};

    for (int k = 0; k < 4; ++k) {
        int newY = y + dy[k];
        int newX = x + dx[k];

        // If the adjacent cell is a glacier and not visited, add it to the queue
        if (earth[newY][newX] == '1' && !v.count({newY, newX}) &&
            isAdjacentToWater(earth, newY, newX, rows, cols, v)) {
            q.emplace(newY, newX);
            v.insert({newY, newX});
        }

            // If the adjacent cell is water and not visited, explore it recursively
        else if (earth[newY][newX] == '0' && !v.count({newY, newX})) {
            v.insert({newY, newX});
            exploreWater(earth, rows, cols, q, v, newY, newX);
        }
    }
}



