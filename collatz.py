# Scenario
# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, skip to point 2.
c0 = int(input("Enter a natural number: "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
        print(c0)
        steps += 1
    else:
        c0 = 3 * c0 + 1       
        print(c0)
        steps += 1
print("Steps:", steps)
