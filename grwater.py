
user = int(input("Enter an integer: "))
user1 = int(input("Enter an integer: "))
user2 = int(input("Enter an integer: "))
user3 = int(input("Enter an integer: "))
user4 = int(input("Enter an integer: "))

if user > (user1 and user2 and user3 and user4):
            print(user)
if user1 > (user and user2 and user3 and user4):
            print(user1)
if user2 > (user1 and user and user3 and user4):
            print(user2)
if user3 > (user1 and user2 and user and user4):
            print(user3)
if user4 > (user1 and user2 and user3 and user):
            print(user4)

        



