#write a python function to remove a given word from a list and strip it at the same time

            
            
def rem(l, word):
    n = []
    for item in l:
        if item != word:  # Skip items that exactly match the word
            n.append(item.replace(word, ""))  # Remove occurrences of the word within the item
    return n

list_items = ["harry", "sayan"]
print(rem(list_items, "a"))

