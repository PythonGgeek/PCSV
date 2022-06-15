# PCST - PythonCheckSumTool
# Based on PythonGgeek's PCSV
# PCST uses the GPLv3 free license.
# Forked and reworked by slezy

__version__ = "1.0"

import subprocess
import pyperclip
import colorama
from colorama import Fore

colorama.init()

def selection():

    print(Fore.CYAN + """[/] Select mode: 
    [1] Get checksum
    [2] Verify checksum""")

    mode = input("> ")

    if mode == "1":
        extract1()

    if mode == "2":
        verify1()

    else:
        input(Fore.RED + "[-] Wrong value entered. Press enter to try again.")
        selection()


def extract1():

    print(Fore.CYAN + """[/] Select a hash type to extract: 
    [1] SHA1
    [2] SHA256
    [3] SHA384
    [4] SHA512
    [5] MD2
    [6] MD4
    [7] MD5""")

    extract = input("> ")

    if extract == "1":
        htype = "SHA1"
    elif extract == "2":
        htype = "SHA256"
    elif extract == "3":
        htype = "SHA384"
    elif extract == "4":
        htype = "SHA512"
    elif extract == "5":
        htype = "MD2"
    elif extract == "6":
        htype = "MD4"
    elif extract == "7":
        htype = "MD5"

    else:
        input(Fore.RED + "[-] Wrong value entered. Press enter to try again.")
        extract1()

    path = input("[/] Enter a file path. (You can use Drag and Drop): ")

    if path == "":
        input(Fore.RED + "File's path hasn't been entered. Press enter to try again.")
        extract1()

    print(Fore.YELLOW + "[/] The program is running. It may take a couple of minutes (depends on file size)")

    output = subprocess.run(["certutil", "-hashfile", path, htype], stdout=subprocess.PIPE, text=True)

    newoutput = output.stdout.split("\n")

    print(f"{Fore.GREEN}[+] Done! The file's {htype} checksum is: {Fore.WHITE + newoutput[1]}")

    a = print(Fore.CYAN + """[/] What's next?
    [Press ENTER] to close PCST
    [0] Copy checksum to clipboard
    [1] Get hash
    [2] Verify hash""")

    q = input("> ")

    if q == "0":
        pyperclip.copy(newoutput[1])
        print(Fore.GREEN + "Copied")
        selection()
    if q == "1":
        extract1()
    if q == "2":
        verify1()
    else:
        print(Fore.CYAN + """[?] Are you sure?
    [Press ENTER] Yes
    [0] No""")
        x = input("> ")
        if x == "0":
            selection()
        else:
            exit()


def verify1():

    print(Fore.CYAN + """[/] Select a hash type to verify: 
    [1] SHA1
    [2] SHA256
    [3] SHA384
    [4] SHA512
    [5] MD2
    [6] MD4
    [7] MD5""")

    verify = input("> ")

    if verify == "1":
        htype = "SHA1"
    elif verify == "2":
        htype = "SHA256"
    elif verify == "3":
        htype = "SHA384"
    elif verify == "4":
        htype = "SHA512"
    elif verify == "5":
        htype = "MD2"
    elif verify == "6":
        htype = "MD4"
    elif verify == "7":
        htype = "MD5"

    else:
        input(Fore.RED + "[-] Wrong value entered. Press enter to reload.")
        verify1()

    checksum = input(f"{Fore.CYAN}[/] Enter the {htype} checksum: ")

    path = input(Fore.CYAN + "[/] Enter a file path. (You can use Drag and Drop): ")
    
    if path == "":
        input(Fore.RED + "File's path hasn't been entered. Press enter to try again.")
        verify1()

    print(Fore.YELLOW + "[/] The program is running. It may take a couple of minutes (depends on file size)")

    output = subprocess.run(["certutil", "-hashfile", path, htype], stdout=subprocess.PIPE, text=True)

    newoutput = output.stdout.split("\n")

    if checksum == newoutput[1]:
        print(f"{Fore.GREEN}[+] Done! {htype} checksums matches.")

    if checksum != newoutput[1]:
        print(Fore.RED + "[-] Checksums doesn't match. The file is damaged.")

    b = print(Fore.CYAN + """[/] What's next?
    [Press ENTER] to leave PCST
    [1] Get checksum
    [2] Verify checksum""")

    j = input("> ")

    if j == "1":
        extract1()
    if j == "2":
        verify1()
    else:
        print(Fore.CYAN + """[?] Are you sure?
    [Press ENTER] Yes
    [0] No""")
        z = input("> ")
        if z == "0":
            selection()
        else:
            exit()

selection()