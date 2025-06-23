# grade system
score = float(input("Enter your score : "))
'''
>90 A Very Good !!!
>80 B Good
>70 C Normal
>60 D Pass
<60 F Poor
'''
if score >= 90:
    grade = "A"
    comment = "Very Good !!!"
elif score >= 80:
    grade = "B"
    comment = "Good !!!"
elif score >= 70:
    grade = "C"
    comment = "Normal"
elif score >= 60:
    grade = "D"
    comment = "Pass"
else:
    grade = "F"
    comment = "Poor"

print(f"Score : {score}")
print(f"Grade : {grade}")
print(f"Comment : {comment}")