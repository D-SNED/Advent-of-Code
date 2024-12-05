with open("2024/day_1.txt", "r") as file:
    data = file.read()
    data = data.split()


def total_between_lists(data):
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


# find how many times number in left list occurs in right list
# multiply left list number by number if occurences
# add up similarity scores


def find_similarity_score(data):
    l1 = []
    l2 = []

    for i in range(len(data)):
        if i % 2 == 0:
            l1.append(data[i])
        else:
            l2.append(data[i])

    l1 = sorted(l1)
    l2 = sorted(l2)

    similarity_dict = {}

    for i in range(len(l1)):
        if l1[i] not in similarity_dict:
            similarity_dict[l1[i]] = 0

    for i in range(len(l2)):
        if l2[i] in similarity_dict:
            similarity_dict[l2[i]] += 1

    similarity_total = 0

    print(similarity_dict)

    for key in similarity_dict:
        if similarity_dict[key] > 0:
            similarity_total += int(key) * similarity_dict[key]

    return similarity_total


# print(total_between_lists(data))
print(find_similarity_score(data))
