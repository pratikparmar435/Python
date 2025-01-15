# # Two sum
# def Two_sum(arr,target):
#     store_number = {}
#     for i in range(len(arr)):
#         needed = target - arr[i]
#         if needed in store_number:
#             print("done",store_number[needed],i)
#             return [store_number[needed],i] 
    
#         store_number[arr[i]] = i
# my_arr = [2,7,11,5]
# tar = 9
# print(Two_sum(my_arr,tar))

#check palindrome string 
# my_str = input("Enter a sting to check it is palindrome or not:")
# reversed_str = my_str[::-1]
# isPalindrome = False
# if my_str == reversed_str:
#     isPalindrome = True
# if isPalindrome:
#     print("This string is palindrome")
# else: 
#     print("This string is not palindrome")

#or

#check the string is palindrome or not without using any built-in function 
# def chk_palindrome(input_str):
#     input_str = str(input_str)
#     input_str = input_str.lower()
#     reversed_string = ""
#     for i in range(len(input_str)-1,-1,-1):
#         reversed_string += input_str[i]
#     if input_str == reversed_string:
#         return True
#     else:
#         return False
# str1 = "Nitin"
# print(chk_palindrome(str1))

#write a function to find a largest number from list
# def find_larg(list):
#     largest_num = 0
#     for i in range(len(my_list)):
#         if list[i] > largest_num:
#             largest_num = list[i]
#     print(f"The largest number in you list is: {largest_num}")
# my_list = [1,2,4,5,7,44,5,6,3,55,99,4,5,7,0]
# find_larg(my_list)

#write a program to find sum of array elements 
# def find_sum(list):
#     sum = 0
#     for i in range(len(list)):
#         sum += list[i]
#     return sum
# my_list = [1,2,3,4]
# print(find_sum(my_list))

#write a program to count vowels and consonants from string 
# def cnt_ele(input_str):
#     count_vowel = 0
#     count_consonants = 0
#     input_str = input_str.lower().replace(" ","")
#     for i in input_str:
#         if i.isalpha():#checks if character is alphabet or special character
#             # if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#             #or
#             if i in "aeiou":
#                 count_vowel += 1
#             else:
#                 count_consonants += 1
            
#     print("Vowels =",count_vowel,",Consonants =",count_consonants)
# my_str = "Parmar Pratik"
# cnt_ele(my_str)

#write a program to remove duplicate characters from string and print unique string
# def unique_str(input_str):
    # unique_str = ""
    # for i in input_str:
    #     if i not in unique_str:
    #         unique_str += i
    # print("Unique string =",unique_str)
    #or
    # unique_str = set(input_str)
    # print(unique_str)
# str1 = "pratikik"
# unique_str(str1)

#write a program to find most frequent character from string without using any built in function
# def most_Frequent_char(input_string):
#     char_count = {}
#     for char in input_string:
#         if char in char_count:
#             char_count[char] += 1
#         else: 
#             char_count[char] = 1
#     max_value = max(char_count, key=char_count.get)
#     print("Most frequent character is =",max_value,"with the count =",char_count[max_value])
# str1 = "parmar pratik"
# most_Frequent_char(str1)

#write a program to count words from a sentence
# def countWord(input_string):
#     storeWord = ""
#     listOfWords = []
#     for char in input_string:
#         if char == " ":
#             if storeWord:
#                 listOfWords.append(storeWord)
#                 storeWord = ""
#         else: 
#             storeWord += char
#     if storeWord:
#         listOfWords.append(storeWord)
#     print(f"In this sentence their is {len(listOfWords)} words")
# myStr = "i love python programming"
# countWord(myStr)

#write a function to replace all the occurrence of character with new char without using built in function
# def replaceChar(input_string,old_char,new_char):
#     input_string = str(input_string)
#     old_char = str(old_char)
#     new_char = str(new_char)
#     input_string = input_string.lower()
#     uniqueString = ""
#     for char in input_string:
#         if char == old_char:
#             char = new_char
#             uniqueString += char
#         else:
#             uniqueString += char
#     return f"New string is = '{uniqueString}'"
# myStr = "I love python programming"
# print(replaceChar(myStr,'p','k'))

#write a function to capitalize a each word from string sentence 
# def capWord(input_string):
#     storeWord = ""
#     listOfWords = []
#     for char in input_string:
#         if char == " ":
#             if storeWord:
#                 storeWord = storeWord.capitalize()
#                 listOfWords.append(storeWord)
#                 storeWord = ""
#         else:
#             storeWord += char
#     if storeWord:
#         listOfWords.append(storeWord.capitalize())
#     capitalizeStr = " ".join(listOfWords)
#     print("Capitalized string =",capitalizeStr)
# myStr = "i like python programming"
# capWord(myStr)

#write a function to find unique characters from string
# def findUnique(input_string):
#     storeChar = {}
#     uniqueChar = []
#     for char in input_string:
#         if char == " ":
#             char = ""
#         else:
#             if char in storeChar:
#                 storeChar[char] += 1
#             else:
#                 storeChar[char] = 1
#     for i in storeChar:
#         if storeChar[i] == 1:
#             uniqueChar.append(i)
#     print("The list of unique character is =",uniqueChar)
# myStr = "Hello world"
# findUnique(myStr)

#delete characters to make fancy string
# def remove_consecutive_chars(s):
#     stack = []  # This stack will store characters and their counts.

#     for char in s:
#         # Check if the stack is not empty and if the last character in the stack matches the current character
#         if stack and stack[-1][0] == char:
#             stack[-1][1] += 1  # Increase the count of the last character in the stack
#             # if stack[-1][1] == 3:  # If there are 3 in a row
#                 # stack.pop()  # Remove the character from the stack
#         else:
#             # Add a new character with count 1 if it doesn't match the last character
#             stack.append([char, 1])
#     print(stack)
# string = "aaabaaa"
# remove_consecutive_chars(string)
