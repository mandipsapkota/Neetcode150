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