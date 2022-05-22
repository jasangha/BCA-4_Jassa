from tabulate import tabulate

data_list = [['Name', 'Age', 'Job'], ['Mike', '30', 'Engineer'], [
    'John', '40', 'Doctor'], ['Mary', '25', 'Teacher'], ['Bob', '20', 'Student']]

data_dict = {'Name': ['Mike', 'John', 'Mary', 'Bob'], 'Age': [
    '22', '33', '44', '55'], 'Job': ['Engineer', 'Doctor', 'Teacher', 'Student']}

print(tabulate(data_list, headers='firstrow',
      showindex='always', tablefmt='fancy_grid'))

print(tabulate(data_dict, headers='keys',
      showindex='always', tablefmt='fancy_grid'))

# with open("jassa.tex", 'w') as f:
with open("jassa.html", 'w') as f:
    f.write(tabulate(data_list, headers='firstrow', tablefmt='html'))
