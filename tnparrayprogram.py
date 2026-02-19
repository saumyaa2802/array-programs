

#roll no- 0157CY231116


#Reverse an array
arr=list(map(int,input('Enter the values: ').split()))
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)


#Find minimum and maximum value in array
arr=list(map(int,input("Enter the values: ").split()))
maximum=arr[0]
minimum=arr[0]
for num in arr:
    if num >= maximum:
        maximum=num
    if num <= minimum:
        minimum=num
print("MAX: ",maximum)
print("MIN: ",minimum)

#sum of elements in an array
arr=list(map(int,input("Enter the values: ").split()))
left=0
for num in arr:
    left+=num
print("SUM: ",left)

#Count Frequency Of Elements
arr=list(map(int,input("Enter The Values: ").split()))
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print(freq)

#Find The Second Largest Element in an array
arr=list(map(int,input("Enter the values: ").split()))
largest=float('-inf')
second=('-inf')
for num in arr:
    if num>largest:
        second=largest
        largest=num
    if num>second and num!=largest:
        second=num
print("The Second Largest Number Is: ",second)

# Maximum Difference (j > i)
def max_difference(arr):
    min_val = arr[0]
    max_diff = arr[1] - arr[0]
    for i in range(1, len(arr)):
        max_diff = max(max_diff, arr[i] - min_val)
        min_val = min(min_val, arr[i])
    return max_diff

# Equilibrium Index
def equilibrium_index(arr):
    total = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        total -= num
        if left_sum == total:
            return i
        left_sum += num
    return -1


#Product of Array Except Self(No Division)

def product_except_self(arr):
    n = len(arr)
    result = [1] * n

    left = 1
    for i in range(n):
        result[i] = left
        left *= arr[i]

    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= arr[i]

    return result

# Longest Consecutive Sequence
def longest_consecutive(arr):
    s = set(arr)
    longest = 0
    for num in s:
        if num - 1 not in s:
            length = 1
            while num + length in s:
                length += 1
            longest = max(longest, length)
    return longest

# Sort 0s, 1s, 2s (Dutch National Flag)
def sort_012(arr):
    low = mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# First Missing Positive
def first_missing_positive(arr):
    s = set(arr)
    i = 1
    while True:
        if i not in s:
            return i
        i += 1

#Find Peak Element
def find_peak(arr):
    n = len(arr)
    for i in range(n):
        if (i == 0 or arr[i] >= arr[i-1]) and (i == n-1 or arr[i] >= arr[i+1]):
            return arr[i]

#Majority Element (> n/2 times)
def majority_element(arr):
    count = 0
    candidate = None
    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    if arr.count(candidate) > len(arr)//2:
        return candidate
    return None

#Rearrange Alternately (Largest, Smallest)
def rearrange_alternate(arr):
    arr.sort()
    result = []
    left, right = 0, len(arr) - 1
    while left <= right:
        if left != right:
            result.append(arr[right])
            result.append(arr[left])
        else:
            result.append(arr[left])
        left += 1
        right -= 1
    return result

#Maximum Sum Subarray (Kadane’s Algorithm)
def max_subarray_sum(arr):
    max_sum = curr_sum = arr[0]
    for num in arr[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

#22. Find All Subarrays
def all_subarrays(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            result.append(arr[i:j+1])
    return result

#Subarray with Given Sum (Positive Numbers)
def subarray_sum(arr, target):
    start = curr_sum = 0
    for end in range(len(arr)):
        curr_sum += arr[end]
        while curr_sum > target:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == target:
            return arr[start:end+1]
    return None

#Rotate Left by k Positions
def rotate_left(arr, k):
    n = len(arr)
    k %= n
    return arr[k:] + arr[:k]

#Move Zeroes to End
def move_zeroes(arr):
    non_zero = [x for x in arr if x != 0]
    zeros = [0] * (len(arr) - len(non_zero))
    return non_zero + zeros

#Find Leader Elements
def leaders(arr):
    max_right = arr[-1]
    result = [max_right]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > max_right:
            max_right = arr[i]
            result.append(arr[i])
    return result[::-1]

#Union of Two Arrays
def union(arr1, arr2):
    return list(set(arr1) | set(arr2))

#Check if Two Arrays Are Equal
def arrays_equal(arr1, arr2):
    return sorted(arr1) == sorted(arr2)

#Find Duplicates
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)

#Find the Missing Number (1 to n)
def missing_number(arr, n):
    expected = n * (n + 1) // 2
    return expected - sum(arr)

#Merge Two Sorted Arrays
def merge_sorted(arr1, arr2):
    i = j = 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

#Intersection of Two Arrays
def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

#Remove Duplicates (Maintain Order)
def remove_duplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

#Find Pair with Given Sum
def pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return (num, target - num)
        seen.add(num)
    return None

#Rotate Array Right by k Positions
def rotate_right(arr, k):
    n = len(arr)
    k %= n
    return arr[-k:] + arr[:-k]

#Check if Array is Sorted
def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


#Maximum product pair
def max_product_pair(arr):
    if len(arr) < 2:
        return None

    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for num in arr:
        # Update maximums
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        # Update minimums
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    if max1 * max2 > min1 * min2:
        return (max2, max1)
    else:
        return (min1, min2)

# Example
arr = [1, -4, 3, -6, 7, 0]
print(max_product_pair(arr))
