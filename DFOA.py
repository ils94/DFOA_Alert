from tkinter import Tk, Label, BOTH, messagebox
import requests
import miscs
import time
import datetime
from playsound import playsound
from bs4 import BeautifulSoup

OA_site = "https://deadfrontier.com/OACheck.php"

started_time = ""

end_time = ""

has_ended = ""


def event_time_calculation():
    global started_time, end_time

    current_time = datetime.datetime.now().time()

    event_start_minutes = [6, 36]

    event_duration = datetime.timedelta(minutes=30)

    closest_start_time = None
    closest_time_diff = datetime.timedelta(hours=1)

    for start_minute in event_start_minutes:
        start_time = datetime.datetime.combine(datetime.date.today(), datetime.time(current_time.hour, start_minute))

        if current_time >= start_time.time():
            time_diff = datetime.datetime.combine(datetime.date.today(), current_time) - start_time
        else:
            time_diff = start_time - datetime.datetime.combine(datetime.date.today(), current_time)

        if time_diff < closest_time_diff:
            closest_start_time = start_time
            closest_time_diff = time_diff

    started_time = closest_start_time.strftime("%H:%M")

    end_time = (closest_start_time + event_duration).strftime("%H:%M")

    remaining_time = closest_start_time + event_duration - datetime.datetime.now()

    remaining_seconds = int(remaining_time.total_seconds())

    return int(remaining_seconds)


def countdown():
    global started_time, has_ended

    t = event_time_calculation()

    while t and not has_ended:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)

        label_warning["text"] = "OUTPOST ATTACK!" \
                                "\n\nStarted at: " + started_time + \
                                "\n\nEnds in about: " + timer
        time.sleep(1)
        t -= 1

        if t < 3 and not has_ended:
            label_warning["text"] = "The attack \n is about to end."
            break


def bs4soup(link):
    referer = "https://www.google.com/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/108.0.0.0 Safari/537.36", "referer": referer}

    return BeautifulSoup(requests.get(link, headers=headers).text, 'html.parser')


def scan_oa_attacks():
    global has_ended

    has_ended = ""

    while True:
        try:
            attacks = str(bs4soup(OA_site)).replace("[", "").replace("]", "")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            continue

        if attacks:
            root.wm_state("normal")

            miscs.multithreading(countdown)

            playsound("alert.mp3")

            break

        time.sleep(3)

    while True:
        try:
            still_happening = str(bs4soup(OA_site)).replace("[", "").replace("]", "")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            continue

        if not still_happening:
            has_ended = "1"

            label_warning["text"] = "The attack has ended." \
                                    "\n\nStarted at: " + started_time + "\nEnded at: " + end_time

            time.sleep(3)

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
