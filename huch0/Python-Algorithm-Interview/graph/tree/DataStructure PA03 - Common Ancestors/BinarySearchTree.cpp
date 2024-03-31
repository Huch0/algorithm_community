#include <iostream>
#include <string>
#include <stack>
#include <queue>

class binarySearchTree {
    class node {
    public:
        std::string name_;
        node* left_;
        node* right_;
        std::queue<node*> ancestors_;

        node(std::string name) : name_(name), left_(NULL), right_(NULL) {};
        ~node() {};

        bool isExternal () const {
            return left_ == NULL && right_ == NULL;
        }

        void addAncestor(node* ancestor) {
            ancestors_.push(ancestor);
        }
    };

private:
    node* root_;

public:
    binarySearchTree() : root_(NULL) {};
    ~binarySearchTree() {
        removeSubTree(root_);
    };

    // Insert new name to binary search tree
    void insert(std::string name) {
        std::queue<node*> ancestors;

        if (root_ == NULL) { // bst is empty
            root_ = new node(name);
            root_->addAncestor(root_);
            return;
        }
        node* newNode = new node(name);

        node* current = root_;

        node* parent = NULL;

        // Find the proper position for new node
        while (current != NULL) {
            parent = current;
            newNode->addAncestor(parent);
            // Smaller node will be in left subtree
            if (name <= current->name_) {
                current = current->left_;
            } else { // Bigger node will be in right subtree
                current = current->right_;
            }
        }
        // This is proper position
        if (name <= parent->name_ ) { // Bigger node should be in left
            parent->left_ = newNode;
        } else { // Bigger node should be in right
            parent->right_ = newNode;
        }
        // Add itself as ancestor
        newNode->addAncestor(newNode);
    }


    // Remove the subtree of specific node pointer
    // Remove the subtree of specific node pointer
    void removeSubTree(node* position) {
        if (position == NULL) // subtree is empty
            return;

        node* current;
        std::stack<node*> nodeStack;

        // Add position to the stack
        nodeStack.push(position);

        // DFS
        while (!nodeStack.empty()) {
            current = nodeStack.top();
            nodeStack.pop();

            // Add left and right nodes to the stack
            if (current->left_ != NULL)
                nodeStack.push(current->left_);
            if (current->right_ != NULL)
                nodeStack.push(current->right_);

            delete current;
        }
    }


    // Search the node with name
    node* search(std::string searchName) {
        node* current = root_;

        while (current != NULL) {
            // Found the node
            if (searchName == current->name_)
                return current;

            // Smaller node will be in left subtree
            if (searchName <= current->name_ ) {
                current = current->left_;
            } else { // Bigger node will be in right subtree
                current = current->right_;
            }
        }
        // searchName was not in bst
        return current;
    }

    // Print common ancestors of two nodes
    void commonAncestors(std::string firstPersonName, std::string secondPersonName) {
        node* firstPerson = search(firstPersonName);
        node* secondPerson = search(secondPersonName);

        // Get ancestors of each node
        std::queue<node*> firstPersonAncestors = firstPerson->ancestors_;
        std::queue<node*> secondPersonAncestors = secondPerson->ancestors_;

        while (firstPersonAncestors.size() > 0 && secondPersonAncestors.size() > 0) {
            node* firstPersonAncestor = firstPersonAncestors.front();
            firstPersonAncestors.pop();

            node* secondPersonAncestor = secondPersonAncestors.front();
            secondPersonAncestors.pop();

            // They're not common ancestor
            if (firstPersonAncestor != secondPersonAncestor)
                return;

            // It is common ancestor
            std::cout << firstPersonAncestor->name_ << std::endl;
        }
    }

    // Display the content of bst
    void display() const {
        if (root_ == NULL) {
            std::cout << "Tree is empty!" << std::endl;
            return;
        }

        std::queue<node*> nodeQueue;
        nodeQueue.push(root_);

        int level = 0;

        while (!nodeQueue.empty()) {
            int nodeCount = nodeQueue.size();
            std::cout << "Level " << level << ": ";

            // Traverse nodes of same level
            while (nodeCount > 0) {
                node* current = nodeQueue.front();
                nodeQueue.pop();

                if (current != NULL) {
                    std::cout << "[" << current->name_ << "] ";

                    // Add left and right to the queue
                    nodeQueue.push(current->left_);
                    nodeQueue.push(current->right_);
                } else {
                    std::cout << "[Empty] ";
                }

                nodeCount--;
            }

            // End of Traversal of one level
            std::cout << std::endl;
            level++;
        }
    }


};
int main() {
    std::string firstPersonName;
    std::string secondPersonName;
    int N = 0;
    binarySearchTree bst;

    // Get first person's name
    getline(std::cin, firstPersonName);

    // Get second person's name
    getline(std::cin, secondPersonName);

    // Get an integer N which is the number of the total people
    std::cin >> N;
    std::cin.ignore(); // To consume the newline character after the integer

    // Add each person's name to the bst
    for (int i = 0; i < N; i++) {
        std::string newPersonName;
        getline(std::cin, newPersonName);
        bst.insert(newPersonName);
    }

    bst.commonAncestors(firstPersonName, secondPersonName);

    return 0;
}
