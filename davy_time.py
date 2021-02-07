current_time = int(input("What is the current time (in hours 0-23)?"))
wait_time = int(input("How many hours do you want to wait?"))


final_time_str = (current_time + wait_time) % 24
print(final_time_str)
