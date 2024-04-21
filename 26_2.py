file = open("26_2.txt")
N = int(file.readline())

array_of_box_sizes = []

for iteration in range(N):
    size = int(file.readline())
    array_of_box_sizes.append(size)

array_of_box_sizes.sort(reverse=True)

number_of_boxes=1
current_size = array_of_box_sizes[0]

for i in range(1,len(array_of_box_sizes)):
    if current_size - array_of_box_sizes[i]>=3:
        number_of_boxes += 1
        current_size = array_of_box_sizes[i]
print(number_of_boxes, current_size)