# Program to add natural
# sum of natural numbers
# n*n+1/2

# To take input from the user,
n = int(input("Enter n: "))

#n = 10
#initialize sum and counter
sum = 0
i = 1

while i <=n:
    sum = sum + i
    i =i+1

print("The sum is", sum)