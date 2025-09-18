prices = input("Введите цены акций через пробел: ")
prices = list(map(int, prices.split()))

min = 10000
pribil = 0

for i in range(len(prices)):
    if prices[i] < min:
        min = prices[i]
    else:
        pribil = max(pribil, prices[i] - min)

print(pribil)