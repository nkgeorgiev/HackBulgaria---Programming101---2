def calculate_coins(sum):
    #sum *= 100
    sum = round(sum * 100)
    coins = {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0}
    coins[100] = sum // 100
    sum -= 100 * coins[100]
    coins[50] = sum // 50
    sum -= 50 * coins[50]
    coins[20] = sum // 20
    sum -= 20 * coins[20]
    coins[10] = sum // 10
    sum -= 10 * coins[10]
    coins[5] = sum // 5
    sum -= 5 * coins[5]
    coins[2] = sum // 2
    sum -= 2 * coins[2]
    coins[1] = sum

    return coins

print(calculate_coins(8.94))
