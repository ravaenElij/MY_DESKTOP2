num_rows = int(input("Enter the number of rows"));
k = 8
l = 8
for i in range(0, num_rows):
    for j in range(l, k):
        print(end=" ")
    k = k - 2
    l = l - 2
    for j in range(0, i+1):
        print("* ", end="")
    print()
