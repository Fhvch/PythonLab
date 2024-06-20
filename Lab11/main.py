def task1(numbers):
    return sum(x**2 for x in numbers)

def task2(numbers):
    avg = sum(numbers) / len(numbers)
    return sum(x for x in numbers if x >= avg)

def task3(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    sorted_numbers = sorted(numbers, key=lambda x: (-frequency[x], x))

    return sorted_numbers

def task4(numbers):
    n = len(numbers) + 1
    total_sum = n * (n + 1) // 2

    missing_number = total_sum - sum(numbers)

    return missing_number

def task5(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

def task6(nums, k):
    k = k % len(nums)

    rotated_nums = nums[-k:] + nums[:-k]

    return rotated_nums

def task7(nums):
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    result = [1] * n

    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    for i in range(n):
        result[i] = left_products[i] * right_products[i]

    return result

def task8(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)

        max_sum = max(max_sum, current_sum)

    return max_sum

def task9(matrix):
    if not matrix:
        return []

    result = []
    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

def task10(points, k):
    distances = [(point[0] ** 2 + point[1] ** 2, point) for point in points]

    distances.sort(key=lambda x: x[0])

    result = [point for _, point in distances[:k]]

    return result













