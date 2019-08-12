
'''装饰器本质：调用函数时通过注解找到装饰器定义，在wrapper中详细对函数进行代理，外层def仅仅是为了寻址'''

# print('Hello World')
import time

def display(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)    #此处的 result 接收 func函数(prime_num函数)的返回值 
        e_time = time.time()
        print("the time cost: ",(e_time-start_time))
        
        return result

    return wrapper


def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
@display        
def prime_num(maxnum):
    count = 0
    for i in range(2,maxnum):
        if is_prime(i):
            print(i)
            count += 1
            
    return count
                
# prime_num(10)

count = prime_num(100)
print('素数的个数为：',count)
