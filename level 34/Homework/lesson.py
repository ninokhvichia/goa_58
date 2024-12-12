""" შექმენით manual_replace ფუნქცია, რომელიც იქნება .replace() ფუნქციის კლონი. ამ ფუნქციამ სთრინგში არსებული 
sapce-ები უნდა შეცვალოს ტირეებად.
არ გამოიყენოთ ჩაშენებული ფუნქციები და კომენტარებით ახსენით მე-4 დავალება"""

# def manual_replace(string):
#     result = []
#     for char in string:
#         if char == ' ':  
#             result.append('-') 
#         else:
#             result.append(char)  
#     return ''.join(result)

# print(manual_replace("hello world")) 
# print(manual_replace("a b g d"))  
# print(manual_replace("nini nini nini")) 


"""შექმენით ფუნქცია, რომელიც არგუმენტად მიიღებს string-ს. ამ ფუნქციამ უნდა გაიგოს გადმოცემულ string-ში თითოეული
 სიმბოლოს რაოდენობა და ჩაამატოს ახალ სიაში(ერთი სიმბოლის რაოდენობა მხოლოდ ერთხელ უნდა ჩაამატოთ. მგალითად თუ
   string-ში 5 "a" გვხვდება, რიცხვი 5 მასივში მხოლოდ ერთხელ უნდა ჩავამატოთ, მაგრამ სხვა სიმბოლოც თუ გვხვდება 
   იგივე რაოდენობით, მას ვამატებთ ჩვეულებრივ). საბოლოდ დაასორტირეთ მიღებული სია ზრდადობით და დააბრუნეთ """

# def argument_string(string):
#     listn=[]
#     for i in string:
#             count=string.count(i)
#             if count not in listn:
#                   listn.append(count)
#     return list(listn)
# string="niniko"


"""შექმენთ ფუნქცია, რომელიც არგუმენტად იღებს სიმბოლოების სიას. დაასორტირეთ ეს სია ანბანის მიხედვით,
 გადააქციეთ string-ად და დააბრუნეთ"""

# def argument_list_of_symbols(char_list):
#     char_list.sort()
#     result = ''.join(char_list)
    
#     return result

""" შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვების სიას და აბრუნებს მას კლებადობის მიხედვით დასორტირებულს"""
def list_of_numbers(numbers):
     numbers.sort()
     numbers.reverse()
     return numbers

print(list_of_numbers([1,2,3,4,5,6,7,8,9]))



