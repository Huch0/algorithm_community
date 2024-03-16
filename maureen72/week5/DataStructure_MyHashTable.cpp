#include <bits/stdc++.h>
using namespace std;

class HashTable {
	private:
		size_t prime;
		size_t bucket_size;
		size_t num_entries;
		double min_load_factor;
		double max_load_factor;
		vector<vector<pair<string, int>>> bucket;

		void rehash(size_t new_size) {
				cout << "Rehashing: " << bucket_size << " -> " << new_size << '\n';
				vector<vector<pair<string, int>>> old_bucket_array = bucket;
				bucket_size = new_size;
				bucket.resize(bucket_size);
				num_entries = 0;

				for(const auto& old_bucket : old_bucket_array) {
						for(auto [k, v] : old_bucket) {
								insert(k, v);
						}
				}
		}

		size_t hashFunction(const string& k) const {
				size_t hash_value = 0;
				for(auto ch : k) {
						hash_value = (hash_value * prime + ch) % 2147483647;
				}
				return hash_value;
		}

	public:
		HashTable(int bucket_size, int prime, double min_load_factor, double max_load_factor) {
				this->prime = prime;
				this->bucket_size = bucket_size;
				bucket.resize(bucket_size);
				num_entries = 0;
				this->min_load_factor = min_load_factor;
				this->max_load_factor = max_load_factor;
		}

		void insert(const string& k, int v) {
				size_t hash_code = hashFunction(k);
				size_t index = hash_code % bucket_size;

				bucket[index].emplace_back(k, v);
				++num_entries;
		}

		void remove(const string& k) {
				size_t hash_code = hashFunction(k);
				size_t index = hash_code % bucket_size;

				for(auto it=bucket[index].begin() ; it!=bucket[index].end() ; it++) {
						if (it->first == k) {
								bucket[index].erase(it);
								--num_entries;
								break;
						}
				}
		}
		

		void printSummary() {
				size_t index = 0, cmp = 0;
				for(int i=0 ; i<bucket.size() ; i++) {
						if (bucket[i].size() >= cmp) {
								index = i;
								cmp = bucket[i].size();
						}
				}
				cout << "Number of entries: " << num_entries << '\n';
				cout << "Size of the bucket array: " << bucket_size << '\n';
				cout << count_if(bucket.begin(), bucket.end(), [](auto x) {
						if (x.size() >= 5) return true;
						return false;
				}) << " buckets contain more than 5 elements\n";
				cout << "The longest bucket: " << index << '\n';
				for(auto [k, v] : bucket[index]) {
						cout << "(" << k << "," << v << ")\n";
				}
		}

		void resize() {
				if (num_entries > max_load_factor * bucket_size) {
						rehash(bucket_size * 2);
				}
				if (num_entries < min_load_factor * bucket_size && bucket_size > 512) {
						rehash(bucket_size / 2);
				}
		}
};

int main() {
		ios_base::sync_with_stdio(false);
		cin.tie(nullptr);
		cout.tie(nullptr);

		int a, line_length;
		double MIN_LOAD_FACTOR, MAX_LOAD_FACTOR;
		cin >> a >> MIN_LOAD_FACTOR >> MAX_LOAD_FACTOR >> line_length;

		HashTable hashTable = HashTable(512, a, MIN_LOAD_FACTOR, MAX_LOAD_FACTOR);

		while(line_length--) {
				char command;
				string k;
				int v;
				cin >> command >> k >> v;

				if (command == 'i') {
						hashTable.insert(k, v);
				} else if (command == 'r') {
						hashTable.remove(k);
				}
				hashTable.resize();
		}
		hashTable.printSummary();
}