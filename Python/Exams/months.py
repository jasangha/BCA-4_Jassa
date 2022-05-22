months = {'Jan':31, 'Feb':28, 'Mar':31, 
          'Apr':30, 'May':31, 'Jun':30,
          'Jul':31, 'Aug':31, 'Sep':30,
          'Oct':31, 'Nov':30, 'Dec.':31}
    
print("Months: ",end="")

for i in months.keys():
    if i != 'Dec.':
        print(i,end=", ")
    else:
        print(i)

a = input("Month:")
if a == 'Jan':
    print("Days: ",list(months.values())[0])
elif a == 'Feb':
    print("Days: ",list(months.values())[1])
