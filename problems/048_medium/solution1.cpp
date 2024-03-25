#include <vector>
#include <iostream>
using namespace std;

/* 
  1, 2, 3       1, 4, 7     7, 4, 1
  4, 5, 6   ->  2, 5, 8  -> 8, 5, 2
  7, 8, 9       3, 6, 9     9, 6, 3
*/
void rotate(vector<vector<int>>& matrix) {
  int n = matrix.size();
  // iterate over the upper triangular part of the matrix
  for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
      // swap the elements along the diagonal line
      swap(matrix[i][j], matrix[j][i]);
    }
  }
  for (int i = 0; i < n; i++) {
    reverse(matrix[i].begin(), matrix[i].end());
  }
}

int main() {
  vector<vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
  
  rotate(matrix);
  
  // Print the rotated matrix
  for (int i = 0; i < matrix.size(); i++) {
    for (int j = 0; j < matrix[i].size(); j++) {
      cout << matrix[i][j] << " ";
    }
    cout << endl;
  }
  
  return 0;
}