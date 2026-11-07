import time
import win32gui
import win32con
import os
import ctypes
def screen_off():
    ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)
def hide_console_buttons():
    hwnd = win32gui.GetForegroundWindow()
    if hwnd:
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
        style &= ~win32con.WS_MINIMIZEBOX
        style &= ~win32con.WS_MAXIMIZEBOX
        style &= ~win32con.WS_SYSMENU
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)
        win32gui.SetWindowPos(hwnd, 0, 0, 0, 0, 0,
                            win32con.SWP_NOMOVE |
                            win32con.SWP_NOSIZE |
                            win32con.SWP_NOZORDER |
                            win32con.SWP_FRAMECHANGED)

hide_console_buttons()
b = 0
print("Привет, как думаешь, кто лучше?")
print("------------------------------")
print("[1] МУЖЧИНА!!!!")
print("[2] женщина.!.")
print("------------------------------")
a = int(input())
print("------------------------------")
if a == 1:
    print("ДААААААА МУЖЧИНЫ ЛУЧШЕ!!!!!!")
elif a == 2:
    print("ФУ ПОШЛА НАХУЙ ЖЕНЩИНА, УДАЛЯЮ КОМПЬЮТЕР!!!")
    print("-------------------------------------------")
    print("ВНИМАНИЕ ПРИ ПОПЫТКЕ ЗАКРЫТИЯ ПРОГРАММЫ, КОМПЬЮТЕР БУДЕТ УНИЧТОЖЕН БЕЗ ВОЗМОЖНОСТИ ВОССТАНОВЛЕНИЯ!!!")
    print("----------------------------------------------------------------------------------------------------")
    while b < 101:
        print("Удаление компьютера... ",b,"%")
        if b == 100:
            screen_off()
            os.system('shutdown -s')
            b = b + 1
        else:
            b = b + 1
            time.sleep(1)
