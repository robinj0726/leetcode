#include <iostream>
#include <vector>

bool searchMatrix(std::vector<std::vector<int>>& matrix, int target) {
  if (matrix.empty() || matrix[0].empty()) {
    return false;
  }
  
  int rows = matrix.size();
  int cols = matrix[0].size();
  
  int row = 0;
  int col = cols - 1;

//  It starts from the top-right corner of the matrix and moves either left or down depending on the comparison between the current value and the target value. By following this pattern, the loop efficiently searches through the matrix until it stops at (rows - 1, 0)

  while (row < rows && col >= 0) {
    if (matrix[row][col] == target) {
      return true;
    } else if (matrix[row][col] < target) {
      row++;
    } else {
      col--;
    }
  }
  
  return false;
}

int main() {
  // Test the searchMatrix function
  std::vector<std::vector<int>> matrix = {
    {1, 4, 7, 11, 15},
    {2, 5, 8, 12, 19},
    {3, 6, 9, 16, 22},
    {10, 13, 14, 17, 24},
    {18, 21, 23, 26, 30}
  };
  
  int target = 5;
  
  bool found = searchMatrix(matrix, target);
  
  if (found) {
    std::cout << "Target found in the matrix." << std::endl;
  } else {
    std::cout << "Target not found in the matrix." << std::endl;
  }
  
  return 0;
}