import math
from time import time, localtime, strftime, sleep
from os import system

starting_time = time() 
time_now = starting_time

clear = lambda: system('clear')

while True:
	time_now = time()
	if (math.floor(time_now - starting_time) >= 1):
		clear()
		print(strftime("%M %S", localtime(math.floor(time_now - \
		starting_time))))
		
	sleep(1)
