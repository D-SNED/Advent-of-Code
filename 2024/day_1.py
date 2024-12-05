def total_between_lists():
    with open("2024/day_1.txt", "r") as file:
        data = file.read()
        data = data.split()
        l1 = []
        l2 = []

        for i in range(len(data)):
            if i % 2 == 0:
                l1.append(data[i])
            else:
                l2.append(data[i])

        l1 = sorted(l1)
        l2 = sorted(l2)

        res = 0

        for i in range(len(l1)):
            res += abs(int(l1[i]) - int(l2[i]))

        return res


print(total_between_lists())
