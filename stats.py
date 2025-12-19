def get_num_words(file):
    with open(file) as f: #A with block can be used to open a file. The with block will automatically close the file when the block is exited, cleaning up resources
        file_content = f.read() #Used method to read the contents of a file into a string
        new_file = file_content.split() #Used to split the strings. Creating a list with all the words inside the string
        count_words = len(new_file) #See the lenght of the file, to know how many words does the text has
    return f"Found {count_words} total words"

def get_count_characters(file):
    dic = {}
    with open(file) as f:
        file_content = f.read()
        new_file = file_content.split()
        for i in range(0, len(new_file)): #Reading the list created by the split function, where each index of the list represents each word of the file
            new_word = new_file[i].lower() #Convert any character to lowercase. We don't want duplicates
            char = list(new_word) #Convert the word string in a list with their characters
            for j in range(0, len(char)): #Read the characters list
                if char[j] not in dic: #Verify if the character read is already on dictionary, if not we add and create it a counter
                    dic[char[j]] = 1
                elif char[j] in dic: #If the character was already read incremente the counter
                    dic[char[j]] += 1
        return dic

def sort_on(items): #Function used to sort the list of dictionaries
    return items["num"]

def print_report(dics):
    new_list = []
    for dic in dics:
        new_test_dic = {} #Solution: Create a new dictionary inside the loop. This ensures that every time the loop runs, i create a brand-new object in memory.
        new_test_dic["char"] = dic #Creation of the Key and value 
        new_test_dic["num"] = dics[dic]
        new_list.append(new_test_dic)

    new_list.sort(reverse = True, key=sort_on) #Sorting the list from greatest to the least by the count

    for i in range(0, len(new_list)):
        if new_list[i]["char"].isalpha() == False: #I don't want to print the no-alphabetic characters
            continue
        else:
            print(f"{new_list[i]["char"]}: {new_list[i]["num"]}")