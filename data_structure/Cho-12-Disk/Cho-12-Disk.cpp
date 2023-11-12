#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

list<pair<string,int>> disk;

void writeFile() {
    string fileName; int size;
    cin >> fileName >> size;

    int nullSize = 0;
    auto nullIt = disk.begin();
    while (true) {
        nullIt = find_if(nullIt, disk.end(), [](pair<string,int> file) {return file.first == "";});
        if( nullIt == disk.end() ) break;
        nullSize += nullIt->second;
        nullIt++;
    }

    if (nullSize < size) {
        cout << "diskfull" << endl;
        return;
    }

    nullIt = find_if(disk.begin(), disk.end(), [size](pair<string,int> file) {return file.first == "" && file.second >= size;});
    if( nullIt != disk.end()) {
        if( nullIt->second > size) {
            disk.insert(nullIt, make_pair(fileName, size));
            nullIt->second -= size;
            return;
        }
        else {
            nullIt->first = fileName;
            return;
        }
    }

    nullIt = disk.begin();
    while (size != 0) {
        nullIt = find_if(nullIt, disk.end(), [](pair<string,int> file) {return file.first == "";});
        if( nullIt->second <= size) {
            nullIt->first = fileName;
            size -= nullIt->second;
        }
        else {
            disk.insert(nullIt, make_pair(fileName, size));
            nullIt->second -= size;
            size = 0;
        }
    }
}

void deleteFile() {
    string fileName; cin >> fileName;
    int counter = 0;
    auto deleteIt = disk.begin();
    while (true) {
        deleteIt = find_if(deleteIt, disk.end(), [fileName](pair<string,int> file) {return file.first == fileName;});
        if( counter == 0 && deleteIt == disk.end() ) {
            cout << "error" << endl;
            return;
        }

        if( deleteIt == disk.end() ) break;
        deleteIt->first = "";
        deleteIt++;
        counter++;
    }

    for (auto it=disk.begin(); it!=prev(disk.end()); ++it) {
        if (it->first == "") {
            auto nextIt = next(it);
            if (nextIt != disk.end() && nextIt->first == "") {
                it->second += nextIt->second;
                disk.erase(nextIt);
            }
        }
    }
}

void showFile() {
    string fileName; cin >> fileName;

    int accumulatedSum = 0;
    vector<int> toPrint;
    for (auto p : disk) {
        if (p.first == fileName) toPrint.push_back(accumulatedSum);
        accumulatedSum += p.second;
    }
    if( toPrint.empty() ) {
        cout << "error" << endl;
        return;
    }
    for (auto p : toPrint) {
        cout << p;
        if (p != toPrint.back()) cout << " ";
    }
    cout << endl;
}

void compactFile() {
    auto it = disk.begin();
    while (it != disk.end()) {
        if( it != disk.begin() && it->first == prev(it)->first) {
            prev(it)->second += it->second;
            it = disk.erase(it);
            continue;
        }
        if( *it != disk.back() && it->first == "" ) {
            disk.push_back(make_pair("", it->second));
            it = disk.erase(it);
            if( prev(disk.end(),2)->first == "") {
                prev(disk.end(),2)->second += disk.back().second;
                disk.pop_back();
            }
            continue;
        }
        it++;
    }
}
int main() {
    int V; cin >> V;
    disk.push_back({"", V});
    while (true) {
        string operation; cin >> operation;

        if (operation == "write") writeFile();
        else if (operation == "delete") deleteFile();
        else if (operation == "show") showFile();
        else if (operation == "compact") compactFile();
        else if (operation == "end") break;
    }

    return 0;
}