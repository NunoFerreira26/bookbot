from stats import get_num_words, get_count_characters, print_report
import sys

def main():
    if len(sys.argv) != 2: #A list of strings representing the arguments passed to the script. 
        print("Usage: python3 main.py <path_to_book>") #By writing this command on the terminal(<path_to_book> = books/text_of_user_choosing)
        sys.exit(1) #Exits the script with a status code of 1. Used for validation of solution
    else:
        print("-------- Word Count --------")
        print(get_num_words(sys.argv[1])) #We call the second entry in sys.argv, after the terminal command
        print("----- Character Count -----")
        result = get_count_characters(sys.argv[1])
        print_report(result)
        print("============ END ============")

main()

#Removing hard coded book paths. Example of Hard coded: books/frankenstein.text