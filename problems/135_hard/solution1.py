def candy(ratings):
    # Step 1: Initialize the candies array with all elements set to 1
    candies = [1] * len(ratings)

    # Step 2: Traverse the ratings array from left to right
    for i in range(1, len(ratings)):
        # If the current rating is greater than the previous rating, assign one more candy
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    # Step 3: Traverse the ratings array from right to left
    for i in range(len(ratings)-2, -1, -1):
        # If the current rating is greater than the next rating, and the current candy count is less or equal,
        # assign one more candy than the next rating
        if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
            candies[i] = candies[i+1] + 1

    # Step 4: Return the sum of all candies
    return sum(candies)

