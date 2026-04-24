import time

# my_time = int(input("Enter the time in seconds : "))
# for x in range(my_time , 0 , -1):
#     print(x)
#     time.sleep(1) # it will wait for 1 second before printing the next number
    
# print("Time's up !")


# Digital clock 

time_in_seconds = int(input("Enter the time in seconds: "))
for x in range(time_in_seconds, 0, -1):
    second = x % 60
    minute = int((x / 60) % 60)
    hour = int(x / 3600)
    print(f"{hour:02}:{minute:02}:{second:02}") # :02 used to set defalt value of 0 if the number is less than 10
    time.sleep(1)

print("Time's up !")

