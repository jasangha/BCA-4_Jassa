# from clint.textui import colored, puts
# from termcolor import colored, cprint
# import sys
import os

try:
    import colorama
    from colorama import Fore, Back, Style
except ImportError:
    os.system("pip install colorama")
# import json
# import requests


# def brwsr():
#     import os
#     import ctypes
#     import webbrowser

#     def yt():
#         url = "https://youtube.com/"
#         webbrowser.get().open(url)

#     def gl():
#         url = "https://google.com/"
#         webbrowser.get().open(url)

#     def rd():
#         url = "https://reddit.com/"
#         webbrowser.get().open(url)

#     print('Jassa')


# headers = {"Authorization": "Bearer 4/0AX4XfWhZgWe3ec2IxE15nagtJC9o_GwZgSwgLZ5HyqG36xPJcTmbZ_pgV2vLHbly1ULGYA"}
# para = {
#     "name": "jassa.txt",
#     # "parents": ["folder"]
# }
# files = {
#     'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
#     # replace 'application/zip' by 'image/png' for png images; similarly 'image/jpeg' (also replace your file name)
#     'file': ('application/txt', open("./jassa.txt", "rb"))
# }
# r = requests.post(
#     "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
#     headers=headers,
#     files=files
# )
# print(r.text)


# print(Fore.RED + "Jassa")

# text = colored('Jassa', 'red', attrs=['reverse', 'blink'])
# print(text)


colorama.init(autoreset=True)
# print('{:s}'.format('\u0332'.join("Jassa ")))
# print(Fore.RED+"Jassa")
# print(Fore.BLACK+"Jassa")
# print(f"{Fore.GREEN}{Style.BRIGHT}Jassa")
# print(f"{Fore.GREEN}{Style.NORMAL}Jassa")
# print(f"{Fore.GREEN}{Style.DIM}Jassa")
print(Fore.YELLOW+"Jassa")
print(Fore.BLUE+"Jassa")
print(Fore.MAGENTA+"Jassa")
print(Fore.CYAN+"Jassa")
print(Fore.WHITE+"Jassa")


# totalfiles = 0
# totaldirectories = 0
# music_dir = 'E:\\Music\\[Punjabi Songs]'
# for base, dirs, files in os.walk(music_dir):
#     for Directories in dirs:
#         totaldir += 1
#     for Files in files:
#         totalfiles += 1
# print(totalfiles)

# dict = {1: 0, 1: 9}
# print(dict)
