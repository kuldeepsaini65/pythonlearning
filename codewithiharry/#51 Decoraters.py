# decorators is used in functions of function to use them in at the time of need in same programme

def print_my_name(func):
    def execute_now():
        print("Executing This Now....")
        func()
        print("Executed Sucessfully....")
    return execute_now()

def who_is_kuldeep():
    print("Kuldeep is New Coading Learner..")

who_is_kuldeep = print_my_name(who_is_kuldeep)

    #or

"""
@print_my_name      #this is important to this line above function that you want to print
def no_fun():
    print("Kuldeep is New Coading Learner..")
"""