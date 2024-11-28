""" შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში 
ყველაზე დიდი რიცხვი"""

# numbers = [4, 23, 1, 56, 89, 12, 34, 7]

# max_number = numbers[0]

# for number in numbers:
#     if number > max_number: 
#         max_number = number 

# print("The largest number is:", max_number)


""" შექმენით რიცხვების სია და დაბეჭდეს სიის თითოეული რიცხვის ფაქტორიალი"""

# import math 

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in numbers:
#     factorial = math.factorial(number)
#     print(f"The factorial of {number} is {factorial}")


"""შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე 
პატარა რიცხვი"""

# numbers = [34,10, 56, 23, 89, 12, 7, 3]

# min_number = numbers[0]

# for number in numbers:
#     if number < min_number: 
#         min_number = number 

# print("ყველაზე პატარა რიცხვია: ", min_number)


""" შექმენით რიცხვების სია სადაც გექნებათ დადებითი და უარყოფითი რიცხვები, შემდეგ 
შექმენით ახალი სია სადაც გექნებათ მხოლოდ უარყოფითი რიცხვები და დაბეჭდეთ
 ის(გამოიყენეთ while)."""

# numbers = [34, -12, 56, -3, 23, -9, -7, 0, 18, -5]

# negative_numbers = []

# index = 0

# while index < len(numbers):
#     if numbers[index] < 0:  
#         negative_numbers.append(numbers[index]) 
#     index += 1  

# print("უაყოფითი რიცხვებია: ", negative_numbers)


""" შექმენით რიცხვების სია და დაპრინტეთ სიის თითოეული ელემენტი უკუღმა
(გამოიყენეთ range() ფუქნცია ან შექმენით ცვლადი)"""

# numbers = [10, 20, 30, 40, 50]

# for i in range(len(numbers)-1, -1, -1):
#     print(numbers[i])

"""შექმენით სიმბოლოების სია, სადაც იქნება დუბლიკატები. შექმენით ახალი სია სადაც ყველა
 სიმბოლო მხოლოდ ერთხელ გვხვდება"""
"""
# symbols = ['a', 'b', 'c', 'a', 'd', 'b', 'e', 'f', 'c']
# unique_symbols = list(set(symbols))
# print("Unique symbols:", unique_symbols)

"""

# symbols = ['a', 'b', 'c', 'a', 'd', 'b', 'e', 'f', 'c']

# unique_symbols = []

# for symbol in symbols:
#     if symbol not in unique_symbols: 
#         unique_symbols.append(symbol)  

# print("Unique symbols:", unique_symbols)

"""შექმენით ცლვადი სადაც შეინახავთ string-ს, შემდეგ შექმენით ახალი ცვლადი სადაც 
შეინახავთ ამ სტრინგს შემოტრიალებულად და დაბეჭდეთ ის"""

# string = "hello"

# reversed_string = string[::-1]
# print("Reversed string:", reversed_string)

"""დაწერეთ პროგრამა, რომელიც მომხამრებელს შემოატანინებს რიცხვს და აბრუნებს სიას, 
სადაც იქნება გამდოცემული რიცხვის ყველა გამყოფი"""

# number = int(input("Please enter a number: "))

# divisors = []

# for i in range(1, number + 1):
#     if number % i == 0:
#         divisors.append(i)

# print(f"The divisors of {number} are:", divisors)


"""შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს და დაპრინტავს
რომელი საუკუნეა ის"""

# year = int(input("Please enter a year: "))
# century = (year - 1) // 100 + 1
# print(f"The year {year} is in the {century} century.")


































































