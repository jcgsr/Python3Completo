# 14.12.2020
# Susi no hospital de tarde, Diana na casa da avó

x = 0
y = 10
print("WHILE")
while x < 8:
    while y >= 2:
       print(f'{x} {y}')
       y -= 1
       x += 1

print()
print("FOR")
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
