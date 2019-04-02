import subprocess
import tkinter
import win32api
import win32con
import time
from tkinter import messagebox
from get_keys import key_check

WINDOW_WIDTH = 350
WINDOW_HEIGHT = 300
key = "K"
listening = False


def change_key(button, current_key):
    i = 0
    while True:
        keys = key_check()
        if len(keys) >= 1:
            new_key = keys
            button["text"] = str(new_key[0])
            current_key = str(new_key[0])
            break
        button["text"] = ""
        if i % 2 == 0:
            button["text"] = "_"
        i += 1
        main.update()
        time.sleep(0.5)
    return current_key


def run_listener(current_key, listening, stop_button, start_button):
    stop_button["state"] = "active"
    start_button["state"] = "disabled"
    messagebox.showinfo("Hinweis", "Das Programm läuft jetzt im Hintergrund und wartet auf den Kick-Befehl\nGTA V kann nach dem Bestätigen dieser Meldung gestartet werden.")
    main.iconify()
    listening = True
    while listening:
        if win32api.GetAsyncKeyState(win32con.VK_LCONTROL) and win32api.GetAsyncKeyState(ord(current_key)):
            subprocess.check_call('netsh interface ipv4 set subinterface "Ethernet" mtu=1500 store=persistent', shell=True)
            time.sleep(0.1)
            subprocess.check_call('netsh interface ipv6 set subinterface "Ethernet" mtu=1492 store=persistent', shell=True)
            time.sleep(1)
            subprocess.check_call('ipconfig /release', shell=True)
            subprocess.check_call('ipconfig /renew', shell=True)
            time.sleep(0.5)
            break
        main.update()
        time.sleep(0.25)


def stop_listener(listening, stop_button, start_button):
    stop_button["state"] = "disabled"
    start_button["state"] = "active"
    listening = False
    return listening


main = tkinter.Tk()
# main.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
main.title("GTA Online Solo Public")
main.iconbitmap("icon.ico")

l1 = tkinter.Label(main, text="Tastenkombination: ", font="12pt").grid(row="0", column="0", pady="10")
# Tastenkombination
l2 = tkinter.Label(main, text="STRG + ", font="12pt").grid(row="0", column="1")
b1 = tkinter.Button(main, text="K", font="12pt", width="2", command=lambda: change_key(b1, key))
b1.grid(row="0", column="2", padx="5")
b3 = tkinter.Button(main, text="Stop!", font="12pt", command=lambda: stop_listener(listening, b3, b2))
b3.grid(row="1", column="4", sticky="e", padx="10", pady="10")
b2 = tkinter.Button(main, text="Start!", font="12pt", command=lambda: run_listener(key, listening, b3, b2))
b2.grid(row="1", column="0", sticky="w", padx="10", pady="10")
b3["state"] = "disabled"
main.mainloop()
