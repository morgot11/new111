def exam_funk(argument):
    return sum(int(i) for i in str(argument))

start = int('9' * (159 // 9) + str(159 % 9))
print(start)
counter = 0
for i in range(start, 2 ** 63 + 1):
    print(i)
    if exam_funk(i) == 159:
        counter += 1
