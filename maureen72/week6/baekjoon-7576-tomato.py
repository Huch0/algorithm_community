#include <bits/stdc++.h>
using namespace std;

int n, m;
int maps[1001][1001];
queue<pair<int, int>> q;


int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void bfs()
{
    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            //int nx = x + dx[i];
            //int ny = y + dy[i];

            if (x + dx[i] < 0 || x + dx[i] >= m || y + dy[i] < 0 || y + dy[i] >= n)
            {
                continue;
            }
            if (maps[x + dx[i]][y + dy[i]] == -1)
            {
                continue;
            }
            //
            if (maps[x + dx[i]][y + dy[i]] == 0)
            {
                maps[x + dx[i]][y + dy[i]] = maps[x][y] + 1;
                q.push({x + dx[i], y + dy[i]});
            }
        }
    }
}

int main()
{

    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &maps[i][j]);
            if (maps[i][j] == 1)
            {
                q.push({i, j});
            }
        }
    }

    int result = 0;
    bfs();

   for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            result = max(result, maps[i][j] - 1);
        }
    }

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (maps[i][j] == 0)
            {
                result = -1;
            }
        }
    }

    printf("%d\n", result);

    return 0;
}
