newArray = []
def leaderboardOrder():
    file = open("/home/bob/PycharmProjects/PythonProject/TCP/ServerLeaderboard","r")
    for line in file:
        line = line.strip()
        if line:
            parts = line.split(',')
            if len(parts) > 1:
                second_value = parts[1]
                res = [int(second_value)]
                newArray.append(*res)
    print(newArray)
    file.close

def bubble_sort():
    for n in range(len(newArray) - 1,0,-1):
        swapped = False

        for i in range(n):
            if newArray[i] > newArray[i + 1]:
                newArray[i], newArray[i + 1] = newArray[i + 1], newArray[i]

                swapped = True
        if not swapped:
            break

print("Un-sorted")
leaderboardOrder()
print("Sorted")
bubble_sort()
print(newArray)