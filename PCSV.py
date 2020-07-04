# PCSV - PythonCheckSumVerifier for Windows
# Created by PythonGgeek
# PCSV uses the GPLv3 free license.
__version__ = "1.2.4"
import subprocess


def russian():
    print("""Укажите тип хеша: 
    1. SHA1
    2. SHA256
    3. SHA384
    4. SHA512
    5. MD2
    6. MD4
    7. MD5""")
    what = input(">>> ")
    if what == "1":
        htype = "SHA1"
    elif what == "2":
        htype = "SHA256"
    elif what == "3":
        htype = "SHA384"
    elif what == "4":
        htype = "SHA512"
    elif what == "5":
        htype = "MD2"
    elif what == "6":
        htype = "MD4"
    elif what == "7":
        htype = "MD5"
    else:
        print("Введите допустимое значение! (1-7). Перезапустите программу во избежание ошибки.")

    checksum = input("Введите контрольную сумму: ")
    path = input("Введите путь до файла. (Вы можете использовать Drag and Drop.) : ")
    print("Ждите, программа выполняется. Это может занять пару минут.")
    output = subprocess.run(["certutil", "-hashfile", path, htype], stdout=subprocess.PIPE, text=True)
    newoutput = output.stdout.split("\n")
    if checksum == newoutput[1]:
        print("OK. Хеш-суммы совпадают.")
    else:
        print("Хеш-суммы не совпадают. Файл повреждён.")
    input("Нажмите Enter для выхода...")


def english():
    print("""Specify a hash type: 
    1. SHA1
    2. SHA256
    3. SHA384
    4. SHA512
    5. MD2
    6. MD4
    7. MD5""")
    what = input(">>> ")
    if what == "1":
        htype = "SHA1"
    elif what == "2":
        htype = "SHA256"
    elif what == "3":
        htype = "SHA384"
    elif what == "4":
        htype = "SHA512"
    elif what == "5":
        htype = "MD2"
    elif what == "6":
        htype = "MD4"
    elif what == "7":
        htype = "MD5"
    else:
        print("Enter a valid value! (1-7). Restart the program to avoid an error.")

    checksum = input("Enter the checksum: ")
    path = input("Enter a file path. (You can use Drag and Drop) : ")
    print("Wait, the program is running. It may take a couple of minutes.")
    output = subprocess.run(["certutil", "-hashfile", path, htype], stdout=subprocess.PIPE, text=True)
    newoutput = output.stdout.split("\n")
    if checksum == newoutput[1]:
        print("OK. Checksums match.")
    else:
        print("Checksums do not match. The file is damaged.")
    input("Press Enter to exit...")


try:
    language = open("Language.txt", "r")
except FileNotFoundError:
    print("Choose your language")
    print("1. English")
    print("2. Russian")
    l = input(">>> ")
    if l == "1":
        language = open("Language.txt", "w")
        language.write("English")
        language.close()
        english()
    elif l == "2":
        language = open("Language.txt", "w")
        language.write("Russian")
        language.close()
        russian()
else:
    if language.read() == "Russian":
        russian()
        language.close()
    else:
        english()
        language.close()

