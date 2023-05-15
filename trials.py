"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums


def get_odd_indices(items):
    result = []

    for idx, item in enumerate(items):
        if idx % 2 != 0:
            result.append(item)

    return result


def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f'{i}. {item}')
        i += 1

def get_range(start, stop):
    nums = []
    for i in range(start,stop):
        nums.append(i)

    return nums
        


def censor_vowels(word):
    chars = []
    for letter in word:
        if letter in "aeiou":
            chars.append('*')
        else:
            chars.append(letter)
    
    return ''.join(chars)


def snake_to_camel(string):
    camel_case_list = []
    string_list = string.split('_')
    camel_case_list.append(string_list[0])
    for i, word in enumerate(string_list):
        if i > 0:
            word = word.title()
            camel_case_list.append(word)
    
    return "".join(camel_case_list)    

# print(snake_to_camel("snake_to_camel_case"))

def longest_word_length(words):
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

# print(longest_word_length(["cat", "house", "gorgonzola", "fishies"]))

def truncate(string):
    result = []
    for char in string:
        if (len(result) == 0) or (char != (result[len(result)-1])):
            result.append(char)

    return ''.join(result) 

# print(truncate('aaaabbbbcccca'))

def has_balanced_parens(string):
    parens = 0
    for char in string:
        if char == '(':
            parens +=1
        elif char == ')':
            parens -=1
    if parens != 0:
        return False
    else:
        return True
        


def compress(string):
    compressed = []
    curr_char = ''
    char_count = 0
    for char in string:
        if char != curr_char:
            compressed.append(curr_char)
            
            if char_count > 1:
                compressed.append(str(char_count))
                char_count = 0
        else:
            curr_char = char
            char_count += 1

    # compressed.append(curr_char)
    # if char_count > 1:
    #     compressed.append(str(char_count))

    return ''.join(compressed)

print(compress("aabbbccccddddd"))