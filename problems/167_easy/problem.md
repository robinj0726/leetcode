# Two Sum II - Input array is sorted

## Problem Description

Given an array of integers `numbers` that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function `twoSum` should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

- Your returned answers (both index1 and index2) are not zero-based.
- You may assume that each input would have exactly one solution and you may not use the same element twice.

## Example

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.

## Constraints

- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in increasing order.
- -1000 <= target <= 1000

## Follow-up

Can you come up with an algorithm that is less than O(n^2) time complexity?
