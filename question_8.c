#include<stdio.h>
#include<stdlib.h>
struct node {
   struct node* left;
   struct node* right;
   int data;
};
struct node* New(int data) {
   struct node* temp = (struct node*)malloc(sizeof(struct node));
   temp->data = data;
   temp->left = NULL;
   temp->right = NULL;
   return temp;
}
void leaf(struct node* root, int level) {
   if (root == NULL)
      return;
   if (level == 1) {
      if (root->left == NULL && root->right == NULL)
      printf("%d\n",root->data);
   } else if (level > 1) {
      leaf(root->left, level - 1);
      leaf(root->right, level - 1);
   }
}
int main() {
   printf("leaf nodes are: ");
   struct node* root = New(15);
   root->left = New(22);
   root->right = New(43);
   root->left->left = New(66);
   root->right->right = New(45);
   root->left->left->left = New(78);
   root->left->left->right = New(87);
   int level = 4;
   leaf(root, level);
   return 0;
}
