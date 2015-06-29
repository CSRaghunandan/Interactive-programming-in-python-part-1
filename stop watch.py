# template for "Stopwatch: The Game"

import simplegui

# define global variables required for stop watch
count = 0
success = 0
tries = 0
timer_stopped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    D = t % 10
    temp = t / 10
    BC = temp % 60
    if BC == 0:
        BC = "00"
    elif BC < 10:
        BC = "0" + str(BC)
    A = temp / 60
    
    return str(A) + ":" + str(BC) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global timer_stopped
    timer.start()
    timer_stopped = False

def Stop():
    global success, tries, timer_stopped
    # if timer is already stopped, don't do anything.
    if timer_stopped == True:
        return
    
    timer.stop()
    timer_stopped = True

    if count % 10 == 0:
        success += 1
        tries += 1
    else:
        tries += 1
    
def Reset():
    global count, success, tries, timer_stopped
    count, success, tries = 0, 0, 0
    
    timer.stop()
    timer_stopped = True

# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count = count + 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(count),[110,110], 40, "red")
    hitmiss = str(success) + "/" + str(tries)
    canvas.draw_text(hitmiss, [250,30], 30, "green")
    
# create frame
frame = simplegui.create_frame("Stop watch", 300, 200)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", Start, 100)
frame.add_button("Stop", Stop, 100)
frame.add_button("Reset", Reset, 100)

# start frame
frame.start()
timer.start()
timer.stop()
# Please remember to review the grading rubric
