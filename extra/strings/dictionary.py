# Question: “You’re given a string of user votes for different colors, formatted like 'red,blue,red,green,blue,red'
# Input: 'red,blue,red,green,blue,red'
# Output: {'red': 3, 'blue': 2, 'green': 1}

def count_votes(input_string):
    if not input_string:
        return {}
    votes = input_string.split(', ')
    color_counts = {}
    for vote in votes:
        if vote in color_counts:
            color_counts[vote] += 1
        else:
            color_counts[vote] = 1
    return color_counts

# Test
print(count_votes('red, blue, red, green, red, blue, green, green, yellow'))  # {'c': 'cat', 'd': 'dog', 'b': 'bird'}



# Question: “Given a string of animal names and their lengths like 'cat:3,dog:3,bird:4', create a dictionary where keys are the lengths and values are lists of animal names with that length.”
# Input: 'cat:3,dog:3,bird:4'
# Output: {'3': ['cat', 'dog'], '4': ['bird']}

def animal_lengths(input_string):
    if not input_string:
        return {}
    animal_names = input_string.split(',')
    dictionary = {}
    for animal in animal_names:
        animal, length = animal.split(':')
        if length in dictionary:
            dictionary[length].append(animal)
        else:
            dictionary[length] = [animal]
    return dictionary


# Question: “You’re given a string of animal names and their first letters, formatted like 'cat:c,dog:d,bird:b'. Each pair is separated by a comma, and within each pair, the animal and its first letter are separated by a colon. Create a dictionary where the keys are the first letters, and the values are the animal names, but only keep the first animal for each letter.”
# Input: 'cat:c,dog:d,bird:b'
# Output: {'c': 'cat', 'd': 'dog', 'b': 'bird'}

def animal_map(input_string):
    if not input_string:
        return {}
    animals = input_string.split(',')
    maps = {}
    for animal in animals:
        animal_name, letter = animal.split(':')
        if letter not in maps:
            maps[letter] = animal_name
    return maps


# Question: “Given a string of words like 'cat,dog,cat', count the frequency of each word and return a dictionary where keys are words and values are their counts.”
# Input: 'cat,dog,cat'
# Output: {'cat': 2, 'dog': 1}

def count_words(input_string):
    if not input_string:
        return {}
    animals = input_string.split(',')
    counts = {}
    for animal in animals:
        if animal in counts:
            counts[animal] += 1
        else:
            counts[animal] = 1
    return counts


# Question: “You’re given a string, and your task is to swap cases—convert all lowercase letters to uppercase and vice versa. Non-letter characters should stay unchanged.”
# Input: 'Happy Birthday'
# Output: 'hAPPY bIRTHDAY'

def swap_case(s):
    if not s:
        return ''
    result = ''
    for letter in s:
        if letter.isupper():
            result += letter.lower()
        elif letter.islower():
            result += letter.upper()
        else:
            result += letter
    return result


# Task: You’re given a string of items and categories like 'apple:fruit,banana:fruit,carrot:veg,orange:fruit'. Create a dictionary where keys are categories, and values are lists of items, merging duplicates into the same list.
# Input: 'apple:fruit,banana:fruit,carrot:veg,orange:fruit'
# Output: {'fruit': ['apple', 'banana', 'orange'], 'veg': ['carrot']}

def merge_fruits(input):
    if not input:
        return {}
    fruits = input.split(',')
    dictionary = {}
    for fruit in fruits:
        item, category = fruit.split(':')
        if category in dictionary:
            dictionary[category].append(item)
        else:
            dictionary[category] = [item]
    return dictionary

result = print(merge_fruits('apple:fruit,banana:fruit,carrot:veg,orange:fruit'))
    

# Task: Given a string of names and IDs like 'john:123,bob:456,john:789', create a dictionary where keys are IDs and values are lists of names that map to that ID. If an ID repeats, include all names.
# Input: 'john:123,bob:456,john:789'
# Output: {'123': ['john'], '456': ['bob'], '789': ['john']}

def name_by_id(input_string):
    if not input_string:
        return {}
    employees = input_string.split(',')
    dictionary = {}
    for employee in employees:
        person, ID = employee.split(':')
        if ID in dictionary:
            dictionary[ID].append(person)  # Add to existing list
        else:
            dictionary[ID] = [person]     # Start new list
    return dictionary


# Task: Given a string like 'aabbccdd', count the frequency of each character, but only include characters that appear more than 2 times in the output dictionary.
# Input: 'aabbccdd'
# Output: {'a': 2, 'b': 2, 'c': 2, 'd': 2} → Filter to {}, since none exceed 2.
# Input: 'aaaabbbccd'
# Output: {'a': 4, 'b': 3} (only 'a' and 'b' > 2).
# Hint: Count first, then filter.


def count_frequency(input_string):
    if not input_string:
        return {}
    dictionary = {}
    for char in input_string:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    
    result = {char:count for char, count in dictionary.items() if count > 2 } 
            
    return dictionary
    
result = count_frequency('aabbbbccdd')
print(result)



def analyze_text(text):
    words = text.split()
    word_count = len(words)
    letter_count = {}
    for char in text.lower():
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    return {'words': word_count, 'letters': letter_count}
print(analyze_text('hello world'))
# {'words': 2, 'letters': {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}}


# Count the occurrences of each word in a paragraph
def count_words(string):
    if not string:
        return {}
    dictionary = {}
    input = string.split(' ')
    for char in input:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
            
    return dictionary
    
output = count_words('hello hi bye hello hi')
print(output)


# getting word count in a dictionary : 
def count(string):
    input = string.split(" ")
    word_count = {}
    for word in input:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


# find the most frequent word in a text

def count_words(sentence):
    words = sentence.split(" ")
    refined_words = {}
    for word in words:
        refined_words[word] = refined_words.get(word, 0) + 1
    highest_count = max(refined_words.values())
    frequent_words = [word for word, count in refined_words.items() if count == highest_count]
    return frequent_words, highest_count
    
    
output = count_words("hello hi hello hi hello hi bye")
print(output)


# find the most frequent word in a text

def categorize_entries(entries):
    positive_words = {"happy", "joy", "excited", "good", "great"}
    negative_words = {"sad", "angry", "bad", "terrible", "upset"}
    categories = {'positive' : [], 'negative' : [], 'neutral' : []}
    for entry in entries:
        words = set(entry.lower().split())
        if words & positive_words:
            categories['positive'].append(entry)
        elif words & negative_words:
            categories['negative'].append(entry)
    return categories
    
    
print(categorize_entries(["I am happy", "I am sad", "It was okay"]))
