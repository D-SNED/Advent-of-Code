with open("2024/day_2.txt", "r") as file:
    data = file.read()
    data = data.split("\n")
# find number of safe levels
# safe level is strictly increasing or decreasing
# numbers in safe level must be stepped between 1 - 3


def find_safe_levels(data):
    # create res var
    # iterate through each report
    # create safe var = None
    # if report != sorted report or report != reverse sorted report
    # break

    # iterate through each number
    # if report == sorted report:
    # if next number - current number > 3:
    # break
    # if next number - current number < 1:
    # break

    # if report == reverse sorted report:
    # if current number - next number > 3:
    # break
    # if current number - next number < 1:
    # break
    # set safe var = True
    # if safe var = True
    # add 1 to res
    # rest safe var = None
    # return res

    res = 0

    for report in data:
        report = report.split()
        safe = None

        if report == sorted(report):
            for i in range(len(report) - 1):
                if int(report[i + 1]) - int(report[i]) > 3:
                    print(i, report, "UNSAFE")
                    break
                elif int(report[i + 1]) - int(report[i]) < 1:
                    print(i, report, "UNSAFE")
                    break
                else:
                    safe = True

            # safe = True
        elif report == sorted(report, reverse=True):
            for i in range(len(report) - 1):
                if int(report[i]) - int(report[i + 1]) > 3:
                    # print(i, report, "UNSAFE")
                    break
                elif int(report[i]) - int(report[i + 1]) < 1:
                    # print(i, report, "UNSAFE")
                    break
                else:
                    safe = True

        if safe == True:
            res += 1
            print(report, "safe=TRUE")

        safe = None

    return res


print(find_safe_levels(data))
