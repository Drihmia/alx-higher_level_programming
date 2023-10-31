def uppercase(str):
    for ch in str:
        if ch >= 'a' and ch <= 'z':
            ch = chr(ord(ch) - ord(" "))
        print(ch, end="")
    print("")
