// No skeleton code is provided
#include <iostream>
#include <string>
#include <list>
#include <vector>

class HashTable
{
private:
    typedef std::pair<std::string, std::string> Entry;
    typedef std::list<Entry> Bucket;
    typedef std::vector<Bucket> BucketArray;

    BucketArray bucketArray;

    // For Load Factor
    int bucketArraySize;
    int numEntry;
    double minLoadFactor;
    double maxLoadFactor;

    // For HashFunction
    int aValue;

public:
    HashTable(int initialSize, double minLF, double maxLF, int aVal) : bucketArraySize(initialSize), numEntry(),
                                                                       minLoadFactor(minLF),
                                                                       maxLoadFactor(maxLF), aValue(aVal)
    {
        bucketArray.resize(bucketArraySize);
    }

    int hashFunction(const std::string &key) const
    {
        int hashCode = 0;

        for (char c : key)
        {
            hashCode = hashCode * aValue + c;
        }

        return std::abs(hashCode);
    }

    void insert(const std::string &key, const std::string &value)
    {
        int hashCode = hashFunction(key);
        Entry newEntry = Entry(key, value);

        bucketArray[hashCode % bucketArraySize].push_back(newEntry);
        numEntry++;

        checkAndResize();
    }

    void remove(const std::string &key)
    {
        int hashCode = hashFunction(key);

        auto &bucket = bucketArray[hashCode % bucketArraySize];

        for (auto it = bucket.begin(); it != bucket.end(); ++it)
        {
            if (it->first == key)
            {
                bucket.erase(it);
                numEntry--;

                checkAndResize();
                break;
            }
        }
    }

    void printSummary() const
    {
        int numBucketContainsMoreThanFive = 0;
        int lastLongestBucketIndex = 0;
        int longestBucketSize = 0;

        for (int i = 0; i < bucketArraySize; ++i)
        {
            int bucketSize = bucketArray[i].size();

            if (bucketSize > 5)
            {
                numBucketContainsMoreThanFive++;
            }

            if (bucketSize >= longestBucketSize)
            {
                longestBucketSize = bucketSize;
                lastLongestBucketIndex = i;
            }
        }

        std::cout << "Number of entries: " << numEntry << std::endl;
        std::cout << "Size of the bucket array: " << bucketArraySize << std::endl;
        std::cout << numBucketContainsMoreThanFive << " buckets contain more than 5 elements" << std::endl;
        std::cout << "The longest bucket: " << lastLongestBucketIndex << std::endl;
    };

    void checkAndResize()
    {
        double loadFactor = static_cast<double>(numEntry) / bucketArraySize;

        if (loadFactor > maxLoadFactor)
        {
            std::cout << "Rehashing: " << bucketArraySize << " -> " << bucketArraySize * 2 << std::endl;
            resizeBucketArray(bucketArraySize * 2);
        }
        else if (bucketArraySize > 512 && loadFactor < minLoadFactor)
        {
            std::cout << "Rehashing: " << bucketArraySize << " -> " << bucketArraySize / 2 << std::endl;
            resizeBucketArray(bucketArraySize / 2);
        }
    }

    void resizeBucketArray(int newBucketArraySize)
    {
        BucketArray newBucketArray(newBucketArraySize);

        for (const auto &bucket : bucketArray)
        {
            for (const auto &entry : bucket)
            {
                int hashCode = hashFunction(entry.first);
                newBucketArray[hashCode % newBucketArraySize].push_back(entry);
            }
        }

        bucketArray = std::move(newBucketArray);
        bucketArraySize = newBucketArraySize;
    }
};

int main()
{
    int a;
    double MIN_LOAD_FACTOR, MAX_LOAD_FACTOR;
    int NUMBER_OF_THE_FOLLOWING_LINES;

    std::cin >> a >> MIN_LOAD_FACTOR >> MAX_LOAD_FACTOR >> NUMBER_OF_THE_FOLLOWING_LINES;

    HashTable myHashTable(512, MIN_LOAD_FACTOR, MAX_LOAD_FACTOR, a);

    for (int i = 0; i < NUMBER_OF_THE_FOLLOWING_LINES; i++)
    {
        char COMMAND_N;
        std::string KEY_N;
        std::string VALUE_N;

        std::cin >> COMMAND_N >> KEY_N >> VALUE_N;

        //        std::cout << i << " : 2" << std::endl;

        if (COMMAND_N == 'i')
        {
            myHashTable.insert(KEY_N, VALUE_N);
        }
        else
        {
            myHashTable.remove(KEY_N);
        }
    }

    myHashTable.printSummary();

    return 0;
}