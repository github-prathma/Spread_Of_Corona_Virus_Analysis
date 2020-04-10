from pathlib import Path

path1 = Path("COVID-19-TweetIDs-samples/by_hour/2020-01")
path2 = Path("COVID-19-TweetIDs-samples/by_hour/2020-02")
path3 = Path("COVID-19-TweetIDs-samples/by_hour/2020-03")

all_date_files = [p for p in path1.iterdir()] + \
    [p for p in path2.iterdir()] + [p for p in path3.iterdir()]
data = ""
AllIds = set()
dayNum = 0
for p in all_date_files:
    with open(p, 'r') as file:
        data = file.read().replace('\n', ' ')
        currentIds = data.split(" ")
        for Id in currentIds:
            if Id not in AllIds:
                AllIds.add(Id)

AllIDs = list(AllIds)
f = open("SamplingTweetID.txt", "w+")
for val in AllIDs:
    f.write(val + "\n")
f.close()
