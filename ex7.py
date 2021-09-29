def birthday(x):
    question=input("enter name:")
    if question in x:
        print(x.get(question))
    else:
        print("no such name")

birthday({"ruchi":22,"yathi":55,"bhagya":45,"kundan":18})

