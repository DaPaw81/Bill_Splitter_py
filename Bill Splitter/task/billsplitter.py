import random

print('Enter the number of friends joining (including you):')
n1 = int(input())
if n1 < 1:
    print('No one is joining for the party')
    exit()

else:
    names = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(n1):
        name = str(input())
        names[name] = 0

print('Enter the total bill value:')
t_bill = int(input())

print('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
answer = input()
if answer == 'Yes':
    lucky_one = list(names.keys())  # Extract names from the dictionary keys
    mr_x = random.choice(lucky_one)
    print(f'{mr_x} is the lucky one!\n')
    n1 -= 1
    s_bill = round(t_bill / n1, 2)
    result = {name: s_bill for name in names}
    result[mr_x] = 0
    print(result)
    exit()
else:
    print('No one is going to be lucky\n')
    s_bill = round(t_bill / n1, 2)
    result = {name: s_bill for name in names}
    print(result)
