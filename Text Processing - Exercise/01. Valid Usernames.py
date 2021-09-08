usernames = input().split(", ")

for username in usernames:
    if len(username) in range(3, 17):
        is_valid = True
        for ch in username:
            if not ch.isalpha() and not ch.isdigit() and not ch == "-" and not ch == "_":
                is_valid = False
                break
        if is_valid:
            print(username)
