#include <iostream>
#include <vector>
#include <list>
#include <cmath>

using namespace std;

struct HashNode {
    string key;
    int value;
    HashNode* next;

    HashNode(const string& k, int v) : key(k), value(v), next(nullptr) {}
};

class HashTable {
private:
    int size;
    int hash_a;
    double min_load_factor;
    double max_load_factor;
    int num_entries;
    vector<list<HashNode*>> bucket_array;
    int longest_bucket_index;


public:
    HashTable(int a, int numCommands, double min_load, double max_load)
        : size(512), hash_a(a), min_load_factor(min_load), max_load_factor(max_load),
        num_entries(0), bucket_array(size), longest_bucket_index(0) {}

    size_t polynomialHashCode(size_t x) {
        const size_t modulo = 2147483647;
        x = x % modulo;
        return x;
    }

    size_t hashFunction(const string& key) {
        const size_t modulo = 2147483647;
        size_t code = 0;

        for (char ch : key) {
            // Update the hash code using the polynomial expression
            code = (hash_a * polynomialHashCode(code + ch));
        }

        return code/hash_a;
    }


    size_t compressHash(size_t hashCode) {
        // Division method
        return hashCode % size;
    }

    void rehash(int newSize) {
        cout << "Rehashing: " << size << " -> " << newSize << endl;
        vector<list<HashNode*>> oldArray = bucket_array;
        size = newSize;
        bucket_array = vector<list<HashNode*>>(newSize);
        num_entries = 0;
        longest_bucket_index = 0;

        for (auto& oldBucket : oldArray) {
            for (auto& node : oldBucket) {
                insert(node->key, node->value);
            }
            oldBucket.clear();
        }
        vector<list<HashNode*>>().swap(oldArray);
    }

    void insert(const string& key, int value) {
        int hashCode = hashFunction(key);
        int index = compressHash(hashCode);
        //cout << "insert at " << index << " bucket" << endl;
        HashNode* newNode = new HashNode(key, value);
        auto& bucket = bucket_array[index];

        for (auto& node : bucket) {
            if (node->key == key) {
                // Key already exists, update the value and return
                node->value = value;
                delete newNode; // Delete the unused node
                return;
            }
        }

        if (bucket_array[index].empty()) {
            bucket_array[index].push_back(newNode);
        }
        else {
            bucket_array[index].back()->next = newNode;
            bucket_array[index].push_back(newNode);
        }

        num_entries++;

        if (num_entries > size * max_load_factor) {
            rehash(size * 2);
        }
    }

    void remove(const string& key) {
        int hashCode = hashFunction(key);
        int index = compressHash(hashCode);
       // cout << "remove from  " << index << " bucket" << endl;
        auto& bucket = bucket_array[index];
        auto it = bucket.begin();
        HashNode* prev = nullptr;

        while (it != bucket.end() && (*it)->key != key) {
            prev = *it;
            ++it;  // Update iterator
        }

        if (it != bucket.end()) {
            if (prev) {
                prev->next = (*it)->next;
                it = bucket.erase(it);
            }
            else {
                bucket.pop_front();
            }

            num_entries--;

            if (num_entries < size * min_load_factor && size > 512) {
                rehash(size / 2);
            }
        }
    }


    void printSummary() {
        cout << "Number of entries: " << num_entries << endl;
        cout << "Size of the bucket array: " << size << endl;

        int longBuckets = 0;
        int maxBuckets = 0;
        int longestBucket = 0;
        for (int i = 0; i < size; i++) {
            int bucketLength = 0;
            for (auto node : bucket_array[i]) {
                bucketLength++;
            }

            if (bucketLength > 5) {
                longBuckets++;
            }

            if (bucketLength >= maxBuckets) {
                maxBuckets = bucketLength;
                longest_bucket_index = i;
            }
        }

        cout << longBuckets << " buckets contain more than 5 elements" << endl;


        cout << "The longest bucket: " << longest_bucket_index << endl;

        
        for (auto node : bucket_array[longest_bucket_index]) {
            cout << "(" << node->key << "," << node->value << ")" << endl;
        }
        
    }
};

int main() {
    int a, numCommands;
    double minLoad, maxLoad;

    cin >> a >> minLoad >> maxLoad;
    cin >> numCommands;

    HashTable hashTable = HashTable(a, numCommands, minLoad, maxLoad);

    for (int i = 0; i < numCommands; i++) {
        char command;
        string key;
        int value;

        cin >> command >> key >> value;;

        if (command == 'i') {
            hashTable.insert(key, value);
        }
        else if (command == 'r') {
            hashTable.remove(key);
        }
    }

    hashTable.printSummary();
    return 0;
}
