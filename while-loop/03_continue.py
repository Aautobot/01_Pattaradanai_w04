#Prime Number
print(f"เลขจำนวนเฉพาะเลขบวก")
mixed = [-10,-8,-4,-2,0,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,91,97]
for num in mixed
    if num <= 0:
        continue
    
    prime = num ** 2
    print(f"{num}  {prime}")
    