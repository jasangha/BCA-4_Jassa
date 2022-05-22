stu = {
    'name': 'Jassa',
    'class': 'BCA',
    'Roll_no': 3252,
    'subject': 'python'
}
print(stu.keys())
print(stu.values())
print(len(stu))
stu['marks'] = 100
print(stu)
stu['class'] = 'btech'
print(stu)
a = stu.copy()
stu.clear()
print(stu, a)
