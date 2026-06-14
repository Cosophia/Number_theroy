
def E_sieve():
    for item in range(2, len(is_prime)):
        if is_prime[item]:
            for val in range(item**2,len(is_prime),item):
                is_prime[val] = False
        else:
            # print(f"{item}不是质数！")
            continue
    return None

def decomposition(num, prime_index_list):
    for val in range(2, num + 1):
        if is_prime[val] and num % val == 0:
            prime_index_list.append(val)
            num = num // val
            if is_prime[num]:
                prime_index_list.append(num)
                break
            else:
                num , prime_index_list=decomposition(num, prime_index_list)
    return  0 , []
# 1.单值
# number = int(input("输入你想知道的输是否为质数:"))
# is_prime = [True] * (number+1)
# is_prime[0] = is_prime[1] = False # 0,1不是质数
# prime_index =[]
# expression = f"{number} = "
# E_sieve() # 生成质数
# if is_prime[number]:
#     expression += str(number)
#     print(f"{number}是质数！")
#     print(expression)
# else:
#     print(f"{number}不是质数！")
#     decomposition(number,prime_index)
#     for item in prime_index:
#         expression += str(item) + " * "
#     if expression[-3:]==" * ":
#         expression = expression.rstrip(" * ")
#     print(expression)

# 2.批量值
number_list = list(range(1,100001))
is_prime = [True] * (len(number_list)+1)
is_prime[0] = is_prime[1] = False # 0,1不是质数
E_sieve()
for number in number_list:
    prime_index = []
    expression = f"{number} = "
    if is_prime[number]:
        expression += str(number)
        # print(f"{number}是质数！")
        print(expression)
    else:
        # print(f"{number}不是质数！")
        decomposition(number,prime_index)
        for item in prime_index:
            expression += str(item) + " * "
        if expression[-3:]==" * ":
            expression = expression.rstrip(" * ")
        print(expression)

