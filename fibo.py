first=0
second=1
n=int(input("enter the value of n:"))
print(first)
print(second)
for i in range(n-1):
    third=first+second
    print(third)
    first=second
    second=third
