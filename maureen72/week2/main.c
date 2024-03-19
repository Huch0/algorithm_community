#include <stdio.h>
#define MAX_NODES 10
#define INF 100000000
#define TRUE 1
#define FALSE 0
typedef struct GraphType {
    int n;  // 네트워크에 존재하는 정점의 개수
    int cost[MAX_NODES][MAX_NODES]; // 두 이웃한 정점간 거리/비용
} GraphType;

int distance[MAX_NODES];  // 시작 정점으로부터 각 정점까지의 거리 비용
int found[MAX_NODES];  // 최소 거리 계산이 완료된 정점을 표시

void print_status (GraphType* g, int step) {
    printf("STEP %d\n", step);
    printf("\t\tdistance: ");
    for (int i = 0; i < g->n; i++) {
        if (distance[i] == INF) {
            printf("\t * ");
        }
        else {
            printf("\t%d ", distance[i]);
        }
    }
    printf("\n");

    printf("\t\tfound: \t");
    for (int i = 0; i < g->n; i++) {
        printf("\t%d ", found[i]);
    }
    printf("\n");
}

int choose(int dist[], int n, int f[]) {
    int minNum = INF;
    int result = -1;
    for (int i = 0; i < n; i++) {
        if (f[i] == FALSE && dist[i] < minNum) {
            minNum = dist[i];
            result = i;
        }
    }
    return result;
}

void shortest_path(GraphType* g, int start_node) {
    // Initialize found and distance arrays
    for (int i = 0; i < g->n; i++) {
        found[i] = FALSE;
        distance[i] = INF;
    }
    // Initialize the starting node
    found[start_node] = TRUE;
    for (int i = 0; i < g->n; i++) {
        distance[i] = g->cost[start_node][i];
    }
    int step = 0;
    // Loop until all nodes are in found[]
    while (step < g->n) {
        print_status(g, step);
        // Choose the node with the minimum distance
        int now = choose(distance, g->n, found);
        // Add now to found[]
        found[now] = TRUE;
        // Update distance for adjacent nodes not in found[]
        for (int z = 0; z < g->n; z++) {
            if (!found[z]) {
                if (distance[now] + g->cost[now][z] < distance[z]) {
                    distance[z] = distance[now] + g->cost[now][z];
                }
            }
        }
        step++;
    }
}




int main() {
    int start_node_index = 1;
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

    //shortest_path(&G1, start_node_index);
    shortest_path(&G2, start_node_index);
}