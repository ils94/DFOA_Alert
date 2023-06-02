import webScrapper
import globalVariables
from tkinter import messagebox
import miscs
import countdownClock
from playsound import playsound
import time
import datetime

OA_site = "https://deadfrontier.com/OACheck.php"


def scan_oa_attacks(root, label):
    globalVariables.has_ended = ""

    while True:
        try:
            attacks = str(webScrapper.bs4soup(OA_site)).replace("[", "").replace("]", "")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            continue

        if attacks:
            root.wm_state("normal")

            miscs.multithreading(lambda: countdownClock.countdown(label))

            playsound("alert.mp3")

            break

        time.sleep(3)

    while True:
        try:
            still_happening = str(webScrapper.bs4soup(OA_site)).replace("[", "").replace("]", "")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            continue

        if not still_happening:
            globalVariables.has_ended = "1"

            end_time = datetime.datetime.now().strftime("%H:%M")

            label["text"] = "The attack has ended." \
                            "\n\nStarted at: " + globalVariables.started_time + "\nEnded at: " + end_time

            time.sleep(3)

            miscs.multithreading(scan_oa_attacks)

            break

        time.sleep(3)
