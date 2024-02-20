A common approach to solve the "Non-overlapping Intervals" problem is to use a greedy algorithm. The idea is to sort the intervals by their end times and always select the interval with the earliest end time. This leaves the maximum room for the rest of the intervals.

Here is a Python solution using this approach:

```python
def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    # Sort the intervals by end time
    intervals.sort(key=lambda x: x[1])

    end = intervals[0][1]
    count = 0

    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            # If the current interval overlaps with the previous one, increment count
            count += 1
        else:
            # Otherwise, update the end time
            end = intervals[i][1]

    return count
```

In this solution, `eraseOverlapIntervals` function sorts the intervals by their end times. It then iterates over the sorted intervals, and for each interval, if its start time is less than the end time of the previous interval, it increments a counter. If not, it updates the end time to the end time of the current interval. The counter represents the minimum number of intervals that need to be removed to make the rest non-overlapping.

The time complexity of this solution is O(n log n) due to the sorting operation, where n is the number of intervals. The space complexity is O(1) if the sorting operation is considered to be in-place, or O(n) if not (depending on the specific sorting algorithm used by Python in the background).