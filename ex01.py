num_list = input().split()
result = 0
count = 0

for i in range(len(num_list)):
    if int(num_list[i]) >= 0:
        result += int(num_list[i])
        count += 1

print(count, result)