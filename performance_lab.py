from collections import Counter

def most_frequent(numbers):
    if not numbers:
        return None  # Handle empty list case
    counts = Counter(numbers)
    return counts.most_common(1)[0][0]
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # Output: 3
def test_most_frequent():
    # Basic test case
    assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3

    # Tie case: 1 and 2 both appear twice
    assert most_frequent([1, 2, 1, 2]) in [1, 2]

    # Single element
    assert most_frequent([42]) == 42

    # All elements unique
    assert most_frequent([5, 6, 7, 8]) in [5, 6, 7, 8]

    # Empty list
    assert most_frequent([]) is None

    # Negative numbers
    assert most_frequent([-1, -2, -1, -3]) == -1

    # Large list with clear winner
    assert most_frequent([9]*100 + [8]*50 + [7]*25) == 9

    # Mixed types (if allowed)
    assert most_frequent([1, 'a', 'a', 2]) == 'a'

    print("All tests passed!")

test_most_frequent()



"""
Time and Space Analysis for problem 1:
- Even if the first item is the most frequent one, Counter must still iterate over all n elements to build the counts.
- the worst case is O(n + k log k)
- the average case is still requires counting all n elements and sorting or heapifying k items.
- O(k) where k = number of unique elements in the list
- this approach because its simple, readable, and concise
- yes, You could manually count elements and track the current most frequent element during iteration
the trade offs are Using Counter (original) and also manual tracking.
"""


def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
def test_remove_duplicates():
    # Test 1: Basic case with duplicates
    assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]

    # Test 2: All unique elements
    assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]

    # Test 3: All identical elements
    assert remove_duplicates([9, 9, 9, 9]) == [9]

    # Test 4: Empty list
    assert remove_duplicates([]) == []

    # Test 5: Single element
    assert remove_duplicates([42]) == [42]

    # Test 6: Negative numbers
    assert remove_duplicates([-1, -2, -1, -3]) == [-1, -2, -3]

    # Test 7: Mixed types (if allowed)
    assert remove_duplicates([1, '1', 1, '1']) == [1, '1']

    # Test 8: Large input
    large_input = list(range(1000)) + list(range(500))
    expected_output = list(range(1000))
    assert remove_duplicates(large_input) == expected_output

    print("All tests passed!")

test_remove_duplicates()


"""
Time and Space Analysis for problem 2:
- Even if all elements are duplicates, we still scan each of the n elements once. So the loop runs in O(n) time.
- Even if all n elements are unique, each is added to the set and result list.
- Whether few or many duplicates, we're still scanning all n items and doing O(1) work per item.
- the Space complexity is O(k), where k ≤ n
- i picked this approach because it is the most efficient way to remove duplicates while also preserving order.
- yes it can be optimized
- there are a good few of trade offs like less readable for beginners, Still only works with hashable elements, May seem like a "hack" or be less transparent, Slightly more verbose
"""


def find_pairs(nums, target):
    seen = set()
    pairs = set()
    
    for num in nums:
        complement = target - num
        if complement in seen:
            # Use tuple with sorted values to avoid duplicates like (1,4) and (4,1)
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    
    return list(pairs)

print(find_pairs([1, 2, 3, 4], target=5))
# Output: [(1, 4), (2, 3)]

def test_find_pairs():
    # Basic test case
    assert sorted(find_pairs([1, 2, 3, 4], 5)) == sorted([(1, 4), (2, 3)])

    # No pairs sum to target
    assert find_pairs([1, 2, 3], 10) == []

    # Empty list
    assert find_pairs([], 5) == []

    # Single element list
    assert find_pairs([5], 5) == []

    # Negative numbers
    assert sorted(find_pairs([-1, -2, -3, -4], -5)) == sorted([(-1, -4), (-2, -3)])

    # Mixed positive and negative numbers
    assert sorted(find_pairs([-2, 0, 2, 4], 2)) == sorted([(-2, 4), (0, 2)])

    # Zero as target
    assert sorted(find_pairs([-3, 0, 3], 0)) == sorted([(-3, 3)])

    # Large numbers
    assert sorted(find_pairs([1000000, 500000, -500000], 0)) == sorted([(500000, -500000)])

    # Multiple valid pairs
    assert sorted(find_pairs([1, 3, 5, 7, 9], 10)) == sorted([(1, 9), (3, 7)])

    print("All test cases passed!")

# Run the tests
    test_find_pairs()
"""
Time and Space Analysis for problem 3:
- Even if no valid pairs are found, the loop still iterates through all n items once.
- Even if many valid pairs are found, inserting into a set is O(1) (average).
- All realistic scenarios take O(n) time very efficient.
- seen → stores up to n items → O(n) pairs → stores up to n/2 unique pairs → O(n) in the worst case
- i chose this approach because first of all it avoids nested loops (no O(n²) time), Fast O(1) average-time lookups
- yes this could be optimized
- Captures all valid pairs (even duplicates), More memory (O(n)), Slightly more complex
"""


