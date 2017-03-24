import time # bring time
import webbrowser  # bring webbrowser

#how much views you want
#This only works when video has less than 300 views, it won't work when there are more than 300 views...
#due to youtube's policy.

print("Enjoy your Time\n" + time.ctime()) # print "Enjoy your time" and set newline and print variable
for count in range(30): # make a for loop that repeats if count is in range 30
    time.sleep(5) # pause the code for five seconds
    webbrowser.open("https://www.youtube.com/watch?v=o6A7nf3IeeA") # open a webbrowser with a specific link
