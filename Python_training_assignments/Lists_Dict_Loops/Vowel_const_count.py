str = input("Enter a string: ")

vowels = 0
const = 0

if str.isalpha() or " " in str:
    for ch in str:
        if ch in "AEIOUaeiou":
            vowels += 1
        elif ch == " ":
            pass
        else:
            const += 1
    print("Vowels = ", vowels)
    print("Consonants = ", const)
else:
    print("Invalid String")
