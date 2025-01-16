import webScrapper
import globalVariables
from tkinter import messagebox
import miscs
import countdownClock
from playsound import playsound
import time

OA_site = "https://deadfrontier.com/OACheck.php"


def scan_oa_attacks():
    globalVariables.has_ended = ""

    while True:
        try:
            attacks = str(webScrapper.bs4soup(OA_site)).replace("[", "").replace("]", "")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            continue

        if attacks:
            globalVariables.root.wm_state("normal")

            miscs.multithreading(lambda: countdownClock.countdown())

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

            globalVariables.label["text"] = "The attack has ended."

            time.sleep(3)

            miscs.multithreading(lambda: scan_oa_attacks)

            break

        time.sleep(3)
