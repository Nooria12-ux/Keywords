word = input("Enter  word: ")

for i in word:
    
    if i == 'A' or i == "a":
        print("A is found")
        break
    else:
        print(f"A IS NOT FOUND AT {i}")