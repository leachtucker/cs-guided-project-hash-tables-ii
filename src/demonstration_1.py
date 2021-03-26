"""
You are given a non-empty list of words.

Write a function that returns the *k* most frequent elements.

The list that you return should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical
order should come first.

Example 1:

```plaintext
Input:
words = ["lambda", "school", "rules", "lambda", "school", "rocks"]
k = 2

Output:
["lambda", "school"]

Explanation:
"lambda" and "school" are the two most frequent words.
```

Example 2:

```plaintext
Input:
words = ["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"]
k = 4

Output:
["the", "is", "cloudy", "sky"]

Explanation:
"the", "is", "cloudy", and "sky" are the four most frequent words. The words
are sorted from highest frequency to lowest.
```

Notes:

- `k` is always valid: `1 <= k <= number of unique elements.
- words in the input list only contain lowercase letters.
```
"""
def top_k_frequent(words, k):
    """
    Input:
    words -> List[str]
    k -> int

    Output:
    List[str]
    """
    # Your code here
    frequency_dict = {}

    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    frequency_array = []
    prevWord = None
    for key, value in sorted(frequency_dict.items(), key=lambda word: word[1], reverse=True):
        if prevWord is not None and prevWord[1] == value and prevWord[0] > key:
            # Check alphabetical order
            # if the previous word's alphabetical order is greater, let's place it after

            # Pop the previous word off the array
            item = frequency_array.pop(len(frequency_array)-1)

            # Append the word we are currently on from the dict
            frequency_array.append([key, value])

            # Append the previous word back on
            frequency_array.append(prevWord)
        else:
            frequency_array.append([key, value])

        prevWord = [key, value]
        # Break from the for-loop if we've appended the first k-items from the sorted items arr^
        if len(frequency_array) >  k:
            break

    return frequency_array[0:k]

words = ["lambda", "school", "rules", "lambda", "school", "rocks"]
k = 2
print(top_k_frequent(words, k))

words = ["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"]
k = 4
print(top_k_frequent(words, k))

words = ["the", "the", "the", "all", "all", "all"]
k = 2
print(top_k_frequent(words, k))
