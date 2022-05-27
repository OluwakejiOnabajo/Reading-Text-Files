# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here     
    text = open("./story.txt", "r")      
    return text.read()
    


def count_words():
    text = read_file_content("story.txt")
    
    words = text.split()
    dictionary = {}
    for word in words:
            dictionary[word] = dictionary.get(word, 0) + 1
    return dictionary


print("Text: ", read_file_content("story.txt"))
print("Dictionary: ", count_words())