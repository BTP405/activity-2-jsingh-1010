""" 
Count the times a word appears in a text file and provide a
dictionary that associates each word with a list of line numbers.
Args: t (str): The name of the file to be processed.Returns: dict: A 
dictionary with lists of line numbers for values and words for keys.

"""
def wordCount(t):
    w_dict = {}
    with open(t, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            words = line.split()
            for word in words:
# To ensure uniformity, remove punctuation and convert to lowercase.
                word = word.strip('.,!?;:').lower()
                if word in w_dict:
                    w_dict[word].append(line_num)
                else:
                    w_dict[word] = [line_num]
    return w_dict

print(wordCount('t.txt'))
