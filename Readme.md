# Introduction
This document contains solutions for the Neetcode 150 problems. I plan to cover all 150 problems in the next 150 days, tackling one problem per day.

# Arrays and Hashing Problem

## Day 1 - Contains Duplicate
Given an integer array `nums`, return `true` if any value appears more than once, otherwise return `false`.

## Day 2 - Anagrams
Given two strings "stringa" and "stringb", return `true` if they are anagrams of each other, otherwise return `false`.

Anagram : An anagram is a string that has the exact same characters as another string, but in a different order.

Approaches used:
* Hashmap : adding in hashmap and comparing characterwise match of number of appearance
* Sorting : sorting and then comparing equality

## Day 3 - Two Sum
Given an array and a target, find the indices of two elements whose sum equals the target.

Approaches used:
* Brute force
* One-pass approach : subtracting element from target and finding the resultant in hashmap.

## Day 4 -  Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

## Day5 - Top k frequent
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

## Day 6 - Encode decode problem
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

## Day 7 - Product of Array except self
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in (n) time without using the division operation?

## Day 8 - Valid Sudoku Board
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

- Each row must contain the digits 1-9 without duplicates.
- Each column must contain the digits 1-9 without duplicates.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return `true` if the Sudoku board is valid, otherwise return `false`

Note: A board does not need to be full or be solvable to be valid.

## Day 9 - Longest Consecutive Sequence
Given an array of integers `nums`, return the `length` of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in `O(n)` time.

# Two pointer

## Day 10 - Valid Palindrome
Given a string `s`, return `true` if it is a **palindrome**, otherwise return `false`.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

`Note`: Alphanumeric characters consist of letters `(A-Z, a-z)` and numbers `(0-9)`.

## Day 11 - Two Sums II
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices **(1-indexed)** of two numbers, `[index1, index2]`, such that they add up to a given target number `target` and `index1 < index2`. Note that `index1` and `index2` cannot be equal, therefore you may not use the same element twice.

There will always be **exactly one valid solution**.

Your solution must use O(1) additional space.

