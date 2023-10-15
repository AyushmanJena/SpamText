import pyautogui

pyautogui.sleep(5)
f = open("Messages.txt", 'r')

i = 0

for word in f:
    pyautogui.hotkey('ctrl', 't')  # Press Ctrl + T

    if(i % 3 == 0):
        pyautogui.typewrite(word, 0.09, None, True)
        pyautogui.press("enter")
        pyautogui.sleep(3)

    elif(i % 3 == 1):
        pyautogui.typewrite(word, 0.04, None, True)
        pyautogui.press("enter")
        pyautogui.sleep(2)

    elif(i % 3 == 2):
        pyautogui.typewrite(word, 0.06, None, True)
        pyautogui.press("enter")
        pyautogui.sleep(4)

    i = i+1
    pyautogui.hotkey('ctrl', 'w')

f.close()
