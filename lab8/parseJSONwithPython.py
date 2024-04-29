#!/bin/env python3

import json

#thinking to divide each step into seperate functions

#function to read the schacon.repos file (code from the instructions)
def readFile(filePath):
    with open(filePath, 'r', encoding='utf-8') as file: #needed to add that encoding line because of a special character error
        data = json.load(file)
    return data

#function to pull out the name, html_url, updated_at, and visibility fields from json and combine to a csv file
def writeToCSV(data, filePath):
    with open(filePath, 'w') as file: #w for write
        for x in data[:5]: #LIMIT the output to 5 lines only
            file.write(f"{x['name']},{x['html_url']},{x['updated_at']},{x['visibility']}\n") #four fields into a comma-separated line

#main function to create chacon.csv
def main():
    #variables for reusability
    jsonPath = "C:/Users/rdinh/OneDrive/Documents/GitHub/json-practice/data/schacon.repos.json" #input file path
    csvPath = "./chacon.csv" #output file name and path
    
    #input json data
    data = readFile(jsonPath)

    #writing to csv
    writeToCSV(data, csvPath)

#script execution
if __name__ == "__main__":
    main()

#outputted csv looks like instruction examples