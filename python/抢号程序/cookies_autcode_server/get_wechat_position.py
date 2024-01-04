import pyautogui
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)
pyautogui.click(currentMouseX, currentMouseY)