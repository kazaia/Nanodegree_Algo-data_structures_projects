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
    
 incomingNumbers_calls, answeringNumbers_calls, incomingNumbers_texts, answeringNumbers_texts, allNumbers = ([] for i in range(5))

    for line in texts:
        incomingNumbers_texts.append(line[0])
        
    for line in texts:
        answeringNumbers_texts.append(line[1])
    
    for line in calls:
        incomingNumbers_calls.append(line[0])
        
    for line in calls:
        answeringNumbers_calls.append(line[1])

    allNumbers =  incomingNumbers_calls + answeringNumbers_calls + incomingNumbers_texts + answeringNumbers_texts

    allNumbers = list(dict.fromkeys(allNumbers))

    print("There are ", len(allNumbers) , " different telephone numbers in the records.")
        


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
    
