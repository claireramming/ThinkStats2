import nsfg
import thinkstats2
from modefunctions_mysolution import Mode, AllModes

df = nsfg.ReadFemPreg()
hist = thinkstats2.Hist(df.prglngth)
print('Mode:', Mode(hist))
AllModes(hist)
