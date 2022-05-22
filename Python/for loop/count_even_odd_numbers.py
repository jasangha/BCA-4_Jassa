numbers=[1,2,3,4,5,6,7,8,9]
odd=0
even=0
for i in numbers:
    if i%27:
        odd+=1
    else:
        even+=1
print("Even numbers are= ",even)
print("Odd numbers are= ",odd)
