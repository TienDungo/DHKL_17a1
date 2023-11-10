import time

def countdown (seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1 

    print("Start!!!")

countdown(10)