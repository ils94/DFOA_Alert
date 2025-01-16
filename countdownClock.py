import eventTimeCalculation
import time
import globalVariables


def countdown():
    event_times = eventTimeCalculation.calculate_remaining_minutes()

    t = event_times

    while t and not globalVariables.has_ended:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)

        globalVariables.label["text"] = "OUTPOST ATTACK!" \
                                        "\n\nEnds in about: " + timer
        time.sleep(1)
        t -= 1

        if t < 3 and not globalVariables.has_ended:
            globalVariables.label["text"] = "The attack \n is about to end."
            break
