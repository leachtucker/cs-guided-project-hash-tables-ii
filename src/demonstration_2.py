"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

```plaintext
Input:
"free"

Output:
"eefr"

Explanation:
'e' appears twice while 'f' and 'r' appear once.
So 'e' must appear before 'f' and 'r'. Therefore, "eerf" is also a valid answer.
```

Example 2:

```plaintext
Input:
"dddbbb"

Output:
"dddbbb"

Explanation:
Both 'd' and 'b' appear three times, so "bbbddd" is also a valid answer.
Note that "dbdbdb" is incorrect, as the same characters must be together.
```

Example 3:

```plaintext
Input:
"Bbcc"

Output:
"ccBb"

Explanation:
"ccbB" is also a valid answer, but "Bbcc" is incorrect.
Note that 'B' and 'b' are treated as two different characters.
```
"""
def frequency_sort(s: str) -> str:
    """
    Inputs:
    s -> str

    Output:
    str
    """
    # Your code here
    frequency_dict = {}

    for letter in s:
        if letter in frequency_dict:
            frequency_dict[letter] += 1
        else:
            frequency_dict[letter] = 1

    frequency_arr = []

    for key, item in frequency_dict.items():
        # Using a tuple here since it will result in faster runtimes than a two-element array/list
        frequency_arr.append((key, item))

    frequency_arr = sorted(frequency_arr, key=lambda letter: letter[1], reverse=True)

    outStr = ""

    for letter_tuple in frequency_arr:
        for i in range(letter_tuple[1]):
            outStr += letter_tuple[0]

    return outStr

print(frequency_sort('free'))
print(frequency_sort('dddbbb'))
print(frequency_sort('Bbcc'))