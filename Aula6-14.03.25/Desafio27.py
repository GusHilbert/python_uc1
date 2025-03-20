# 🔢 Sequência de Fibonacci
# 🔖 Gere os primeiros 10 números da sequência de Fibonacci usando um while.


count = 0

while count <= 499:
    if count == 0:
        x = 1
        y = 1
        fibo = 1
        print(f"{count+1} - {fibo}")
        count+=1
    elif count == 1:
        x = 1
        y = 1
        fibo = 1
        print(f"{count+1} - {fibo}")
        count+=1
    else:
        fibo = x + y
        print(f"{count+1} - {fibo}")
        x = y
        y = fibo
        fibo = x + y
        count +=1