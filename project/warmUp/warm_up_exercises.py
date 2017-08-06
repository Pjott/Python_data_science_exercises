# 1
# myNumber = 7**4
# print(myNumber)



# 2 Split this string into a list.
# s = "Hi there Sam!"
# sList = s.split()
# print(sList)



# 3 Use .format() to print string
# planet = "Earth"
# diameter = 12742
# print('The diameter of {} is {} kilometers.'.format(planet,diameter))



# 4 get 'hello'
# lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
# print(lst[3][1][2])



# 5 Given this nested dictionary grab the word "hello".
# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
# print(d['k1'][3]['tricky'][3]['target'][3])



# 6 Create a function that grabs the email website domain from a string in the form:
# user@domain.com
# So for example, passing "user@domain.com" would return: domain.com
# def domainGet(userEmail):
#     emaliList = userEmail.split('@')
#     return print(emaliList[1])
#
# domainGet('user@domain.com')



# 7 Create a basic function that returns True if the word 'dog' is contained in the input string.
# Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.

# def findDog(userFindDogInput):
#     findDogList = userFindDogInput.split()
#     return  print('dog' in findDogList)
#
# findDog('Is there a dog here?')



#8 Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases.
# def countDog(userInput):
#     dog = 'dog'
#     num = 0
#     inputList = userInput.split()
#     for string in inputList:
#         if string == dog:
#             num = num + 1
#     return print(num)
#
# countDog('This dog runs faster than the other dog dude!')



# 9 Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'.
# For example:
# seq = ['soup','dog','salad','cat','great']
# should be filtered down to:
# ['soup','salad']

# seq = ['soup','dog','salad','cat','great']
# print(list(filter(lambda item: item.startswith('s'),seq)))



#10 You are driving a little too fast, and a police officer stops you.
# Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".
# If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive,
# the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket".
# Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday,
# your speed can be 5 higher in all cases.

# solution is not perfect... but good enough for now...
def caught_speeding(speed, is_birthday):
    if ((speed <= 60)  and (is_birthday == False)):
        print('No Ticket')
    elif ((61 < speed <= 80 )and (is_birthday == False)):
        print('Small Ticket')
    elif ((speed >= 81) and (is_birthday == False)):
        print('Big Ticket')
    elif ((speed <=65) and (is_birthday == True)):
        print('No Ticket')
    elif ((66 < speed <= 85) and (is_birthday == True)):
        print('Small Ticket')
    elif ((speed >= 86) and (is_birthday == True)):
        print('Big Ticket')

caught_speeding(82, True)


