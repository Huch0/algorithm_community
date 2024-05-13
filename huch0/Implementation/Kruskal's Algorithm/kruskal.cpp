#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

void kruskal(int n, std::vector<std::pair<std::pair<int, int>, int>> &E, std::vector<std::pair<std::pair<int, int>, int>> &F)
{
    // F = ∅
    F.clear();
    // Create n disjoint subsets of V
    std::vector<std::vector<int>> disjoint_sets = std::vector<std::vector<int>>(n + 1);

    // Sort the edges in non-decreasing order of their weights
    std::sort(E.begin(), E.end(), [](const std::pair<std::pair<int, int>, int> &a, const std::pair<std::pair<int, int>, int> &b)
              { return a.second < b.second; });

    for (int _ = 0; _ < n - 1; _++)
    {
        // Select the edge with the smallest weight
        // If the edge connects two different subsets, add it to F
        while (true)
        {
            auto e = E.front();
            E.erase(E.begin());
            // check if the edge connects two different subsets
            if (std::find(disjoint_sets[e.first.first].begin(), disjoint_sets[e.first.first].end(), e.first.second) == disjoint_sets[e.first.first].end() && std::find(disjoint_sets[e.first.second].begin(), disjoint_sets[e.first.second].end(), e.first.first) == disjoint_sets[e.first.second].end())
            {
                // Merge the two subsets
                for (auto v : disjoint_sets[e.first.second])
                {
                    disjoint_sets[e.first.first].push_back(v);
                }

                for (auto v : disjoint_sets[e.first.first])
                {
                    disjoint_sets[e.first.second].push_back(v);
                }

                // Add the edge to F
                F.push_back(e);
                disjoint_sets[e.first.first].push_back(e.first.second);
                disjoint_sets[e.first.second].push_back(e.first.first);
                break;
            }
        }
    }
}
int main()
{
    int n = 5;
    std::vector<std::pair<std::pair<int, int>, int>> E = {
        {{1, 2}, 1},
        {{1, 3}, 3},
        {{2, 3}, 3},
        {{2, 4}, 6},
        {{3, 4}, 4},
        {{3, 5}, 2},
        {{4, 5}, 5}};

    std::vector<std::pair<std::pair<int, int>, int>> F;
    kruskal(n, E, F);

    for (auto e : F)
    {
        std::cout << e.first.first << " " << e.first.second << " " << e.second << std::endl;
    }

    return 0;
}