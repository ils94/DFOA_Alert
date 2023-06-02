import eventTimeCalculation
import time
import globalVariables


def countdown(label):
    event_times = eventTimeCalculation.event_get_time()

    t = event_times[0]

    globalVariables.started_time = event_times[1]

    while t and not globalVariables.has_ended:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)

        label["text"] = "OUTPOST ATTACK!" \
                        "\n\nStarted at: " + globalVariables.started_time + \
                        "\n\nEnds in about: " + timer
        time.sleep(1)
        t -= 1

        if t < 3 and not globalVariables.has_ended:
            label["text"] = "The attack \n is about to end."
            break
