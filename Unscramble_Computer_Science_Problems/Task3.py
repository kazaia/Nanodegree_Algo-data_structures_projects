
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

    receivers, codes = ([] for i in range(2))

    for line in calls:
        if line[0].startswith("(080)"):
            receivers.append(line[1])

    receivers = list(dict.fromkeys(receivers))
    
    for record in receivers:
        if record.startswith("(0"):
            codes.append(record[:record.find(")") +  1])
        if record.startswith("140"):
            codes.append(140)
        if record.startswith("7") or record.startswith("8") or record.startswith("9"):
            codes.append(record[0:4])
    codes = list(dict.fromkeys(codes))
    codes.sort()       
       print("The numbers called by people in Bangalore have codes:\n", "\n".join(codes))


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates."""

banglore_to_banglore =[]
banglore_to_all = []

for line in calls:
    if line[0].startswith("(080)") and line[1].startswith("(080)"):
        banglore_to_banglore.append(line[0])
