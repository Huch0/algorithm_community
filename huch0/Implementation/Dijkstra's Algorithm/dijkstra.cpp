#include <iostream>
#include <vector>
#include <set>

#define INF 999

void dijkstra(int n, std::vector<std::vector<size_t>> &W, std::vector<std::pair<size_t, size_t>> &F)
{
    int i, v_nearest;
    std::pair<int, int> e;
    std::vector<size_t> touch(n + 1);
    std::vector<int> length(n + 1);

    // F = ∅
    F.clear();

    // Initialize
    for (i = 2; i <= n; i++)
    {
        touch[i] = 1;
        length[i] = W[1][i];
    }

    // Repeat n - 1 times
    for (int _ = 0; _ < n - 1; _++)
    {
        // Find the vertex v_nearest ∈ V - Y such that nearest to Y.
        int min = INF;
        for (i = 2; i <= n; i++)
        {
            if (0 <= length[i] && length[i] < min)
            {
                min = length[i];
                v_nearest = i;
            }
        }
        std::cout << "v_nearest = " << v_nearest << " min = " << min << std::endl;

        // Add the edge (touch[v_nearest], v_nearest) to F
        e.first = touch[v_nearest];
        e.second = v_nearest;
        F.push_back(e);

        // Update the length of the shortest path
        for (i = 2; i <= n; i++)
        {
            if (length[i] != -1 && length[v_nearest] + W[v_nearest][i] < length[i])
            {
                length[i] = length[v_nearest] + W[v_nearest][i];
                touch[i] = v_nearest;
            }
        }
        // Y = Y ∪ {v_nearest}
        length[v_nearest] = -1;
    }

    // Print
    std::cout << "F\t= ";
    for (auto e : F)
    {
        std::cout << e.first << "->" << e.second << ", ";
    }
    std::cout << std::endl;

    std::cout << "touch\t= ";
    for (auto t : touch)
    {
        std::cout << t << " ";
    }
    std::cout << std::endl;

    std::cout << "length\t= ";
    for (auto l : length)
    {
        std::cout << l << " ";
    }
    std::cout << std::endl;
}

int main()
{
    int n = 5;
    std::vector<std::vector<size_t>> W = {
        {0, 0, 0, 0, 0, 0},
        {0, 0, 7, 4, 6, 1},
        {0, 7, 0, 2, 3, INF},
        {0, 4, 2, 0, 5, INF},
        {0, 6, 3, 5, 0, 1},
        {0, 1, INF, INF, 1, 0}};
    std::vector<std::pair<size_t, size_t>> F;
    dijkstra(n, W, F);

    return 0;
}