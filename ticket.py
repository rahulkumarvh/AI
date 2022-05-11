def maxProfit(seats, k, n):
    list = []
    for i in range(k):
        list.append(seats[i])
    list.sort(reverse=True)
    profit = 0

    c = 0
    while(c < n):
        list.sort(reverse=True)
        top = list[0]
        list.pop(0)
        if(top == 0):
            break
        profit += top
        list.append(top - 1)
        c += 1
    return profit


if __name__ == "main":

    seats = [12, 11, 10, 10]
    k = len(seats)
    n = 4
    print(maxProfit(seats, k, n))
