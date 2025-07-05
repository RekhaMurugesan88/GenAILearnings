import pyautogui
import time
import webbrowser

time.sleep(3)
webbrowser.open("https://www.gmail.com")
time.sleep(10)
pyautogui.click(747,463)
time.sleep(5)
pyautogui.scroll(-500)
time.sleep(2)
pyautogui.scroll(500)
time.sleep(2)
#x,y = pyautogui.position()
#print(f'x:{x},y:{y}')
pyautogui.doubleClick(1780,474)
time.sleep(2)
pyautogui.write("rekhatest88@gmail.com")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(758,689)
time.sleep(1)
pyautogui.write("test reply")
time.sleep(1)
pyautogui.hotkey('ctrl','Enter')


