file = open("27A.txt")
N = int(file.readline())
data = []
for line in file:
    number_of_collection_point, number_of_test_tubes = map(int, line.split())
    if number_of_test_tubes % 36 == 0:
        data.append([number_of_collection_point, number_of_test_tubes//36])
    else:
        data.append([number_of_collection_point, number_of_test_tubes//36 + 1])

minimum_sum = 10 ** 30

for i in range(N):
    transportation_cost = 0
    for j in range(N):
        transportation_cost += abs(data[i][0] - data[j][0]) * data[j][1]
    minimum_sum = min(minimum_sum, transportation_cost)
print(minimum_sum)