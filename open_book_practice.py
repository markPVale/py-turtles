# a = "all"
# b = "work"
# c = "and"
# d = "no"

# print(a + " " + b + " " + c + " " + d)

# x = 6 * (1-2)
# print(x)

# def name_chunk():
#     name = input("Enter your name: ")
#     print(name)

# name_chunk()

# bruce = 6
# print(bruce + 4)


# P = 10000
# n = 12
# r = .08
# yr = input("how many years: ")
# t = int(yr)

# A = P*(1 + r/n)**(n*t)

# print(A)





# 7. You look at the clock and it is exactly 2pm. You set an alarm to go
# off in 51 hours. At what time does the alarm go off? (Hint: you could
# count on your fingers, but this is not what we’re after. If you are
# tempted to count on your fingers, change the 51 to 5100.)

# answer is contained in solution to next problem

# 8. Write a Python program to solve the general version of the above
# problem. Ask the user for the time now (in hours), and ask for the
# number of hours to wait. Your program should output what the time will
# be on the clock when the alarm goes off.

#! /usr/bin/env python3

# exercises 7 and 8 - compute the time in n hours, starting from 2pm



# Diff Version Found Online:

# n = int(input("How many hours: "))
# days = n//24
# timeafter = n%24
# if(timeafter > 10):
#     days = days + 1
#     hours = timeafter - 10
# else:
#     hours = timeafter + 14

# print("End time is in: ", days, "days at", hours, ":00 hours")


time_now = int(input('what is the time now? '))
alarm_time = int(input("in how many hours would you like your alarm to go off? "))

wake_time = (time_now + alarm_time) % 24

print(wake_time)

