import time

def main():
    seconds=0
    strut=" the quick brown fox jumps over the lazy dog"
    zeus=input("retype: the quick brown fox jumps over the lazy dog")
    x=True
    while x==True:
        seconds+=1
        time.sleep(1)
    
    if zeus == strut:
        print("your bad at coding")
        x=False
        print(seconds)
    else:
        print("wrong")

main()