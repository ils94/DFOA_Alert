from tkinter import Tk, Label, BOTH
import requests
import miscs
import time
from datetime import datetime
from playsound import playsound
from bs4 import BeautifulSoup

OA_site = "https://deadfrontier.com/OACheck.php"

started_time = ""

end_time = ""


def get_time():
    current_time = datetime.now().strftime("%H:%M:%S")

    return current_time


def countdown():
    global started_time, end_time

    t = 1980

    while t and not end_time:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        label_warning["text"] = "OUTPOST ATTACK!" \
                                "\n\nStarted at: " + started_time + \
                                "\n\nEnds in about: " + timer
        time.sleep(1)
        t -= 1

        if t < 3:
            label_warning["text"] = "The attack \n is about to end."
            break


def bs4soup(link):
    try:
        referer = "https://www.google.com/"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                 "AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/108.0.0.0 Safari/537.36", "referer": referer}

        return BeautifulSoup(requests.get(link, headers=headers).text, 'html.parser')
    except Exception as e:
        print(e)


def scan_oa_attacks():
    global started_time, end_time

    started_time = ""
    end_time = ""

    while True:

        attacks = str(bs4soup(OA_site)).replace("[", "").replace("]", "")

        if attacks:
            started_time = get_time()

            root.wm_state("normal")

            miscs.multithreading(countdown)

            playsound("alert.mp3")

            break

        time.sleep(3)

    while True:

        still_happening = str(bs4soup(OA_site)).replace("[", "").replace("]", "")

        if not still_happening:
            end_time = get_time()

            label_warning["text"] = "The attack has ended." \
                                    "\n\nStarted at: " + started_time + "\nEnded at: " + end_time

            time.sleep(10)

            miscs.multithreading(scan_oa_attacks)

            break

        time.sleep(3)


root = Tk()

width = 230
height = 120

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = screen_width - width

y = 0

root.geometry(f"{width}x{height}+{x}+{y}")
root.attributes("-topmost", True)
root.title("DFOA Alert")
root.iconbitmap("icon.ico")
root.resizable(False, False)

label_warning = Label(root, bg="black", fg="red", text="No attacks yet.", font=("Arial", 15), anchor="center")
label_warning.pack(fill=BOTH, expand=True)

miscs.multithreading(scan_oa_attacks)

root.mainloop()
