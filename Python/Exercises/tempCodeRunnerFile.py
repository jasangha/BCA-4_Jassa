
numbers = [x * 5 for x in range(2000, 3000)]
results = []

progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i+1, len(n