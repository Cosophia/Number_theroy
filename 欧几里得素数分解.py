prime_list = []
used_prime_list = []
# Number -> prime mul prime mul ...
def is_prime(num):
    flag = 0
    if num == 1:
        return False
    if num in used_prime_list:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                flag += 1
            if flag > 0:
                return False
    return True


def prime_block(num, prime_lis):
    for val in range(2, num + 1):
        if is_prime(val) and num % val == 0:
            used_prime_list.append(val) # 可备用的质数
            num = num // val
            prime_lis.append(val)
            if is_prime(num): # 处理后的 数 是否为素数
                prime_lis.append(num)
                break
            else:
                if num == 1:
                    break
                num, prime_lis = prime_block(num, prime_lis)
            continue
        # else:
        # if is_prime(number):
        #     prime_list.append(number)
        #     break
        # continue
    return 0,[]





# number = int(input("A number:")) # 输入
# expression = f"{number} = " # 表达式前缀
# prime_block(number, prime_list)
# prime_list = sorted(prime_list)
# # dealing the equation
# for value in prime_list:
#     expression += str(value) + " * "
# if expression[-3:]==" * ":
#     expression = expression.rstrip(" * ")
# print(expression)
number_list = list(range(1,10001))
for number in number_list:
    prime_list = []
    expression = f"{number} = " # 表达式前缀
    prime_block(number, prime_list)
    prime_list = sorted(prime_list)
    # dealing the equation
    for value in prime_list:
        expression += str(value) + " * "
    if expression[-3:]==" * ":
        expression = expression.rstrip(" * ")
    print(expression)



