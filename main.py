from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates


# title of your time period
title = "UC Merced Fall Semester 2023"

# gets todays date
currentDate = datetime.today()
year = currentDate.year
month = currentDate.month
day = currentDate.day
today = f'{year}-{month}-{day}'

# put your start/end dates of some time period, where today exists between the start/end dates
fall2023Start = '2023-08-23'
fall2023End = '2023-12-14'

# makes a list
dates = [fall2023Start, today, fall2023End]
todayPos = -1
datesLength = len(dates)
for i in range(datesLength):
    if dates[i] == today:
        todayPos = i

print(todayPos)
for i in range(datesLength):
    dates[i] = datetime.strptime(dates[i], "%Y-%m-%d")
# dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]

totalDays = int((((dates[datesLength-1]-dates[0]).total_seconds())/86400)+1)
daysLeft = int((((dates[2]-dates[todayPos]).total_seconds())/86400)+1)
daysCompleted = (totalDays-daysLeft)
percentCompleted = (daysCompleted/totalDays)*100
percentCompletedAsString = (str(percentCompleted)[0:5])+"%"
print(f'there are {totalDays} total days in this semester.')
print(f'there are {daysLeft} days remaining in this semester.')
print(f'that means we have completed {daysCompleted} days and are {percentCompletedAsString} through the semester.')

names = ['Start Fall 2023', 'You are here, at '+percentCompletedAsString+" completed.", 'End Fall 2023']
levels = np.tile([-5, 5, -3, 3, -1, 1], int(np.ceil(len(dates)/6)))[:len(dates)]

fig, ax = plt.subplots(figsize=(10, 4), layout="constrained")
ax.set(title=title)

ax.vlines(dates, 0, levels, color="tab:red")
ax.plot(dates, np.zeros_like(dates), "-o", color="k", markerfacecolor="w")
#test

for d, l, r in zip(dates, levels, names):
    ax.annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top")


ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")  # rotates the labels
ax.margins(y=0.1)

# clean up plot
ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)


plt.show()
