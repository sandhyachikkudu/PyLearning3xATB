# def complete_in_future():
#     pass
#
# complete_in_future()


# decaorators
# decorators is essentially takes a function as an argument
# returns  a new function usually  extend


def my_decorator(func):
    def wrapper():
        print("starting")
        print("********************")
        func()
        print("********************")
        print("ending")

    return wrapper()
@my_decorator
def say_hello():
    print("say hello")

import time
def note_time_taken(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("tmie take:"+str(end - start))


    return wrapper()


@note_time_taken
def log_function():
    time.sleep(5)
    print("log function take")
    print("print the logs of time")














