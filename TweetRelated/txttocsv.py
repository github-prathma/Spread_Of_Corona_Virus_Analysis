import csv
import re
with open('TweetInfo.txt', 'r') as infile, open('uncleanedtweet.csv', 'w') as outfile:
    stripped = (line.strip() for line in infile)
    new_list = []
    for text in stripped:
        if "    " in text:
            new = text.replace("    ", '##')
            new_list.append(new)
    lines = (line.split("##") for line in new_list if line)
    writer = csv.writer(outfile)
    writer.writerows(lines)
