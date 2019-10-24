# Generate multiples of 7 from 1 to 100

START = 1
END = 50
num = 7

for i in range(START, END+7):
  if i % num == 0:
    print(i, end=' ')
