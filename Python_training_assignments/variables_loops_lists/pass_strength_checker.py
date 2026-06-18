print("Password strength checker")
password = input("Enter password  ")
count =0
if len(password)>=8:
    count+=1
for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True

if len(password) >= 8:
    count += 1

if has_upper:
    count += 1

if has_lower:
    count += 1

if has_digit:
    count += 1

if has_special:
    count += 1

if count >= 5:
    print("Strong")
elif count >= 3:
    print("Medium")
else:
    print("Weak")