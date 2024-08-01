# Write a function that takes a string prefix as the first argument, a string suffix as the second argument, and an integer length as the third argument. It should return an array of all of the words that start with that prefix, end with that suffix, and are that length.

def find_words(prefix,suffix,length):

    file_name = '../../Wordplay/sowpods.txt'
    file_handle = open(file_name)

    results = []

    results = [word.strip() for word in file_handle if word.startswith(prefix) and word.strip().endswith(suffix) 
    and len(word.strip())== length]

    
   
    return results

print(find_words('IN','ER', 10))

