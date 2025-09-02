def count_words_in_file(filename):

    # Handling Errors
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        words = content.split()

        word_count = len(words)
        return word_count
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")
        return None
    
    except IsADirectoryError:
        print(f"Error: Unable to decode the file '{filename}'. It may not be a text file.")
        return None
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
def main():

    print("--- WORD COUNTER ---")
    print ("This programme can count numbers of text in your text file. \n")

    # Get filepath from user
    filename = input("Enter the path to the text file: ").strip()

    if not filename:
        print("Error: Enter a file name.")
        return
    
    # Count words
    word_count = count_words_in_file(filename)