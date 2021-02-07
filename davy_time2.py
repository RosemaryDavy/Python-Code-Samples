current_time = int(input("What time is it now?"))
wait_time = int(input("What is the number of hours to wait?"))



time_when_alarm_go_off = ((current_time + wait_time) %24)

print(time_when_alarm_go_off)