def add_n_items(n):
    capacity = 2  # Initial capacity
    size = 0      # Current number of items
    lst = [None] * capacity  # Simulated fixed-size list

    for i in range(n):
        if size == capacity:
            print(f"Resizing from capacity {capacity} to {capacity * 2}")
            new_lst = [None] * (capacity * 2)
            for j in range(size):
                new_lst[j] = lst[j]
            lst = new_lst
            capacity *= 2

        lst[size] = i
        size += 1

    print("Final list contents:", lst[:size])
    add_n_items(6)

def add_n_items(n):
    capacity = 2
    size = 0
    lst = [None] * capacity

    for i in range(n):
        if size == capacity:
            print(f"Resizing from capacity {capacity} to {capacity * 2}")
            new_lst = [None] * (capacity * 2)
            for j in range(size):
                new_lst[j] = lst[j]
            lst = new_lst
            capacity *= 2

        lst[size] = i
        size += 1

    print("Final list contents:", lst[:size])
    return lst[:size]
def test_add_n_items():
    print("\nTest Case 1: n = 0 (Edge case: empty list)")
    result = add_n_items(0)
    assert result == [], f"Expected [], got {result}"

    print("\nTest Case 2: n = 1 (No resizing)")
    result = add_n_items(1)
    assert result == [0], f"Expected [0], got {result}"

    print("\nTest Case 3: n = 2 (Exactly fills initial capacity)")
    result = add_n_items(2)
    assert result == [0, 1], f"Expected [0, 1], got {result}"

    print("\nTest Case 4: n = 3 (Triggers one resize)")
    result = add_n_items(3)
    assert result == [0, 1, 2], f"Expected [0, 1, 2], got {result}"

    print("\nTest Case 5: n = 6 (Triggers multiple resizes)")
    result = add_n_items(6)
    assert result == [0, 1, 2, 3, 4, 5], f"Expected [0, 1, 2, 3, 4, 5], got {result}"

    print("\nTest Case 6: n = 100 (Stress test)")
    result = add_n_items(100)
    assert result == list(range(100)), f"Expected range(100), got {result}"

    print("\nAll test cases passed!")

test_add_n_items()


"""
Time and Space Analysis for problem 4:
- Resizing happens when the list is full, and it doubles its capacity.
- The worst-case for a single append is when a resize is triggered
- amortized time per append is 0(1)
- space complexity: The array grows to fit all n items, and at some points, has extra unused capacity.
- If instead of doubling, you increased capacity by a fixed amount (say +1 each time), resizing would be very frequent
"""


def running_total(nums):
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result

print(running_total([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]

def running_total(nums):
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result
def test_running_total():
    # Basic case
    assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]

    # Edge case: empty list
    assert running_total([]) == []

    # Edge case: single element
    assert running_total([5]) == [5]

    # Negative numbers
    assert running_total([-1, -2, -3]) == [-1, -3, -6]

    # Mixed positive and negative
    assert running_total([3, -1, 4, -2]) == [3, 2, 6, 4]

    # All zeros
    assert running_total([0, 0, 0]) == [0, 0, 0]

    # Large numbers
    assert running_total([1000, 2000, 3000]) == [1000, 3000, 6000]

    print("All tests passed!")

test_running_total()

"""
Time and Space Analysis for problem 5:
- Even in the best case, you still loop through the list.
- All elements must be visited regardless of values.
- Same as best and worst, linear pass through nums.
- Space complexity: O(n), You build a new result list of length n. im not modifying the original list (nums), so this is not done in-place.
- this approach is simple, readable, and efficient
- Could it be optimized? yes it can
-the trade offs are Safe, preserves input for no Uses of extra space. Saves memory so it doesnt Mutates input (not always acceptable)
"""



from typing import List, Tuple, Set

def find_pairs(nums: List[int], target: int) -> List[Tuple[int, int]]:
    seen: Set[int] = set()
    pairs: Set[Tuple[int, int]] = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            pair = tuple(sorted((num, complement)))
            pairs.add(pair)
        seen.add(num)
    
    return list(pairs)

def test_find_pairs():
    assert sorted(find_pairs([1, 2, 3, 4], 5)) == sorted([(1, 4), (2, 3)])
    assert find_pairs([1, 2, 3], 10) == []
    assert find_pairs([], 5) == []
    assert find_pairs([5], 5) == []
    assert sorted(find_pairs([-1, -2, -3, -4], -5)) == sorted([(-1, -4), (-2, -3)])
    assert sorted(find_pairs([-2, 0, 2, 4], 2)) == sorted([(-2, 4), (0, 2)])
    assert sorted(find_pairs([-3, 0, 3], 0)) == sorted([(-3, 3)])
    assert sorted(find_pairs([1000000, 500000, -500000], 0)) == sorted([(500000, -500000)])
    assert sorted(find_pairs([1, 3, 5, 7, 9], 10)) == sorted([(1, 9), (3, 7)])
    print("All test cases passed!")

    print(find_pairs([1, 2, 3, 4], target=5))  # Output: [(1, 4), (2, 3)]
    test_find_pairs()

