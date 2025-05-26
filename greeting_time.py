# Greeting Program Based on Time
import time
current_hour = int(time.strftime("%H"))
if 0 <= current_hour < 12:
    print("Good Morning Shoaib")
elif 12 <= current_hour < 17:
    print("Good Afternoon Shoaib")
else:
    print("Good Evening Shoaib")
