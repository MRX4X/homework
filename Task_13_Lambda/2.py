from operator import itemgetter
grades = [{'name': 'Jennifer', 'final': 95},
     {'name': 'David', 'final': 92},
    {'name': 'Aaron', 'final': 98}]
grades = sorted(grades, key=lambda grades: grades['name'])
print(grades)