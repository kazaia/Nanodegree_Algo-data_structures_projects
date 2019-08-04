
"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

ongoingCalls, callsReceivers, ongoingTexts, textsReceivers, telemaketersNumbers = ([] for i in range(5))

for line in calls:
    ongoingCalls.append(line[0])
    callsReceivers.append(line[1])

for line in texts:
    ongoingTexts.append(line[0])
    textsReceivers.append(line[1])

telemaketersNumbers = list(set(ongoingCalls) - set(textsReceivers) - set(callsReceivers) - set(ongoingTexts))
