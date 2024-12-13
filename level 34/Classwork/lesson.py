""" შექმენით ცვლადი, სადაც შეინახავთ string-ს. დაბეჭდეთ მისი თითოეული სიმბოლო და გვერდით მიუწერეთ რიგით მერამდენეა ის.
# მგალითად: "Hello" >>> "H - 1", "e - 2"..."""

string = "Hello"
for i in range(len(string)):
    print(string[i], "-", i + 1)


"""შექმენით manual_join ფუნქცია, რომელსაც გადაეცემა სთინგების სია და ერთი სთრინგი. ამ ფუნქციამ უნდა შეართოს ეს 
 სია და თითოეულ ელემენტს შორის ჩასვას გადმოცემული სთრინგი
არ გამოიყენოთ .join() ფუნქცია"""


def manual_join(items):
    result = ""
    for i in range(len(items)):
        result += items[i]
        if i < len(items) - 1:
            result += " "
    return result
print(manual_join(["hi", "world", "list"]))

""" შექმენით manual_count ფუნქცია, რომელსაც გადაეცემა სთრინგი ნა სია და ელემენტი რომლის რაოდენობაც უნდა გაიგოთ. 
დააბრუნეთ მიღებული შედეგი."""

def manuel_count (listn,symbol):
    count=0
    for i in listn:
        if symbol == i:
            count += i
    return count

"""შექმენით manual_replace ფუნქცია, რომელიც იქნება .replace() ფუნქციის კლონი. ამ ფუნქციამ სთრინგში არსებული sapce-ები უნდა შეცვალოს ტირეებად."""
def custom_replace(string, old_string, new_string):
    result = ""
    i = 0
    while i < len(string):
        if string[i:i+len(old_string)] == old_string:
            result += new_string
            i += len(old_string)
        else:
            result += string[i]
            i += 1
    return result
print(custom_replace("hi ", "lol", "listt"))