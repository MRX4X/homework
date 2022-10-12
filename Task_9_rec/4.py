def cacluate(*a):
    c=sum(a)
    d = c / len(a)
    return (d, [i for i in a if i > d])
print(cacluate(3, 4, 5, 5, 6, 7, 66, 7))
