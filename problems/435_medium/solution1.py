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
