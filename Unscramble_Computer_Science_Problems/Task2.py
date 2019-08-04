
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    callers, timeInSeconds, receivers  = ([] for i in range(3))
    aDict = {}
    
    
    for line in calls:
        callers.append(line[0])

    for line in calls:
        receivers.append(line[1])

    for t in calls:
        timeInSeconds.append(t[3])

    timeInSeconds = list(map(int, timeInSeconds))

    callers_tuple = list(zip(callers, timeInSeconds))
    receivers_tuple = list(zip(receivers, timeInSeconds))
    all_numbers_tuple = callers_tuple + receivers_tuple

    for key, value in all_numbers_tuple:
        if key not in aDict.keys():
            aDict.update( {key : value} )
        else:
            aDict[key] += value
        
    total_time = max(aDict.values())

    for key, value in aDict.items():
        if value == total_time:
            telephoneNumber_longestCall = key
                
    print(telephoneNumber_longestCall," spent the longest time,", total_time," seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
