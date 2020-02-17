import os
import csv
from filter import listtocsv

def Convert(string, inter):
    text = list(string.split(inter))  # splits string into columns
    return text


def TrimLine(list):  # trims data line to usable format
    trimmed = []  # creates local list for trimmed data
    untrimmed = list  # saves line to local variable
    trimmed.append(untrimmed[4])  # Adds ID value to trimmed data
    trimmed.append(untrimmed[7])  # Adds the textual definition and caseSignificanceID
    return trimmed


def ExportValue(header, string, finalList):  # exports data from finalList to csv file
    try:
        os.remove(string)  # removes NLPData.csv if already exists
    except:
        print("Printing Output")  # confirmation

    with open(string, 'w', newline="") as chi:  # opens NLPData.csv and writes lines for each frequency report
        writer = csv.writer(chi)
        writer.writerow(header)
        for row in finalList:  # runs through items of finalList
            writer.writerow(row)  # writes them in CSV


def NLPFunc():
    txtfile = "sct2_TextDefinition_Full-en_US1000124_20190901.txt"  # has user enter address for text file.
    ExportFile = "NLPData.csv"
    MasterFrequency = ["Word Count", "Average Word Length", "Term ID", "Longest Word",
                       "Terms"]  # appends headers to MasterFrequency List

    x = open(txtfile, "r")
    terminology = dict()
    contents = x.readlines()
    WordFrequency = []  # generates array to contain frequency reports
    for y in contents[1:]:  # runs through lines of
        Terms = dict()  # dict for terms in definition
        FrequencyReport = []  # report on frequency and complexity of
        LineList = Convert(y, "\t")  # converts line from tesxt
        LineList = TrimLine(LineList)  # Trims the data
        averageLength = 0  # averageLength placeholder
        ID = y[0]  # sets ID string equal to ID value from TextDefinition Sheet
        longest = 'x'  # variable to keep track of longest words in line with starting value of one character in length
        terminology[int(LineList[0])] = [str(LineList[1])]
        counter = 0
        for i in Convert(LineList[1].lower(), " "):  # adds terms in definition to dictionary
            counter = counter + 1
            if i in Terms:
                Terms[i] = Terms[i] + 1
            else:
                Terms[i] = 1
        Terms = sorted(Terms.items(), key=lambda x: x[1],
                       reverse=True)  # sorts terms highest to lowest according to value
        total = 0
        for i in Terms:
            y, z = i
            total += len(y)
            if len(y) > len(longest):
                longest = y

        total = total / len(Terms)
        FrequencyReport.append(counter)  # adds count placeholder to Frequency Report
        FrequencyReport.append(total)  # adds averageLength placeholder to Frequency Report
        FrequencyReport.append(LineList[0])  # adds ID to Frequency Report
        FrequencyReport.append(longest)  # adds Longest placeholder to Frequency Report
        for i in Terms:
            FrequencyReport.append(i)
        WordFrequency.append(FrequencyReport)
    listtocsv(terminology, "NLP.csv")
    ExportValue(MasterFrequency, ExportFile, WordFrequency)
    return terminology

if __name__ == '__main__':
    NLPFunc()
