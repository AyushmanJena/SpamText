import pyautogui

pyautogui.sleep(10)
f = open("Messages.txt", 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    pyautogui.sleep(1)

f.close()
