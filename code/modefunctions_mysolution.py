"""My solution to exercise 2.3"""
import thinkplot

def Mode(hist):
    """returns mode. Does not return freq value related to the mode.
    Use AllModes with num=1 for that functionality."""
    mode = 0
    mode_val = 'empty'
    for val, freq in hist.Items():
        if mode < freq:
            mode = freq
            mode_val = val
    return mode_val

def AllModes(hist, num=0):
    """returns all modes, also added support for
    returning specific number of modes.
    Setting num=1 gives same as Mode function but also
    returns frequency value."""
    modes = []
    print('Val | Freq')
    for val, freq in hist.Items():
        modes.append((freq, val))
    sort_modes = sorted(modes, reverse=True)
    if not num:
        num = len(sort_modes)
    for freq, val in sort_modes[0:num]:
        print(val, freq)
