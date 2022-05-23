total = 0
counter = 1
while counter <= 10:
    grade = int (input("점수입력: "))
    total = grade + total
    counter = counter + 1
aver = total / 10 
print(aver)