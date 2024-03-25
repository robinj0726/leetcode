#include <iostream>
#include <vector>

using namespace std;

vector<int> findDisappearedNumbers(vector<int>& nums) {
  vector<int> result;
  for (const int& num : nums) {
    // Inside the loop, the function calculates the index of the current element by taking the absolute value of the element (abs(nums[i])) and subtracting 1. This is done because the elements in nums are treated as indices, and we need to convert them to zero-based indices.
    int index = abs(num) - 1;
    if (nums[index] > 0) {
      nums[index] = -nums[index];
    }
  }
  for (int i = 0; i < nums.size(); i++) {
    if (nums[i] > 0) {
      result.push_back(i + 1);
    }
  }
  return result;
}

int main() {
  vector<int> nums = {4, 3, 2, 7, 8, 2, 3, 1};
  vector<int> result = findDisappearedNumbers(nums);
  for (int num : result) {
    cout << num << " ";
  }
}