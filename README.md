# DFOAlert
Simple tool to alert when an Outpost Attack started in Dead Frontier 3D game.

# How does it works?

A loop will be scanning for Outpost Attacks every 3 seconds, then, when the DFOA API returns something, it will then start a 
countdown of 33 minutes which is an approximate of the length of the event (may vary a lot)

It will then keep scanning to see if the event has ended, and if so, it will display the time the event started 
and when it ended (using the time zone of the player's computer)

Why not just use the Discord bot?

Because the Discord bot is not precisely enough and because I'm not always on Discord. This tool is accessing DF3D's API directly 
and displaying the real deal.
