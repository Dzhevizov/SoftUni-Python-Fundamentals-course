def password_validator(some_string):
    is_valid = True
    if len(some_string) not in range(6, 10 + 1):
        print("Password must be between 6 and 10 characters")
        is_valid = False
    for char in some_string:
        if not char.isalpha() and not char.isdigit():
            print("Password must consist only of letters and digits")
            is_valid = False
            break
    count_digits = 0
    for char in some_string:
        if char.isdigit():
            count_digits += 1
    if count_digits < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


password = input()
password_validator(password)
