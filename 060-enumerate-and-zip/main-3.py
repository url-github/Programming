# Listy danych
projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

# 1. Proste komunikaty
for project, leader in zip(projects, leaders):
    print(f'The leader of "{project}" is {leader}.')

print()  # Dodanie pustej linii dla czytelności

# 2. Komunikaty z datą rozpoczęcia projektu
for project, date, leader in zip(projects, dates, leaders):
    print(f'The leader of "{project}" started {date} is {leader}.')

print()  # Dodanie pustej linii dla czytelności

# 3. Komunikaty z numerem kolejności, datą i liderem
for idx, (project, date, leader) in enumerate(zip(projects, dates, leaders), start=1):
    print(f'{idx} - The leader of "{project}" started {date} is {leader}.')

print("-"*20)

for p, l in zip(projects, leaders):
    print('The leader of "{}" is {}'.format(p,l))

for p, l,d in zip(projects, leaders, dates):
    print('The leader of "{}" started {} is {}'.format(p,d,l))


for i, (p,l,d) in enumerate(zip(projects, leaders, dates)):
    print('{} - The leader of "{}" started {} is {}'.format(i+1,p,d,l))