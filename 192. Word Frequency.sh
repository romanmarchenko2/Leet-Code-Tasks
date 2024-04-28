# Link:
# https://leetcode.com/problems/word-frequency/


# Code: 
# Read from the file words.txt and output the word frequency list to stdout.
tr ' ' '\n' < words.txt | grep -E '^[a-z]' | sort | uniq -c | sort -nr | awk '{print $2, $1}'


# Explanation:
# The tr command is a UNIX command-line utility for translating or deleting characters. It supports a range of 
# transformations including uppercase to lowercase, squeezing repeating characters, deleting specific characters, and 
# basic find and replace. It can be used with UNIX pipes to support more complex translation

# tr -s: truncate the string with target string, but only remaining one instance (e.g. multiple whitespaces)
# sort: To make the same string successive so that uniq could count the same string fully and correctly.
# uniq -c: uniq is used to filter out the repeated lines which are successive, -c means counting
# sort -r: -r means sorting in descending order
# awk '{ print $2, $1 }': To format the output.
