'''
Compile a dictionary with unique words as keys and lists of line
numbers where the term appears. Count the instances of each word
in the provided text file.The path to the text file is indicated
by the parameter t (str).Returns: dict: A dictionary with lists
of line numbers as values and words as keys.


'''

def wordCount(t):
    w_dict = {}
    with open(t, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            words = line.split()
            for word in words:
                word = word.strip('.,!?;:').lower()
                if word in w_dict:
                    w_dict[word].append(line_num)
                else:
                    w_dict[word] = [line_num]
    return w_dict

print(wordCount('t.txt'))
