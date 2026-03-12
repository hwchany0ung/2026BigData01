scores = [100,87,97,82]
hap = 0
count = 0
for score in scores:
    hap = hap + score
    count = count + 1

average = hap / count
print(average)