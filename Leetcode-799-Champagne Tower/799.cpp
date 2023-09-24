#include <algorithm>

class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        double v[101][101] = {};
        v[0][0] = poured;
        for (int i = 0; i < query_row; i++) {
            for (int j = 0; j <= query_glass; j++) {
                double tmp = (v[i][j]-1) / 2;
                if (tmp > 0) {
                    v[i+1][j] += tmp;
                    v[i+1][j+1] += tmp;
                }
            }
        }
        return std::min(1.0, v[query_row][query_glass]);
    }
};

// for문 돌릴 때 j는 j <= query_glass로 해야한다.
/**
 * 처음에 배열을 안쓰고 벡터를 딱 (query_row+1) * (query_glass+1) 크기로 만들었는데
 * 생각해보니 그렇게 하면 query_glass가 작을 때 오른쪽 컵들이 다 버려져서 안된다.
**/