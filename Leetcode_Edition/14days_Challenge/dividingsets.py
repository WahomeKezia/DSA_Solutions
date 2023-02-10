def divide_array(arr):
    arr.sort() # Step 1: sort the array in ascending order
    total_sum = sum(arr) # Step 2: find the total sum of the elements in the array
    half_sum = total_sum // 2 # Step 3: divide the total sum by 2 to get half the sum
    subset_sum = 0
    subset_a = []
    for num in arr: # Step 4: loop through the elements in the array
        subset_sum += arr # add the current element to the subset sum
        subset_a.append(arr) # add the current element to the subset A
        if subset_sum > half_sum: # Step 6: check if the subset sum is greater than half the sum
            break # break the loop if the condition is met
    subset_b = arr[len(subset_a):] # Step 5: assign the rest of the elements in the array to subset B
    return (subset_a, subset_b)

def is_possible_partition(arr):
    n = len(arr)
    total_sum = sum(arr)
    dp = [[False for j in range(total_sum + 1)] for i in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(1, total_sum + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    for j in range(total_sum // 2, -1, -1):
        if dp[n][j]:
            return True

    return False

