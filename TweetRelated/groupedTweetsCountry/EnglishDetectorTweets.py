# This file contains the code to store only english tweets so it is easier to analyze.
# The english tweets are stored in groupedTweetsCountry/tweetContent.csv

from langdetect import detect
import pandas as pd

# Read new tweets file
complete_df = pd.read_csv("../NewTweetInfo.csv", skip_blank_lines=True, error_bad_lines=False)


def store_english_tweets():
    # Read the required columns in the dataframe
    df = complete_df[["Tweet_time", "Tweet_id", "UserId", "UserLocation", "Tweet_content"]]

    df['Lang'] = ''

    # Iterate over tweets and store language in Lang column
    for index, row in df.iterrows():
        try:
            row['Lang'] = detect(row['Tweet_content'])
        except:
            pass

    df[df['Lang'] == 'en'].to_csv("tweetContent12.csv")


store_english_tweets()
