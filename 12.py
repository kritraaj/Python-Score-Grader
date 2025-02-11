score = float(input("Enter the score: "))

if 90 <= score <= 100:
    print("Grade A")
elif 75 <= score < 90:
    print("Grade B")
elif 60 <= score < 75:
    print("Grade C")
elif 50 <= score < 60:
    print("Grade D")
elif 33 <= score < 50:
    print("Grade E")
elif 0 <= score < 33:
    print("Grade F")
else:
    print("Invalid Marks")
