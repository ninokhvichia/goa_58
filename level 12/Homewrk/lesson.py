"""while ციკლის გამოყენებით დაპრინტეთ 1-დან 50-მდე ყველა 4-ის ჯერადი რიცხვის კუბი"""

# num = 1
# while num <= 50:
#     if num % 4 == 0:  
#         print(f"{num}-ის კუბი არის {num**3}")  
#     num += 1  

""" შექმენით რიცხვების დიაპაზონი 1-დან 100-მდე, შეამოწმეთ თუ რიცხვი იყოფა 3-ზე დაბეჭდეთ
"Fizz" და გვერდზე მიუწერეთ რიცხვი. თუ რიცხვი იყოფა 5-ზე დაბეჭდეთ "Buzz" და გვერდზე
მიუწერეთ რიცხვი, ხოლო თუ იყოფა 3-ზეც და 5-ზეც დაბეჭდეთ "FizzBuzz" და გვერდზე 
მიუწერეთ რიცხვი """

# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print(f"FizzBuzz {num}")
#     elif num % 3 == 0:
#         print(f"Fizz {num}")  
#     elif num % 5 == 0:
#         print(f"Buzz {num}")  

"""შექმენით ორი ცვლადი, პირველში შეინახეთ 1-დან 20-ის ჩათვლით ყველა ლუწი რიცხვის ჯამი
მეორეში კი ყველა კენტის. აიყვანეთ ორივე მე-5 ხარისხში და დაპრინტეთ ის, რომელიც არის მეტი"""

# even_sum = 0
# odd_sum = 0

# for num in range(1, 21):
#     if num % 2 == 0:
#         even_sum += num  
#     else:
#         odd_sum += num   

# even_sum_5th_power = even_sum ** 5
# odd_sum_5th_power = odd_sum ** 5

# if even_sum_5th_power > odd_sum_5th_power:
#     print(f"{even_sum_5th_power} - ლუწი რიცხვების ჯამი მე-5 ხარისხში არის მეტი.")
# else:
#     print(f"{odd_sum_5th_power} - კენტის რიცხვების ჯამი მე-5 ხარისხში არის მეტი.")


"""მომხარებელს შემოატანინეთ რიცხვი და გაიგეთ არის თუ არა ის მარტივი, თუ მარტივია
 დაპრინტეთ "Number is prime", სხვა შემთხვევაში "Number is not prime"(მარტივია რიცხვი, 
 რომელიც იყოფა მარტო თავის თავზე და ერთზე)"""


# num = int(input("შეიტანეთ რიცხვი: "))

# if num <= 1: 
#     print("Number is not prime")
# else:
#     is_prime = True 

#     for i in range(2, num):
#         if num % i == 0: 
#             is_prime = False
#             break  

#     if is_prime:  
#         print("Number is prime")
#     else:
#         print("Number is not prime")

"""for ციკლით მომხარებელს შემოატანინეთ 5 ელემენტი სიაში და დაბეჭდეთ სია"""

# my_list = []

# for i in range(5):
#     element = input(f"შეიტანეთ {i+1}-ე ელემენტი: ")
#     my_list.append(element)  

# print("ჩამონათვალია:", my_list)














































































