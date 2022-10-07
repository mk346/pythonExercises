# Write a program that reads the following data into an array, computes and displays the average height.
# 5.1 ,5.4, 5.9, 5.0, 4.11, 6.1
from statistics import mean
num = [5.1, 5.4, 5.0, 5.9, 4.11, 6.1]
avg = mean(num)
print(round(avg,2))