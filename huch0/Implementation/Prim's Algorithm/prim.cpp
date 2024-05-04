#include <iostream>
#include <vector>
#include <unordered_set>
#include <climits> // Add missing header for INT_MAX

void prim(int n, std::vector<std::vector<int>> &W, std::vector<std::pair<int, int>> &F)
{
    std::vector<int> nearest(n + 1, 0);  // Nearest vertex of each vertex from Y [2..n]
    std::vector<int> distance(n + 1, 0); // Distance of each vertex from Y [2..n]
    std::unordered_set<int> Y;           // Set of vertices in the tree

    // Init
    // F = ∅ / Y = {1}
    F.clear();
    Y.insert(1);

    // Init
    // nearest[i] = 1
    // distance[i] = W[1][i] for all i ∈ V - Y
    for (int i = 2; i <= n; i++)
    {
        nearest[i] = 1;
        distance[i] = W[1][i];
    }

    // Repeat n - 1 times
    // Add all n - 1 vertices to Y
    for (int _ = 0; _ < n - 1; _++)
    {
        int min = INT_MAX;
        int vnear = 0; // vnear ∈ V - Y

        // Find the nearest vertex (vnear ∈ V - Y) to Y
        for (int i = 2; i <= n; i++)
        {
            if (0 <= distance[i] && distance[i] < min)
            {
                min = distance[i];
                vnear = i;
            }
        }

        // Add the edge (nearest[vnear], vnear) to F
        std::pair<int, int> e = std::make_pair(nearest[vnear], vnear);
        F.push_back(e);

        // Add vnear to Y
        Y.insert(vnear);
        distance[vnear] = -1;

        // For each vertex i ∈ V - Y,
        // Update its distance from Y
        for (int i = 2; i <= n; i++)
        {
            if (W[i][vnear] < distance[i])
            {
                distance[i] = W[i][vnear];
                nearest[i] = vnear;
            }
        }
    }
}

int main()
{
    int n = 5;
    std::vector<std::vector<int>> W = {
        {INT_MAX, INT_MAX, INT_MAX, INT_MAX, INT_MAX, INT_MAX}, // Dummy
        {INT_MAX, INT_MAX, 1, 3, INT_MAX, INT_MAX}, // W[1][2] = 1, W[1][3] = 3
        {INT_MAX, 1, INT_MAX, 3, 6, INT_MAX}, // W[2][1] = 1, W[2][3] = 3, W[2][4] = 6
        {INT_MAX, 3, 3, INT_MAX, 4, 2}, // W[3][1] = 3, W[3][2] = 3, W[3][4] = 4, W[3][5] = 2
        {INT_MAX, INT_MAX, 6, 4, INT_MAX, 5}, // W[4][2] = 6, W[4][3] = 4, W[4][5] = 5
        {INT_MAX, INT_MAX, INT_MAX, 2, 5, INT_MAX}  // W[5][3] = 2, W[5][4] = 5
    };
    std::vector<std::pair<int, int>> F;

    prim(n, W, F);

    for (auto &e : F)
    {
        std::cout << e.first << " -> " << e.second << std::endl;
    }

    return 0;
}