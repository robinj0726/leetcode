#include <iostream>
#include <vector>

int maxChunksToSorted(std::vector<int>& arr) {
  int chunks = 0;
  int max_val = 0;

  for (int i = 0; i < arr.size(); i++) {
    max_val = std::max(max_val, arr[i]);
    if (max_val == i) {
      chunks++;
    }
  }

  return chunks;
}

int main() {
  // Test the function
   std::vector<int> arr = {4, 3, 2, 1, 0};
  //std::vector<int> arr = {1, 0, 2, 3, 4};
  int result = maxChunksToSorted(arr);
  std::cout << "Max Chunks to Sort: " << result << std::endl;

  return 0;
}