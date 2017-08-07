import time

def countdown(t):
    t = t*60 #sec2min
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Press ENTER to go to next session\n\n\n')
    input()

countdown(1)
countdown(1)
