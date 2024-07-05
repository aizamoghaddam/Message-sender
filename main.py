import pyautogui
from random import choice


x = str(input('enter your message: '))
z = 1
y = int(input('how many messages should I send?: '))
width = 1136
height = 993


for i in range(z, y):
    pyautogui.click(width, height)
    # pyautogui.write(choice(lst))
    pyautogui.write(x)
    pyautogui.press('enter')

