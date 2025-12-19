from stats import get_num_words, get_count_characters, print_report

def main():
    print("-------- Word Count --------")
    print(get_num_words("books/frankenstein.txt"))
    print("----- Character Count -----")
    result = get_count_characters("books/frankenstein.txt")
    print_report(result)
    print("============ END ============")

main()
