#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define SENTINEL_GUARD 1001
#define TWO_DEGREE_OUT(CONTAINER) for(auto i:CONTAINER){for(auto j:i)std::cout<<j<<" / ";std::cout<<endl;}cout<<endl

void inputClient(vector<vector<int>> &row, int k, int number){
    auto rowIt = find_if(row.begin(), row.end(), [number](vector<int> &column){return column.front() > number;});
    if( rowIt == row.begin() ) rowIt++;
    rowIt--;
    auto columnIt = find_if(rowIt->begin(), rowIt->end(), [number](int columnNumber){return columnNumber > number;});
    rowIt->insert(columnIt, number);
    if( rowIt->size() == k*2 ){
        vector<int> newColumn;
        newColumn.assign(rowIt->begin()+k, rowIt->end());
        rowIt->resize(k);
        row.insert(rowIt+1, newColumn);
    }
}

void outputClient(vector<vector<int>> &row, int number){
    auto rowIt = find_if(row.begin(), row.end(), [number](vector<int> &column){return column.front() > number;});
    if( rowIt == row.begin() ) return;
    rowIt--;
    auto columnIt = find_if(rowIt->begin(), rowIt->end(), [number](int columnNumber){return columnNumber == number;});
    if( columnIt == rowIt->end() ) return;
    rowIt->erase(columnIt);
    if( rowIt->size() == 0 ) row.erase(rowIt);
}

int main(){
    vector<vector<int>> row;
    int N; int k;
    cin >> N >> k;

    for( int i=0; i<N; i++){
        char sign; int number;
        cin >> sign >> number;
        switch( sign ){
            case '+':
                if( row.empty() ){
                    row.push_back(vector<int> ());
                    row.push_back(vector<int> ());
                    row[0].push_back(number);
                    row[1].push_back(SENTINEL_GUARD);
                }
                else inputClient(row, k, number);
                break;
            case '-':
                outputClient(row, number);
                break;
        }
        //TWO_DEGREE_OUT(row);
    }
    row.erase(row.end()-1);
    for( auto v : row ){
        cout << v.front() << endl;
    }

    return 0;
}