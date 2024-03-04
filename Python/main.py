"""
这个文件提供了学习Python函数时用到的代码
"""
# import sys
# sys.path.append('/Users/zengxiaowei/STUDY/Language/Language_Learning')
import time
from data.nums_data import nums
import numpy
print(numpy.__file__)
print(numpy.__version__)


    
"""
装饰器
"""
def d_calculate_execution_time(func):
    """这是一个装饰器，将打印所装饰的函数func的执行时间

    Args:
        func (_type_): 通常是一个数组
    """    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"函数{func.__name__}的执行时间为：{execution_time}秒")
        return result
    return wrapper

def merge(nums, start, end):
    """这是归并排序的归并操作

    Args:
        nums (List[int]): _description_
        start (int): _description_
        end (int): _description_
    """    
    mid = start + (end - start) // 2
    L = nums[start: mid + 1]
    R = nums[mid + 1: end + 1]
    
    i, j, k = 0, 0, start
    while i < len(L) and j < len(R):
        if L[i] > R[j]:
            nums[k] = R[j]
            j += 1
        else:
            nums[k] = L[i]
            i += 1
        k += 1
    while i < len(L):
        nums[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        nums[k] = R[j]
        j += 1
        k += 1
        
def merge_sort_recursion(nums, start, end):
    """这是归并排序的递归函数

    Args:
        nums (_type_): _description_
        start (_type_): _description_
        end (_type_): _description_
    """    
    if end > start:
        mid = start + (end - start) // 2
        merge_sort_recursion(nums, start, mid)
        merge_sort_recursion(nums, mid + 1, end)
        merge(nums, start, end)
        
@d_calculate_execution_time
def merge_sort(nums):
    """这是归并排序的入口

    Args:
        nums (_type_): _description_
    """   
    merge_sort_recursion(nums, 0, len(nums) - 1)
    return nums 
    
test = 0
merge_sort(nums) if test == 1 else print("还没有开始!")     
#merge_sort(nums)



"""生成器
"""
# def infinite_sequence():
#     num = 1
#     while num <= 20:
#         yield num
#         num += 1
        
# gen = infinite_sequence()
# for i in gen:
#     print(i)
    
# def read_large_file(file_object):
#     """读取文件的每一行并生成

#     Args:
#         file_object (_type_): _description_

#     Yields:
#         _type_: _description_
#     """
#     while True:
#         line = file_object.readline()
#         if not line:
#             break
#         yield line
        
# with open('large_file.log') as file:
#     """
#     with语法专门用来打开或者创建文件，不管文件操作是否发生异常，
#     都会将这个文件正常关闭
#     """    
#     log_lines = read_large_file(file)
#     for line in log_lines:
#         if '1234567' in line:
#             print(line)
            


"""闭包
"""
# def make_counter():
#     count = 0
#     def add():
#         # nonlocal count
#         count += 1
#         return count
#     return add

# def bank_account(init_balance):
#     balance = init_balance
#     def get_balance():
#         nonlocal balance
#         return balance
    
#     def deposit(amount):
#         nonlocal balance
#         balance += amount
#         return balance
    
#     def withdraw(amount):
#         nonlocal balance
#         if balance >= amount:
#             balance -= amount
#         else:
#             print("您的余额不足")
#         return balance
    
#     return get_balance, deposit, withdraw

# get_my_balance, deposit_my_money, withdraw_my_money = bank_account(10000)
# print(get_my_balance())
# deposit_my_money(2000)
# print(get_my_balance())
# withdraw_my_money(11000)
# print(get_my_balance())
# withdraw_my_money(3000)
# print(get_my_balance())
        
    
