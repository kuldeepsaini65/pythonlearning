# important note:- Please Change Library.txt with your txt file
# and check that your file texts are in lower Case

from time import sleep


def text_searcher():
    # from time import sleep
    print("Reading Your File.....")
    opener = open("Library.txt")
    sleep(5)
    reader = opener.read()

    while True:
        text = (yield)
        sleep(2)
        if text in reader:
            print(f"We Founded Your Text in File \nPosition of Text - {opener.tell()}")
        else:
            print("Oops....! \nWe Can't Found Your Text In File\n\t***********\n")

x = 0
print("**** Welcome To Our Coding Adda @codewithharry ****\n")
search = text_searcher()
next(search)
print("Done \nFile Read Successfully :-)\n")
sleep(2)

while x < 5:
    user_text = input("Please Enter Your Text Here:- ")
    search.send(user_text)
    sleep(1.27)
    x = x+1

print(f"\nI Hope It Will Work For You.....   ;-)")

