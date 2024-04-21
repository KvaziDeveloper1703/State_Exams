file = open("27B.txt")

N = int(file.readline())
data = []

for line in file:
    number_of_collection_point, number_of_test_tubes = map(int, line.split())
    if number_of_test_tubes % 36 == 0:
        number_of_containers = number_of_test_tubes //36
        data.append([number_of_collection_point, number_of_containers])
    else:
        number_of_containers = number_of_test_tubes //36 + 1
        data.append([number_of_collection_point, number_of_containers])

number_of_containers_before_current_collection_point = [0] * N
number_of_containers_before_current_collection_point[0] = data[0][1]
for i in range(1, N):
    number_of_containers_before_current_collection_point[i] = number_of_containers_before_current_collection_point[i-1] + data[i][1]

transportation_cost = 0

for i in range(N):
    transportation_cost += abs(data[i][0] - data[0][0]) * data[i][1]

minimum_transportation_cost = 10 ** 30

for i in range(1,N):
    transportation_cost = transportation_cost + (data[i][0] - data[i-1][0]) * number_of_containers_before_current_collection_point[i-1] - (data[i][0] - data[i-1][0]) * (number_of_containers_before_current_collection_point[-1] - number_of_containers_before_current_collection_point[i-1])
    minimum_transportation_cost = min(minimum_transportation_cost, transportation_cost)
print(minimum_transportation_cost)
