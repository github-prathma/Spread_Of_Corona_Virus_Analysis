import math
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 14
plt.rcParams['legend.fontsize'] = 'medium'

'''
Read txt to numpy arrays
'''


def txt_to_matrix(filename):
    try:
        file = open(filename)
    except IOError:
        print("File doesn't exist: " + filename)
        return None
    else:
        lines = file.readlines()
        rows = len(lines)

        datamat = np.zeros((rows, 1), dtype=int)

        row = 0
        for line in lines:
            line = line.strip().split('\t')
            datamat[row, :] = line[:]
            row += 1

    return datamat


'''
Sample by days
'''
hr = "/Volumes/TOSHIBA SSD/PycharmProjects/COVID-19/COVID-19-TweetIDs-master/2020-"
hw = "/Users/mashazhou/PycharmProjects/COVID-19/COVID-19-TweetIDs-samples/"
for month in ["01", "02", "03"]:
    for day in range(1, 32):
        print("===== Read date: " + month + "-" + str(day).zfill(2) + " =======")
        datavec = np.zeros((0, 1), dtype=int)
        for hour in range(24):
            fr = hr + month + "/coronavirus-tweet-id-2020-" + month + "-" + str(day).zfill(2) + "-" + str(hour).zfill(
                2) + ".txt"
            if txt_to_matrix(fr) is not None:
                datavec = np.vstack((datavec, txt_to_matrix(fr)))

        row_sample = np.random.choice(datavec.shape[0], size=math.ceil(0.001 * datavec.shape[0]), replace=False,
                                      p=None)
        data_sample = datavec[row_sample]
        if data_sample.shape[0] > 0:
            fw = hw + "by days/2020-" + month + "-" + str(day).zfill(2) + ".txt"
            np.savetxt(fw, data_sample, fmt=['%s'], newline='\n')

'''
Sample by hours
'''
hr = "/Volumes/TOSHIBA SSD/PycharmProjects/COVID-19/COVID-19-TweetIDs-master/2020-"
hw = "/Users/mashazhou/PycharmProjects/COVID-19/COVID-19-TweetIDs-samples/"
for month in ["01", "02", "03"]:
    for day in range(1, 32):
        print("===== Read date: " + month + "-" + str(day).zfill(2) + " =======")
        for hour in range(24):
            fr = hr + month + "/coronavirus-tweet-id-2020-" + month + "-" + str(day).zfill(2) + "-" + str(hour).zfill(
                2) + ".txt"
            if txt_to_matrix(fr) is not None:
                datavec = txt_to_matrix(fr)

                row_sample = np.random.choice(datavec.shape[0], size=math.ceil(0.001 * datavec.shape[0]), replace=False,
                                              p=None)
                data_sample = datavec[row_sample]
                if data_sample.shape[0] > 0:
                    fw = hw + "by hours/2020-" + month + "-" + str(day).zfill(2) + "-" + str(hour).zfill(2) + ".txt"
                    np.savetxt(fw, data_sample, fmt=['%s'], newline='\n')

'''
Time serious by days
'''
head = "/Users/mashazhou/PycharmProjects/COVID-19/COVID-19-TweetIDs-samples/by day/"
nums = []
for month in ["01", "02", "03"]:
    for day in range(1, 32):
        print("===== Read date: " + month + "-" + str(day).zfill(2) + " =======")
        filename = head + "2020-" + month + "-" + str(day).zfill(2) + ".txt"
        if txt_to_matrix(filename) is not None:
            nums.append(txt_to_matrix(filename).shape[0])

plt.plot([i for i in range(1, len(nums) + 1)], nums, linestyle='-', linewidth=2.5)
plt.xlabel("# Days Since 2020-01-21")
plt.ylabel("# Sampled Tweets")
plt.savefig("/Users/mashazhou/PycharmProjects/COVID-19/COVID-19-TweetIDs-samples/figures/by_day.eps",
            bbox_inches = 'tight')
plt.show()

'''
Time serious by hours
'''
head = "/Users/mashazhou/PycharmProjects/COVID-19/COVID-19-TweetIDs-samples/by hour/"
nums = []
for month in ["01", "02", "03"]:
    for day in range(1, 32):
        print("===== Read date: " + month + "-" + str(day).zfill(2) + " =======")
        for hour in range(24):
            filename = head + "2020-" + month + "-" + str(day).zfill(2) + "-" + str(hour).zfill(2) + ".txt"
            if txt_to_matrix(filename) is not None:
                nums.append(txt_to_matrix(filename).shape[0])

x = [i for i in range(1, len(nums) + 1)]
plt.plot(x[::4], nums[::4], linestyle='-', linewidth=1.5)
plt.xlabel("# Hours Since 2020-01-21-22")
plt.ylabel("# Sampled Tweets")
plt.savefig("/Users/mashazhou/PycharmProjects/COVID-19/COVID-19-TweetIDs-samples/figures/by_hour.eps",
            bbox_inches = 'tight')
plt.show()
