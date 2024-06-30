#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Node {//a node for the tree
    string name;
    Node* left;
    Node* right;

    Node(string _name) : name(_name), left(nullptr), right(nullptr) {}
};

Node* insertSequentially(Node* root, string name) {//inserts nodes lexicographically, if it's smaller to the left, bigger to the right
    if (root == nullptr) {
        return new Node(name);
    }
    if (name < root->name) {
        root->left = insertSequentially(root->left, name);
    }
    else {
        root->right = insertSequentially(root->right, name);
    }
    return root;
}

Node* findLCA(Node* root, string name1, string name2) {//if it's the end, return nothing. if both strings are on other sides of the root, then the root is the LCA
    if (root == nullptr) {
        return nullptr;
    }

    if (name1 < root->name && name2 < root->name) {//both strings are on the left side, so search more to the left
        return findLCA(root->left, name1, name2);
    }

    if (name1 > root->name && name2 > root->name) {//both strings are on the right side, so search more to the right
        return findLCA(root->right, name1, name2);
    }

    return root;
}

void printAncestors(Node* root, string target) {
    if (root == nullptr) {
        return;
    }

    if (root->name == target) {
        cout << root->name << endl;
        return;
    }
    else if (target < root->name) {
        cout << root->name << endl;
        printAncestors(root->left, target);
    }
    else {
        cout << root->name << endl;
        printAncestors(root->right, target);
    }
}

int main() {
    string name1, name2;
    int N;
    getline(cin, name1); // Read the first name as a full line
    getline(cin, name2); // Read the second name as a full line
    cin >> N;

    Node* root = nullptr;

    for (int i = 0; i < N; i++) {
        string name;
        //cin.ignore(); // Consume newline character
        getline(cin, name); // Read full name as a line
        root = insertSequentially(root, name);
    }

    Node* lca = findLCA(root, name1, name2);

    if (lca) {
        printAncestors(root, lca->name);
    }

    return 0;
}
