force_book = {}

force_info = input()

while not force_info == "Lumpawaroo":

    if "|" in force_info:
        force_side, force_user = force_info.split(" | ")

        if force_side not in force_book:
            force_book[force_side] = []

        is_found = False

        for i in force_book:
            if force_user in force_book[i]:
                is_found = True
                break

        if not is_found:
            force_book[force_side].append(force_user)

    elif "->" in force_info:
        force_user, force_side = force_info.split(" -> ")

        if force_side not in force_book:
            force_book[force_side] = []

        if force_user in force_book[force_side]:
            continue
        else:
            for i in force_book:
                if force_user in force_book[i]:
                    force_book[i].remove(force_user)

            force_book[force_side].append(force_user)

            print(f"{force_user} joins the {force_side} side!")

    force_info = input()

for force_side, force_list in sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0])):

    if len(force_list) > 0:
        print(f"Side: {force_side}, Members: {len(force_list)}")

        for force_user in sorted(force_list):
            print(f"! {force_user}")
