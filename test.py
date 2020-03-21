import tkinter
import win32api
import win32con
import time
import psutil
from tkinter import messagebox

key = "K"
listening = False
keyList = ["\b"]


for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)


def key_check():
    keys = []
    for key in keyList:
        if win32api.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys


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
            i = 0
        i += 1
        main.update()
        time.sleep(0.5)
    return current_key


def run_listener(current_key, listening):
    b3["state"] = "active"
    b2["state"] = "disabled"
    messagebox.showinfo("Hinweis", "Das Programm läuft jetzt im Hintergrund und wartet auf den Kick-Befehl.")
    main.iconify()
    listening = True
    while listening:
        if win32api.GetAsyncKeyState(win32con.VK_LCONTROL) and win32api.GetAsyncKeyState(ord(current_key)):
            for proc in psutil.process_iter():
                if "GTA5" in proc.name():
                    p = psutil.Process(proc.pid)
                    p.suspend()
                    time.sleep(9)
                    p.resume()

        main.update()
        time.sleep(0.25)


def stop_listener(listening):
    b3["state"] = "disabled"
    b2["state"] = "active"
    listening = False
    return listening


main = tkinter.Tk()
main.title("GTA Online Solo Public")
main.iconbitmap("icon.ico")
main.resizable(False, False)

l1 = tkinter.Label(main, text="Tastenkombination: ", font="12pt").grid(row="0", column="0", pady="10")
# Tastenkombination
l2 = tkinter.Label(main, text="STRG + ", font="12pt").grid(row="0", column="1")
b1 = tkinter.Button(main, text="K", font="12pt", width="2", command=lambda: change_key(b1, key))
b1.grid(row="0", column="2", padx="5")
b3 = tkinter.Button(main, text="Stop!", font="12pt", command=lambda: stop_listener(listening))
b3.grid(row="1", column="4", sticky="e", padx="10", pady="10")
b2 = tkinter.Button(main, text="Start!", font="12pt", command=lambda: run_listener(key, listening))
b2.grid(row="1", column="0", sticky="w", padx="10", pady="10")
b3["state"] = "disabled"
main.mainloop()
