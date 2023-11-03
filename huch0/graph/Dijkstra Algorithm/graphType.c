
#include <stdio.h>

#define INF __INT_MAX__

#define MAX_NODES 10
typedef struct GraphType {
    int n; // 네트워크에 존재하는 정점의 개수
    int cost[MAX_NODES][MAX_NODES]; // 두 이웃한 정점간 거리/비용
} GraphType;

int distance[MAX_NODES]; // 시작 정정으로 부터 각 정점까지의 거리 비용
int found[MAX_NODES]; // 최소 거리 계산이 완료된 정점을 표시

#define TRUE 1
#define FALSE 0

void print_status (GraphType* g, int step) {
    printf("STEP %d\n", step);

    // ex) distance: 1  0  10   *
    printf("\t\tdistance: ");
    for (int i = 0; i < g->n; i++) {
        if (distance[i] == INF) {
            printf("\t * ");
        } else {
            printf("\t%2d ", distance[i]);
        }
    }
    printf("\n");

    // ex) found: 0 1 0 0
    printf("\t\tfound: \t");
    for (int i = 0; i < g->n; i++) {
        printf("\t%2d ", found[i]);
    }
    printf("\n");
}

int choose (int distance[], int n, int found[]) {
    int minDistance = INF;
    int minNode = -1;

    for (int i = 0; i < n; i++) {
        if (!found[i] && distance[i] < minDistance) {
            minDistance = distance[i];
            minNode = i;
        }
    }

    return minNode;
}

void shortest_path(GraphType* g, int start_node) {
    found[start_node] = TRUE;

    // Initiate distance
    for (int i = 0; i < g->n; i++) {
        distance[i] = g->cost[start_node][i];
    }

    int step = 0;
    // Loop until all nodes are in found[]
    while (step < g->n - 1) {
        print_status(g, step);

        // Choose the node has minimum distance
        int u = choose(distance, g->n, found);

        // Add u to found[]
        found[u] = TRUE;

        // for each z adjacent to u and not in found[]
        for (int z = 0; z < g->n; z++) {
            if (g->cost[u][z] != INF && !found[z]) {
                if (distance[u] + g->cost[u][z] < distance[z]) {
                    distance[z] = distance[u] + g->cost[u][z];
                }
            }
        }
        step++;
    }
}

int main () {
    int start_node_index = 1;

    GraphType g = { 4,
        {{0, 1, 20, 23},
        {1, 0, 10, INF},
        {20, 10, 0, 18},
        {23, INF, 18, 0}}
    };

    GraphType G1 = { 6,
        {{0, 5, 3, 7, INF, INF},
        {5, 0, 4, INF, 7, 9},
        {3, 4, 0, 3, 8, INF},
        {7, INF, 3, 0, 4, INF},
        {INF, 7, 8, 4, 0, 2},
        {INF, 9, INF, INF, 2, 0}}
    };

    GraphType G2 = { 7,
        {{0, 7, INF, INF, 3, 10, INF},
        {7, 0, 4, 10, 2, 6, INF},
        {INF, 4, 0, 2, INF, INF, INF},
        {INF, 10, 2, 0, 11, 9, 4},
        {3, 2, INF, 11, 0, INF, 5},
        {10, 6, INF, 9, INF, 0, INF},
        {INF, INF, INF, 4, 5, INF, 0}}
    };


    //shortest_path(&g, start_node_index);
    // shortest_path(&G1, start_node_index);
    shortest_path(&G2, start_node_index);
}