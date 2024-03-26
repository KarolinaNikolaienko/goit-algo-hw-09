# У конспекті ми розглянули приклад про розбиття суми на монети. Маємо набір монет [50, 25, 10, 5, 2, 1]. 
# Уявіть, що ви розробляєте систему для касового апарату, яка повинна визначити оптимальний спосіб видачі 
# решти покупцеві.

# Вам необхідно написати дві функції для касової системи, яка видає решту покупцеві:

# Функція жадібного алгоритму find_coins_greedy. Ця функція повинна приймати суму, яку потрібно видати покупцеві, 
# і повертати словник із кількістю монет кожного номіналу, що використовуються для формування цієї суми. 
# Наприклад, для суми 113 це буде словник {50: 2, 10: 1, 2: 1, 1: 1}. Алгоритм повинен бути жадібним, 
# тобто спочатку вибирати найбільш доступні номінали монет.
# Функція динамічного програмування find_min_coins. Ця функція також повинна приймати суму для видачі решти, 
# але використовувати метод динамічного програмування, щоб знайти мінімальну кількість монет, 
# необхідних для формування цієї суми. Функція повинна повертати словник із номіналами монет та їх 
# кількістю для досягнення заданої суми найефективнішим способом. 
# Наприклад, для суми 113 це буде словник {1: 1, 2: 1, 10: 1, 50: 2}
# Порівняйте ефективність жадібного алгоритму та алгоритму динамічного програмування, 
# базуючись на часі їх виконання або О великому та звертаючи увагу на їхню продуктивність при великих сумах. 
# Висвітліть, як вони справляються з великими сумами та чому один алгоритм може бути більш ефективним за 
# інший у певних ситуаціях. Свої висновки додайте у файл readme.md домашнього завдання.

import timeit

def find_coins_greedy(rest):
    coins = [50, 25, 10, 5, 2, 1]
    res = {}
    if rest:
        for coin in coins:
            res[coin] = rest // coin
            rest -= coin * res[coin]
    return res

def find_min_coins(rest, coins):
    coins_needed = [float("inf") for _ in range(rest + 1)]
    coins_needed[0] = 0
    coins_used = [0] * (rest + 1)

    for coin in coins[:-1]:
        for amount in range(len(coins_needed)):
            if coin <= amount and coins_needed[amount] > 1 + coins_needed[amount - coin]:
                coins_needed[amount] = 1 + coins_needed[amount - coin]
                coins_used[amount] = coin

    coins_count = {}
    rest_ = rest
    while rest_ > 0:
        coin = coins_used[rest_]
        coins_count[coin] = coins_count.get(coin, 0) + 1
        rest_ -= coin
    coins_to_return = {coin : coins_count.get(coin, 0) for coin in coins if coin in coins_count}
    return coins_to_return #coins_needed[rest]

def main():
    coins = [50, 25, 10, 5, 2, 1]
    n = len(coins)
    rest = [590, 3817, 20984, 598327]
    for r in rest:
        starttime = timeit.default_timer()
        res = find_coins_greedy(r)
        time = timeit.default_timer() - starttime
        print(f"Greedy for {r}:\n{res}\nTime: {time}\n")

        starttime = timeit.default_timer()
        res = find_min_coins(r, coins)
        time = timeit.default_timer() - starttime
        print(f"Dynamic for {r}:\n{res}\nTime: {time}\n\n")

if __name__ == "__main__":
    main()