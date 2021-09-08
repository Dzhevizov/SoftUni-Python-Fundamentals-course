tickets = [x.strip() for x in input().split(", ") if not x.isspace()]

at_string = "@@@@@@"
hash_string = "######"
dollar_string = "$$$$$$"
circumflex_string = "^^^^^^"


for ticket in tickets:
    if len(ticket) == 20:

        left_side = ticket[:10]
        right_side = ticket[10:]

        matched_symbol = ""
        left_win_length = 0
        right_win_length = 0

        if at_string in left_side and at_string in right_side:
            matched_symbol = "@"
            left_win_length = left_side.count("@")
            right_win_length = right_side.count("@")
        elif hash_string in left_side and hash_string in right_side:
            matched_symbol = "#"
            left_win_length = left_side.count("#")
            right_win_length = right_side.count("#")
        elif dollar_string in left_side and dollar_string in right_side:
            matched_symbol = "$"
            left_win_length = left_side.count("$")
            right_win_length = right_side.count("$")
        elif circumflex_string in left_side and circumflex_string in right_side:
            matched_symbol = "^"
            left_win_length = left_side.count("^")
            right_win_length = right_side.count("^")

        min_length = min(left_win_length, right_win_length)

        if min_length == 10:
            print(f'ticket "{ticket}" - {min_length}{matched_symbol} Jackpot!')
        elif min_length >= 6:
            print(f'ticket "{ticket}" - {min_length}{matched_symbol}')
        else:
            print(f'ticket "{ticket}" - no match')

    else:
        print("invalid ticket")
