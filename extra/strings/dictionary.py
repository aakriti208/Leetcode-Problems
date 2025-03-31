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