## Day 12 - Three Sum 
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` where `nums[i] + nums[j] + nums[k] == 0`, and the indices `i`, `j`and `k` are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in **any order**.

## Day 13 - Container with most water
You are given an integer array `heights` where `heights[i]` represents the height of the _i<sup>th_</sup> bar.

You may choose any two bars to form a container. Return the _maximum_ amount of water a container can store.

## Day 14 - Trapping Rain Water
You’re given an array of non-negative integers `height`, where each `height[i]` denotes the height of a bar of width 1.  

Find and return the maximum area of water that can be held between any two bars.

## Day 15 - Best time to buy and sell stock
You are given an integer array prices, where prices[i] represents the price of individual stock of Tensorletters on the i-th day.

You can buy one Stock on a specific day and sell it on a later day.

Return the maximum profit that can be obtained from a single buy-sell transaction. If no profitable trade is possible, return 0.

## Day 16 - Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.

## Day 17 - Longest Repeating Character Replacement
Given a string s made up of uppercase English letters and an integer k, you are allowed to change at most k characters in the string to any other uppercase letter.

Task is to find the maximum possible length of a substring that can consist of the same character after performing up to k such replacements.

## Day 18 - Permutation in String
We are provided with two strings, s1 and s2.
We need to determine whether any rearrangement of s1 appears as a consecutive substring within s2 and return True if such a substring exists; otherwise, return False.

## Day 19 - Minimum Window Substring
Return the smallest substring of **s** that contains all characters of **t**, counting duplicates as well. If no such substring exists, return an empty string. You can assume there’s only one correct answer.

## Day 20 - Sliding Window Maximum 
You are given an array of integers nums and an integer k. A sliding window of size k moves from the left to the right of the array, shifting one position at a time.

At each step, return the maximum value within the current window.

*Approaches Used*
- Brute Force
- Deque

# Stack

## Day 21 - Valid Parentheses
You’re given a string s made up of '(', ')', '{', '}', '[', and ']'.

The string is valid if:
- Every opening bracket has a matching closing bracket of the same type.
- Brackets close in the correct order.
- No closing bracket appears without a corresponding opening bracket.

Return `true` if the string is valid, otherwise `false`.

## Day 22 - Minimum Stack
**Problem:**
Design a stack that supports `push`, `pop`, `top`, and retrieving the **minimum element** — all in **O(1)** time.

**Functions to implement:**

* `push(val)` → add element
* `pop()` → remove top
* `top()` → return top
* `getMin()` → return minimum

**Hint:**
Use an extra stack (`minStack`) to track the minimum so far.
Each time you push a value, also push the smaller of (value, current min) into `minStack`.

## Day 23 - Evaluate Reverse Polish Notation

**Problem:**
You are given an array of strings `tokens` representing an **arithmetic expression** in **Reverse Polish Notation (RPN)**.
Evaluate the expression and return the final result as an integer.

**Rules:**

* Valid operators are `+`, `-`, `*`, and `/`.
* Each operand may be an integer or another expression.
* Division between two integers should **truncate toward zero**.
* The input is always valid and results in an integer.

**Functions to implement:**

* `evalRPN(tokens: List[str]) -> int` → returns the evaluated result

**Hint:**
Use a **stack** to store numbers.
When you see an operator, pop the last two numbers, apply the operation, and push the result back.
Continue until the stack has one element left — that’s your answer.

**Example:**

```python
Input: tokens = ["2", "1", "+", "3", "*"]
Output: 9
# Explanation: ((2 + 1) * 3) = 9
```

## Day 24 - Generate Parenthesis
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Here’s a matching **README** for the **Daily Temperatures** problem in the same style:

---

## Day 25 - Daily Temperatures

**Problem:**
You are given an integer array `temperatures` where each element represents the daily temperature.
Return an array `answer` such that `answer[i]` is the **number of days** you have to wait after the `iᵗʰ` day to get a **warmer temperature**.
If there is no future day for which this is possible, set `answer[i] = 0`.

**Functions to implement:**

* `dailyTemperatures(temperatures: List[int]) -> List[int]` → returns an array representing the number of days to wait for a warmer temperature.

**Hint:**
Use a **monotonic decreasing stack** that stores indices of days.
While the current temperature is higher than the temperature at the top index of the stack,
pop the stack and calculate how many days it took to find a warmer one.

**Example:**

```python
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
# Explanation:
# Day 1 → wait 1 day for 74
# Day 2 → wait 1 day for 75
# Day 3 → wait 4 days for 76
# Day 7 → no warmer day ahead
```

**Key Insight:**
Instead of checking all future days for each temperature (O(n²)),
the **stack** helps us find the next warmer day in **O(n)** time.

## Day 27 - Largest Rectangle in Histogram

**Problem:**
You are given an array of integers `heights`, where `heights[i]` represents the **height of a bar** in a histogram.
Each bar has a **width of 1**.
Your task is to **return the area of the largest rectangle** that can be formed among these bars.

**Function to implement:**

* `largestRectangleArea(heights: List[int]) -> int` → returns the area of the largest rectangle

**Hint:**

1. Use a **stack** to keep track of bars' indices.
2. Bars in the stack should have **increasing heights**.
3. When a smaller height appears, **pop** from the stack and calculate the rectangle area:

   ```
   height = heights[popped_index]
   width = i - stack[-1] - 1   # if stack not empty
   width = i                   # if stack empty
   ```
4. Continue until all bars are processed — don’t forget to clear remaining bars from the stack.

**Example:**

```python
Input: heights = [2,1,5,6,2,3]
Output: 10

