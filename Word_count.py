# word count
user_input = input("Enter the sentence you want to count the word : \n ")
input_split = user_input.split()
word_count = 0 
for i in input_split:
    word_count += 1
print(f"the word count is :  {word_count}")