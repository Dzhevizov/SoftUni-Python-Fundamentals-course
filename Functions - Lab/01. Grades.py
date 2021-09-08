def convert_grade_in_words(grade):
    if 2.00 <= grade < 3.00:
        return "Fail"
    elif 3.00 <= grade < 3.50:
        return "Poor"
    elif 3.50 <= grade < 4.50:
        return "Good"
    elif 4.50 <= grade < 5.50:
        return "Very Good"
    elif 5.50 <= grade <= 6.00:
        return "Excellent"


input_grade = float(input())
print(convert_grade_in_words(input_grade))
