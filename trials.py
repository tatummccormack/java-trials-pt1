"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
      # TODO: replace this line with your code
    for item in items:
        print(item)

def get_all_evens(nums):
      # TODO: replace this line with your code
    
    evenNums = []
    for num in nums: 
        if num % 2 == 0:
            evenNums.append(num)
    return evenNums

def get_odd_indices(items):
      # TODO: replace this line with your code
    result = []

    for index, item in enumerate(items):
        if index % 2 != 0:
            result.append(item)
    return result

    # return items[1::2]

def print_as_numbered_list(items):
      # TODO: replace this line with your code

    for i, item in enumerate(items, start=1):
        print(f"{i}, {item}")
        

def get_range(start, stop):
      # TODO: replace this line with your code
    nums = []

    num = start
    while num < stop:
        nums.append(num)
        num = num+1

    return nums

def censor_vowels(word):
      # TODO: replace this line with your code
    
    vowels = "aeiou"
    result = ""

    for letter in word: 
        if letter in vowels:
            result += '*'
        else: 
            result += letter
    return result

def snake_to_camel(string):
      # TODO: replace this line with your code
    camel_case = [];

    for word in string.split("_"):
        camel_case.append(word.upper())
    return "".join(camel_case)


def longest_word_length(words):
      # TODO: replace this line with your code

    longest = len(words[0])

    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest

def truncate(string):
      # TODO: replace this line with your code
    result = []

    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)
    return "".join(result)

def has_balanced_parens(string):
      # TODO: replace this line with your code
    parens = 0

    for char in string: 
        if char == '(':
            parens += 1 
        elif char == ')':
            parens -= 1
            if parens < 0:
                return False
    return parens == 0 

def compress(string):
      # TODO: replace this line with your code
    compressed = []

    current_char = ''
    char_count = 0

    for char in string:
        if char != current_char:
            compressed.append(current_char)
            if char_count > 1:
                compressed.append(str(char_count))
            current_char = char
            char_count = 0
        char_count += 1
    
    compressed.append(current_char)
    if char_count > 1:
        compressed.append(str(char_count))
    
    return "".join(compressed)
