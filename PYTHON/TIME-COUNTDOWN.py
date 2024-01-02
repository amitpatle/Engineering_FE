import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  
        time.sleep(1)
        seconds -= 1
    print('Countdown finished!')

timer_duration = int(input("ENTER DURATION [In Second ] - "))
countdown_timer(timer_duration)
