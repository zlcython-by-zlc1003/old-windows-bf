import pyautogui
from pynput.keyboard import *
import time,random
#  ======== settings ========

delay = 0.1  # in seconds
times_to_refresh=30
refresh_button_pos=pyautogui.Point(x=88, y=49)
daily_btn_pos=pyautogui.Point(x=1249, y=750)

resume_key = Key.home
pause_key = Key.end
reset_pos = Key.num_lock
exit_key = Key.esc
#  ==========================

pos=pyautogui.position()
pause = True
running = True
times=0

def on_press(key):
    global running, pause, pos

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")
    elif key == reset_pos:
        pos=pyautogui.position()
        print("[Reset]")


def display_controls():
    print("// AutoClicker by Lucasz")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t HOME = Resume")
    print("\t END = Pause")
    print("\t ESC = Exit")
    print("\t NUM-LOCK = Reset")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')

def refresh():
    ttmp=pyautogui.position()
    pyautogui.click(refresh_button_pos)
    pyautogui.click(ttmp)
    time.sleep(30)
    pyautogui.click(daily_btn_pos)
    time.sleep(2)
    return 0


def main():
    global pos,times
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            times+=1
            if times==times_to_refresh:
                refresh()
                times=0
            tmp=(random.randint(pos[0]-5,pos[0]+500),random.randint(pos[1]-5,pos[1]+50))
            pyautogui.rightClick(tmp)
            pyautogui.click((tmp[0]+120+random.randrange(0,5),
                            tmp[1]+98+random.randrange(0,5)))
            pyautogui.moveTo(tmp)
            time.sleep(random.randrange(2,10))
            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()