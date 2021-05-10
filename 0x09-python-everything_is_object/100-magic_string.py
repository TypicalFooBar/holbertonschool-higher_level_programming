#!/usr/bin/python3
def magic_string(holbertonString=""):
    # magic_string.returnString = magic_string.returnString + ", Holberton" if hasattr(magic_string, "returnString") else "Holberton"
    holbertonString += "Holberton" if holbertonString == "" else ", Holberton"
    return holbertonString