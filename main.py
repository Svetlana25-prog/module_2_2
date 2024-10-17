first = 42
second = 49
third = 42
if first == second == third:
    print(3)
elif (first == second) or (first == third) or (second == third):
    print(2)
else:
    print(0)