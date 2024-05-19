#1
print("Practice 1")

dept = ['工工系', '運管系', '管科系', '資財系', '資管所', '科管所', '經管所', 'GMBA', 'EMBA']

for i, item in enumerate(dept, start=1):
    if '系' in item:
        print(f"{i} : {item}(所)")
    elif 'MBA' in item:
        print(f"{i} : {item}學程")
    else:
        print(f"{i} : {item}")
        
        
 #2
print("Practice 2")

user_input = input("Enter a string: ")
result = ''
for char in user_input:
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char.upper()
    else:
        result += char

print("Result:", result)


#3
print("Practice 3")

with open('test.txt', 'w') as file:
    for _ in range(5):
        user_input = input("Enter a string: ")
        file.write(user_input + '\n')

print("Data written to 'test.txt' successfully.")
       

