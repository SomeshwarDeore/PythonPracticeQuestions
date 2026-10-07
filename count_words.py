text = input("Enter a sentence: ")

count = 0
in_word = False

for char in text:
    if char != ' ':
        if in_word == False:
            count += 1
            in_word = True
    else:
        in_word = False

print("Total words:", count)