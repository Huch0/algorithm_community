#include <iostream>
#include <vector>
using namespace std;
enum SortType { INSERTION=1, SELECTION, HEAP, QUIK };

void insertion(int k) {
    int N; cin >> N;
    vector<int> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }

    int counter = 0;

    for (int j=1; j<k+1; j++) {
        int key = A[j];
        int i = j-1;
        while (i>=0 && A[i]>key) {
            A[i+1] = A[i];
            i--;
            counter++;
        }
        if( i >= 0 ) counter++;
        A[i+1] = key;
    }

    cout << counter << endl;
}

void selection(int k) {
    int N; cin >> N;
    vector<int> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }

    for (int j=0; j<k; j++) {
        int smallest = j;
        for (int i=j+1; i<N; i++) {
            if (A[i] < A[smallest]) {
                smallest = i;
            }
        }
        if( smallest != j ) swap(A[j], A[smallest]);
    }

    for (int i=0; i<N; i++) {
        cout << A[i] << endl;
    }
}
void updateHeap(vector<int>& A, int root, int N) {
    int e = A[root-1];
    int j;
    for (j=2*root; j<=N; j*=2) {
        if( j<N && A[j-1] > A[j] ) j++;
        if ( e <= A[j-1] ) break;
        A[j/2-1] = A[j-1];
    }
    A[j/2-1] = e;
}
void heap(int k) {
    int N; cin >> N;
    vector<int> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    for (int i=N/2; i>=1; i--) {
        updateHeap(A, i, N);
    }

    for (int i=N-1; i>=N-k; i--) {
        swap(A[0], A[i]);
        updateHeap(A, 1, i);
    }

    for (int i=0; i<N-k; i++) {
        cout << A[i] << endl;
    }
}

int partition(vector<int>& A, int low, int high, int& k) {
    k--;
    int left, right;
    int pivot_item = A[low];
    int pivot = low;
    left = low;
    right = high;
    while (left < right) {
        while (A[left] <= pivot_item) left++;
        while (A[right] > pivot_item) right--;
        if( left < right ) swap(A[left], A[right]);
    }
    A[low] = A[right];
    A[right] = pivot_item;

    if( k == 0 ) {
        for (int i=0; i<A.size(); i++) {
            cout << A[i] << endl;
        }
        exit(0);
    }
    return right;
}

void quikSort(vector<int>& A, int N, int low, int high, int& k) {
    if( low < high ) {
        int pivot = partition(A, low, high, k);
        quikSort(A, N, low, pivot-1, k);
        quikSort(A, N, pivot+1, high, k);
    }
}

void quik(int k) {
    int N; cin >> N;
    vector<int> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    quikSort(A, N, 0, N-1, k);

    for (int i=0; i<N; i++) {
        cout << A[i] << endl;
    }
}

int main() {
    int type; int k;
    cin >> type >> k;

    switch(type) {
        case INSERTION:
            insertion(k);
            break;
        case SELECTION:
            selection(k);
            break;
        case HEAP:
            heap(k);
            break;
        case QUIK:
            quik(k);
            break;
        default:
            cout << "INVALID" << endl;
            break;
    }

    return 0;
}