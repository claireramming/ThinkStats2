"""My solution to exercise 2.3"""
import thinkstats2

def Mode(hist):
    """returns mode. Does not return freq value related to the mode.
    Use AllModes with num=1 for that functionality."""
    freq, val = max([(freq, val) for val, freq in hist.Items()])
    return val

def AllModes(hist, num=0):
    """returns all modes, also added support for
    returning specific number of modes.
    Setting num=1 gives same as Mode function but also
    returns frequency value."""
    sort_modes = sorted(hist.Items(), key=lambda row: row[1], reverse=True)
    if not num:
        num = len(sort_modes)
    for freq, val in sort_modes[0:num]:
        print(val, freq)
