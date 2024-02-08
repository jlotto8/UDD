# review try/except
fn = 'sowpods.txt'
fh = open(fn)

def words_uu(file_path):
    with open(file_path, 'r') as fh:
        words = fh.read().splitlines()
        if not words:
            raise ValueError("Error: File is empty.")
        
        UU = []
        for word in words:
            if 'UU' in word:
                UU.append(word)
        return UU

if __name__ == '__main__':

    try:
        print(words_uu(fn))

    except FileNotFoundError:
        print(f"Error: File '{fn}' not found.")
    except IOError:
        print(f"Error: Could not read file '{fn}'.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    