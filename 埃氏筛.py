is_prime = [True] * 100000
is_prime[0] = is_prime[1] = False # 0,1不是质数
# print(is_prime)
def E_sieve():
    for item in range(2, len(is_prime)):
        if is_prime[item]:
            for val in range(item**2,len(is_prime),item):
                is_prime[val] = False
        else:
            # print(f"{item}不是质数！")
            continue
E_sieve()
number = int(input("输入你想知道的输是否为质数:"))
if is_prime[number]:
    print(f"{number}是质数！")
else:
    print(f"{number}不是质数！")
