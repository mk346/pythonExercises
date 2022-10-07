# Write a program that displays even numbers between 20 and 50 and skips those divisible by 10.

for num in range(20,50,2):
    if not num % 10 == 0:
        print(num)
