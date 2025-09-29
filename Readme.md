# Introduction
This document contains solutions for the Neetcode 150 problems. I plan to cover all 150 problems in the next 150 days, tackling one problem per day.

# Day 1 - Contains Duplicate
Given an integer array `nums`, return `true` if any value appears more than once, otherwise return `false`.

# Day 2 - Anagrams
Given two strings "stringa" and "stringb", return `true` if they are anagrams of each other, otherwise return `false`.

Anagram : An anagram is a string that has the exact same characters as another string, but in a different order.

Approaches used:
* Hashmap : adding in hashmap and comparing characterwise match of number of appearance
* Sorting : sorting and then comparing equality

# Day 3 - Two Sum
Given an array and a target, find the indices of two elements whose sum equals the target.

Approaches used:
* Brute force
* One-pass approach : subtracting element from target and finding the resultant in hashmap.

# Day 4 -  Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Day5 - Top k frequent
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

# Day 6 - Encode decode problem
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.