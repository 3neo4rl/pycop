# python module zum besseren kopieren von bestimmten Dateiene

import os, shutil


def copy(begin, num_form, num_end, end="", data = ".MP4"):
    int(num_end)
    print("[*] start copying")
    count_v = 1
    while count_v <= num_end:
        i = count_v
        i = count(num_form, i)
        run = begin + i + end + "/" + begin + i + end +data
        if os.path.exists(run):
            print("[+] copy of " + run)
            ziel = os.environ['HOME'] + "/Video/import/" + i
            try:
                shutil.copy(run, "export" + i+ data)
                print("[+] Copy of " + run + " sucessful")
            except:
                print("[-] error : copy of file " + run + " was not sucessful")
        count_v += 1


def count(num_form, i):
    i = int(i)
    if num_form == 2:
        if i <= 9:
            i = "0" + str(i)
    if num_form == 3:
        if i <= 9:
            i = "00" + str(i)
        elif i <= 99:
            i = "0" + str(i)
    if num_form == 4:
        if i <= 9:
            i = "000" + str(i)
        elif i <= 99:
            i = "00" + str(i)
        elif i <= 999:
            i = "0" + str(i)
    if num_form == 5:
        if i <= 9:
            i = "0000" + str(i)
        elif i <= 99:
            i = "000" + str(i)
        elif i <= 999:
            i = "00" + str(i)
        elif i <= 9999:
            i = "0" + str(i)
    return str(i)

def JVC(a):
    copy("735_", 4, a, end = "_01")