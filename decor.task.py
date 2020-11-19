from datetime import datetime
import timeit
###1

# def get_time(func):
#     def wrapper():
#         time = datetime.now().hour
#         if time in range(9,21):
#             func()
#     return wrapper  

# @get_time
# def say_whee():
#     print("Whee")
# say_whee()

##2

# def get_time(func):
#     def time_():
#         time = timeit.timeit()
#         print(time)
#     return time_
      
# @get_time
# def show_time():
#     range(10)

# show_time()

###3

def repeat_func(num):
    num =int(input("enter num: "))
    def rep_func(func):
        def equal(*args,**kwargs):
            for name in range(num):
                func(*args,**kwargs)
        return equal
            
    return rep_func

@repeat_func(num=4)   
def func_name(name):
    print(f"{name}")

func_name(input('Enter name: '))


    


