"""შექმენით სია სადაც, შეიტანთ მინიმუმ 10 რიცხვს, გადაუარეთ for ციკლის დახმარებით და
 დაბეჭდეთ თითოეული რიცხვი კენტია თუ ლუწი."""

# numbers = [12, 7, 5, 8, 3, 20, 15, 18, 10, 25]

# for number in numbers:
#     if number % 2 == 0:  
#         print(f"{number} არის ლუწი")
#     else:  
#         print(f"{number} არის კენტი")

""" შექმენით სახელების სია სადაც გექნებათ მინიმუმ 10 სახელი, დაბეჭდეთ ამ სიიდან მხოლოდ
 ის სახელები რომლების ინდექსებიც არის ლუწი"""


# names = ["ანა", "გიორგი", "მარიამი", "დათო", "ეკა", "ნინო", "მამუკა", "ლიკა", "გია", "ირაკლი"]

# for i in range(len(names)):
#     if i % 2 == 0: 
#         print(names[i])

"""შექმენით სია სადაც გექნებათ 10 რიცხვი, თქვენი დავალებაა გაიგოთ ამ სიაში ყველა ლუწი და
 კენტი რიცხვიოს ჯამი და დაბეჭდოთ"""

# numbers = [12, 7, 5, 8, 3, 20, 15, 18, 10, 25]

# even_sum = 0
# odd_sum = 0

# for number in numbers:
#     if number % 2 == 0:  
#         even_sum += number
#     else:  
#         odd_sum += number

# print(f"ლუწი რიცხვების ჯამი: {even_sum}")
# print(f"კენტი რიცხვების ჯამი: {odd_sum}")

""" შექმენით სია სადაც გექნებათ 10 რიცვი, შემდეგ შექმენით ახალი სია, სადაც ჩაამატებთ 
პირველი სიიდან ყველა ლუწ რიცხვს და გაიგებთ მათ საშუალო არითმეტიკულს.
(ახალ სიაზე გამოიყენეთ len() ფუნქცია)"""

# numbers = [12, 7, 5, 8, 3, 20, 15, 18, 10, 25]

# even_numbers = []

# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)

# if len(even_numbers) > 0:  
#     average = sum(even_numbers) / len(even_numbers)
#     print(f"ლუწი რიცხვები: {even_numbers}")
#     print(f"მათ საშუალო არითმეტიკული: {average}")
# else:
#     print("ლუწი რიცხვები არ არსებობს.")

"""შექმენით სია სადაც ჩაამატებთ 1-დან 100-მდე ყველა ლუწ რიცხვს. საბოლოოდ დაპრინტეთ 
ეს სია(გამოიყენეთ for loop)"""

# even_numbers = []

# for number in range(1, 101):
#     if number % 2 == 0: 
#         even_numbers.append(number)

# print(even_numbers)

""" შექმენით სია სადაც ჩაამატებთ ყველა რიცხვს 1-დან 50-ის ჩათვლით. შემდეგ გადაუარეთ
for loop-ით და ამ სიიდან წაშალეთ ყველა კენტი რიცხვი. საბოლოოდ დაპრინტეთ მიღებული სია"""

"""# numbers = [number for number in range(1, 51) if number % 2 == 0]
# print(numbers)"""

# numbers = list(range(1, 51))

# even_numbers = []

# for number in numbers:
#     if number % 2 == 0:  
#         even_numbers.append(number)
        
# print(even_numbers)

"""შექმენით ხილების სია სადაც გექნებათ მინიმუმ 10 ელემენტი, while loop-ის გამოყენებით
 წაშალეთ სიის ბოლო ელემენტი იქამდე სანამ სიაში არ დარჩება ორი ელემენტი. 
 ყოველი ელემენტის წაშლისას დაბეჭდეთ ხილების სია"""

# fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# while len(fruits) > 2:
#     fruits.pop()  
#     print(fruits)  

"""შექმენით პროგრამა, რომელიც დაითვლის თუ რამდენჯერ შედის სიაში რიცხვი
 1 numbers = [1,2,0,1,32,1,30,1,1,21,1,1,1] (ამისათვის გადაუარეთ სიას for loop-ით)"""


# numbers = [1, 2, 0, 1, 32, 1, 30, 1, 1, 21, 1, 1, 1]

# count = 0

# for number in numbers:
#     if number == 1:  
#         count += 1 

# print(f"რიცხვი 1 გამოჩნდა {count} ჯერ.")


""" შექმენით ორი ცარიელი სია, for loop-ის გამოყენებით მომხარებელს 5-ჯერ შემოატანინეთ
 ნებისმიერი სიტყვა. თუ შემოტანილი სიტყვის სიგრძე არ აღემატება 5-ს ჩაამატეთ პირველ სიაში,
   სხვა შემთხვევაში მეორეში. საბოლოოდ დაბეჭდეთ ორივე სია"""

# short_words = []  
# long_words = [] 

# for _ in range(5):
#     word = input("შეიტანეთ სიტყვა: ")  
#     if len(word) <= 5:  
#         short_words.append(word)  
#     else:
#         long_words.append(word)  

# print("მოკლე სიტყვები:", short_words)
# print("გრძელი სიტყვები:", long_words)















































































