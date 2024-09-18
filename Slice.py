#1. How do you slice the list my_list = [1, 2, 3, 4, 5, 6] to get the first three elements?
my_list = [1, 2, 3, 4, 5, 6]
first_three =[]
for i in range(3):
    first_three.append(my_list[i])
print(first_three)

#2. How do you slice the list my_list = [1, 2, 3, 4, 5, 6] to get the last two elements?
my_list = [1, 2, 3, 4, 5, 6]
last_two = []
for i in range(len(my_list)- 2, len(my_list)):
    last_two.append(my_list[i])
print(last_two)


#3. How do you slice the list my_list = [1, 2, 3, 4, 5, 6] to get every other element?
my_list = [1, 2, 3, 4, 5, 6]
random_element =[]
for i in range(0,len(my_list),2):
    random_element.append(my_list[i])
print(random_element)

#4. How do you slice the list my_list = [1, 2, 3, 4, 5, 6] to get the elements in reverse order?
my_list = [1, 2, 3, 4, 5, 6]
reversed_my_list =[]
for i in range(len(my_list)-1,-1,-1):
    reversed_my_list.append(my_list[i])
print(reversed_my_list)

#5. How do you slice the string my_string = "hello world" to get the first five characters?
my_string = "hello world"
first_five =''
for i in range(5):
    first_five += my_string[i]
print(first_five)


#6. How do you slice the tuple my_tuple = (1, 2, 3, 4, 5, 6) to get the middle three elements?
my_tuple = (1, 2, 3, 4, 5, 6)
middle_element =[]
for i in range(2,5): #doubt
    middle_element.append(my_tuple[i])
print(middle_element)

#7. How do you slice the list my_list = [1, 2, 3, 4, 5, 6] to get the elements from index 2 to 5?
my_list = [1, 2, 3, 4, 5, 6]
middle_element =[]
for i in range(2,5):
    middle_element.append(my_list[i])
print(middle_element)

#8. How do you slice the string my_string = "hello world" to get the characters from index 3 to 7?
my_string = "hello world"
my_character=[]
for i in range(3,8):    #doubt
    my_character.append(my_string[i])
print(my_character)

#9. How do you slice the list my_list = [1, 2, 3, 4, 5, 6] to get the elements from the end of the list to index 3?
my_list = [1, 2, 3, 4, 5, 6]
get_element = []
for i in range(5,3 ):
    get_element.append(my_character[i])
print(get_element)

#10. How do you slice the tuple my_tuple = (1, 2, 3, 4, 5, 6) to get the elements from index 2 to the end of the tuple?
my_tuple = (1, 2, 3, 4, 5, 6)
get_element = []
for i in range(2,len(my_tuple)): #doubt
    get_element.append(my_character[i])
print(get_element)


#Paragraph: "The quick brown fox jumps over the lazy dog."

#1. How do you slice the paragraph to get the first 10 characters?
str = The quick brown fox jumps over the lazy dog
print



#2. How do you slice the paragraph to get the last 10 characters?
#affan
#3. How do you slice the paragraph to get every other character?

#4. How do you slice the paragraph to get the characters in reverse order?

#5. How do you slice the paragraph to get the words "quick brown"?

#6. How do you slice the paragraph to get the words "lazy dog"?

#7. How do you slice the paragraph to get the characters from index 10 to 20?

#8. How do you slice the paragraph to get the characters from index 5 to 15?

#9. How do you slice the paragraph to get the characters from the end of the paragraph to index 20?

#10. How do you slice the paragraph to get the characters from index 15 to the end of the paragr