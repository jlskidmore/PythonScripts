import pyautogui
import time
import csv

# clear known host
pyautogui.hotkey("winleft")
time.sleep(1)
pyautogui.write("terminal")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("echo > ~/.config/freerdp/known_hosts2")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "shift", "q")

with open("servers.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        address = row[0]
        password = row[1]

        # open remmina
        pyautogui.hotkey("winleft")
        time.sleep(1)
        time.sleep(1)
        pyautogui.write("remmina")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)

        # login to RDP
        pyautogui.write(address)  # IP address
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("tab")  # accept certificate
        pyautogui.press("enter")  # accept certificate
        time.sleep(1)
        pyautogui.write("Administrator")  # username
        time.sleep(1)
        pyautogui.press("tab")
        pyautogui.write(password)  # password
        pyautogui.press("enter")

        # open powershell
        time.sleep(8)  # wait for 8 seconds
        pyautogui.hotkey("winright", "r")
        time.sleep(1)
        pyautogui.write("powershell")
        pyautogui.press("enter")

        # remove key
        time.sleep(1)
        pyautogui.write("slmgr /upk")
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("enter")

        # close remmina
        pyautogui.hotkey("winleft")
        time.sleep(1)
        pyautogui.write("terminal")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.write("pkill remmina")
        pyautogui.press("enter")
        pyautogui.hotkey("ctrl", "shift", "q")
