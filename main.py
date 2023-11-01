from pyautogui import moveTo, sleep, click
from winsound import MessageBeep, MB_ICONHAND

sleep(5)
for i in range(25):
    moveTo(1250, 275, 0.2)
    click(button="right")
    moveTo(1155, 275, 0.2)
    click(button="right")
    moveTo(1065, 275, 0.2)
    click(button="right")
    moveTo(920, 575, 0.2)
    click(button="right")
    moveTo(835, 675, 0.2)
    click()
    sleep(5)
MessageBeep(MB_ICONHAND)
# MessageBeep(-1)
