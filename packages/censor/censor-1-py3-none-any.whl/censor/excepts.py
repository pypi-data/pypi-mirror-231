# This file is placed in the Public Domain.
#
#


"exceptions"


errors = []
output = None
skip = ["PING", "PONG", 'PRIVMSG']


def debug(txt):
    if not output:
        return
    donext = False
    for skp in skip:
        if skp in txt:
            donext = True
    if donext:
        return
    output(txt)