# Explanation:
# The rectangle formed by bars with height [5,6] has area 5*2 = 10.
```

**Intuition:**
Think of the histogram as **building walls** of different heights.
As you scan from left to right, the stack helps track where each wall **starts expanding**.
When you hit a shorter bar, it means the previous taller walls **end here**, so you compute their possible rectangle areas.
This ensures you efficiently find the **maximum area** using **O(n)** time.

# Binary Search

## Day 28 - Binary Search Algorithm

**Problem:**
Given a **sorted array** `nums` and an integer `target`, return the **index** of `target` if found; otherwise, return `-1`.

**Function to implement:**

* `search(nums: List[int], target: int) -> int`

**Hint:**

1. Keep two pointers : `left` and `right`.
2. Find the middle index:

   ```python
   mid = (left + right) // 2
   ```
3. Compare `nums[mid]` with `target` and **halve the search space** each time:

   * If equal → return `mid`
   * If smaller → move `left = mid + 1`
   * If larger → move `right = mid - 1`

**Example:**

```python
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
```

**Intuition:**
Binary Search applies the **divide and conquer** principle — repeatedly splitting the array in half to narrow down the target’s position, achieving **O(log n)** efficiency.

## Day 29 - Search a 2d Matrix
You are given an m x n 2-D integer array matrix and an integer target.
- Each row in matrix is sorted in non-decreasing order.
- The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

**Intuition**
Think of  implementing binary search to first search relevant row, and then search if a matching row is found. 

## Day 30 - Koko Eating Bananas

**Problem:**
You are given an array `piles`, where `piles[i]` represents the number of bananas in the *i-th* pile, and an integer `h` representing the total number of hours Koko has to eat all the bananas.
Koko can choose an integer eating speed `k` (bananas per hour). Each hour, she chooses a pile and eats up to `k` bananas from it. If the pile has fewer than `k` bananas, she eats them all and doesn’t continue to another pile that hour.

Your task is to find the **minimum integer speed `k`** such that Koko can eat all the bananas within `h` hours.

**Intuition:**
Use **binary search** on the range `[1, max(piles)]`.
For each possible `k`, calculate the total hours Koko would take to finish all piles.
If the total hours ≤ `h`, try a smaller speed; otherwise, increase `k`.

## Day 31 - Finding Minimum in Rotated Sorted Array

**Problem:**
You are given a rotated sorted array `nums` of unique integers. The array was originally sorted in ascending order but then rotated at an unknown pivot.  
Your task is to find the **minimum element** in the array.

**Intuition:**
Use **binary search** to efficiently locate the minimum element:
1. Check if the array is already sorted (i.e., `nums[left] < nums[right]`), in which case the first element is the minimum.
2. Otherwise, use the middle index to determine whether the mitounimum lies in the left or right half:
   - If `nums[mid] > nums[right]`, the minimum is in the right half.
   - If `nums[mid] < nums[right]`, the minimum is in the left half.
3. Narrow the search space until you find the minimum.

This approach ensures an **O(log n)** time complexity.

## Day 32 - Search in Rotated Sorted Array
**Problem:**
You are given a rotated sorted array `nums` of unique integers and an integer `target`. The array was originally sorted in ascending order but then rotated at an unknown pivot.  
Your task is to find the index of `target` in `nums`. If `target` is not found, return `-1`. 

**Intuition:**
Use **binary search** to efficiently locate the target:
1. Determine which half of the array is sorted.
2. Check if the target lies within the sorted half:
   - If it does, narrow the search to that half.         
   - If it doesn’t, search in the other half.

## Day 33 - Time Based Key-Value Store
**Problem:**
Design a time-based key-value store that can store multiple values for the same key at different timestamps and retrieve the value associated with a key at a specific timestamp.   
**Intuition:**
Use a **dictionary** to store keys and their corresponding values as a list of `(timestamp, value)` pairs.  
For retrieval, use **binary search** to efficiently find the largest timestamp less than or equal to the given timestamp.  
This ensures both insertion and retrieval operations are efficient, with retrieval taking **O(log n)** time for each query.

## Day 34 - Median of Two Sorted Arrays
**Problem:**
You are given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively. Your task is to find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

**Intuition:**
Use **binary search** on the smaller array to partition both arrays into left and right halves such that:
- All elements in the left halves are less than or equal to all elements in the right halves.
- The left halves contain half of the total elements (or one more if the total is
   odd).             

# Linked List Starts

## Day 35 - Reverse Linked List

**Problem:**
Given the head of a singly linked list, reverse the list and return the new head.

**Intuition 1: Iterative**
Use three pointers: `prev`, `curr`, and `next`.
- Initialize `prev = None` and `curr = head`.
- While `curr` is not `None`:
  - Store `curr.next` in `next`.
  - Reverse the link by setting `curr.next = prev`.
  - Move `prev` and `curr` one step forward.
- When the loop ends, `prev` will be the new head of the reversed list.

**Intuition 2: Recursive**
Use recursion to reverse the list:
- **Base case:** If `head` is `None` or `head.next` is `None`, return `head`.
- Recursively reverse the rest of the list.
- After the recursive call, set `head.next.next = head` and `head.next = None`.
- Return the new head (the result of the recursive call).

## Day 36 - Merge Linked list
Make a new sorted linked list by merging two sorted linked lists. New list should be made from nodes of old lists.

**Approach**:
- test the smalle value, and start the dummy node with smaller value.
- then keep adding smaller value node to the next of dummy node, while also moving the pointer of that list forward.
- finally return dummy.next

## Day 37 - Linked List Cycle
Given the head of a linked list, determine if the linked list has a cycle in it.

**Intuition(hashset approach):**
Note : this is not optimal approach, but easy to understand.
- Initialize an empty hash set to store visited nodes.
- Traverse the linked list starting from the head node.
- For each node, check if it is already in the hash set:
  - If it is, return `true` (cycle detected).
  - If it is not, add the node to the hash set and continue to the next node.
- If you reach the end of the list (`None`), return `false` (no cycle).

**Intuition(tortroise hare approach):**

Use two pointers, `slow` and `fast`.
- Initialize both pointers to the head of the list.
- Move `slow` one step at a time and `fast` two steps at a time.
- If there is a cycle, the `fast` pointer will eventually meet the `slow` pointer.
- If `fast` reaches the end of the list (`None`), then there is no cycle.

## Day 38 - Reorder Linked List 

You are given the head of a singly linked list.

The positions of a linked list of length `n` can initially be represented as:

`[0, 1, 2, ..., n-1]`

Reorder the nodes of the linked list to be in the following order:

`[0, n-1, 1, n-2, 2, n-3, ...]`

**Constraints**:
- You may not modify the values in the list's nodes.
- You must reorder the nodes themselves.

**Approach**:
- Use two pointers, `slow` and `fast`, both initialized to the head of the list.
- Move `slow` one step at a time and `fast` two steps at a time.
- Continue moving the pointers until `fast` reaches the end of the list or `slow` and `fast` meet.
- If `slow` and `fast` meet, a cycle exists in the linked list.
- If `fast` reaches the end (`None`), there is no cycle in the linked list.

**Example**:
```python
Input: head = [1, 2, 3, 4]
Output: [1, 4, 2, 3]
```

**Complexity**:
- Time Complexity: O(n) — Traversing the list multiple times.
- Space Complexity: O(1) — In-place reordering without extra space.

## Day 39 - Remove Nth Node From End of List
**Problem:**
Given the head of a linked list, remove the nth node from the end of the list and return its head.

**Approach:**
1. Use a two-pointer technique:
   - Initialize two pointers, `first` and `second`, both pointing to a dummy node before the head.
   - Move the `first` pointer `n + 1` steps ahead to create a gap of `n` nodes between `first` and `second`.
2. Move both pointers one step at a time until `first` reaches the end of the list.
3. The `second` pointer will now be just before the node to be removed. Adjust the `next` pointer of `second` to skip the target node.
4. Return the head of the modified list.

**Example:**
```python
Input: head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]
```

**Complexity:**
- Time Complexity: O(n) - Single traversal of the list.
- Space Complexity: O(1) - No extra space used.

## Day 40 - Copy Linked List with Random Pointer

**Problem**
Create a deep copy of a linked list where each node has an additional random pointer that can point to any node in the list or be null.

**Solution**
- Two pass apprach
- In first pass, make nodes
- In second class | Just like practical file. ||| is needed

**Complexity:**
- Time Complexity: O(n)
- Space Complexity: O(1)


## Day 41 - Two Sum in Linked List 

**Problem:**
You are given the heads of two sorted linked lists `list1` and `list2`, representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. 

**Example**
Input : list1 = [2,4,3], list2 = [5,6,4]
Output : [7,0,8]

**Approach:**
- Initialize a dummy node to build the result linked list.
- Use two pointers to traverse both linked lists.
- Add corresponding digits along with any carry from the previous addition.
- Create new nodes for the result linked list based on the sum.
- Return the next node of the dummy node as the head of the result linked list.

## Day 42 - Find the Duplicate Number

**Problem:**
You are given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.  
There is only one repeated number in `nums`, return this repeated number.

**Constraints:**
- You must solve the problem without modifying the array `nums` and use only constant extra space.
- Your solution should run in `O(n)` time complexity.

**Approach 1: Floyd's Tortoise and Hare (Cycle Detection)**
1. Treat the array as a linked list where the value at each index points to the next index.
2. Use two pointers, `slow` and `fast`:
   - Move `slow` one step at a time.
   - Move `fast` two steps at a time.
3. If there is a duplicate, the two pointers will eventually meet.
4. To find the duplicate, reset one pointer to the start of the array and move both pointers one step at a time until they meet again.

**Approach 2: Binary Search**
1. Use binary search on the range `[1, n]` to find the duplicate.
2. For each mid-point, count how many numbers in the array are less than or equal to `mid`.
3. If the count is greater than `mid`, the duplicate is in the lower half; otherwise, it is in the upper half.

**Example:**
```python
Input: nums = [3, 1, 3, 4, 2]
Output: 3
```

**Complexity:**
- Time Complexity: O(n) for Floyd's algorithm, O(n log n) for binary search.
- Space Complexity: O(1).

# Binary Tree 

## Day 46 - Invert Binary Tree

**Problem:**
Given the root of a binary tree, invert the tree, and return its root.
**Example:**

```python
Input:
   4
   / \
  2   7
 / \ / \
1  3 6  9

Output:
   4
   / \
  7   2
 / \ / \
9  6 3  1
```

**Approach:**
For every node, recuursively swap children node.
