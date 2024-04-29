#!/bin/bash

#Retrieve data from the URL and store it to aviation.json
curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40,-90,45,-85"  > aviation.json

#parse json file and return first 6 receipt times
#need to find specifc pathway to receiptTime variable so manually curled data first
#it is actually .[].receiptTime (bc in the json file the first data structure is an array and then receiptTime is contained inside that array)
#note on last pipeline: head takes top outputs and flag -n limits how many entries are outputted
#cat ./aviation.json | jq -r '.receiptTime' aviation.json | head -n 6
cat ./aviation.json | jq -r '.[].receiptTime' aviation.json | head -n 6