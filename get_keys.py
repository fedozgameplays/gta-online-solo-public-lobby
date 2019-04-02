import win32api

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)


def key_check():
    keys = []
    for key in keyList:
        if win32api.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys
