# This file contains code for 2 operations:
# 1. Add country column to ../TweetRelated/CleanedTweetsInfo.csv which will be further used for sentiment analysis
# 2. Plot number of Tweets vs country graph


import pandas as pd
import matplotlib.pyplot as plt


def get_tweets_country():
    df_country = pd.read_csv('tweetsCountry.csv', delimiter="\t", header=None)

    df_country.columns = ['Geo_Place']

    df_country['Geo_Country'] = None

    for index, row in df_country.iterrows():
        place_list = row['Geo_Place'].rsplit(',', 1)
        row['Geo_Country'] = place_list[len(place_list) - 1]
    return df_country


def get_user_location_country_map(df_country):
    df_unique_locations = pd.read_csv('uniqueLocations.csv', delimiter="\t", header=None)
    df_unique_locations.columns = ['Tweet_Place']

    # Create new dataframe of Tweet_Place and Geo_Country
    tweet_country_df = pd.DataFrame(columns=['Tweet_Place', 'Geo_Country'])
    tweet_country_df['Tweet_Place'] = df_unique_locations['Tweet_Place']
    tweet_country_df['Geo_Country'] = df_country['Geo_Country']
    return tweet_country_df


def add_country_column(tweet_country_df):
    cleaned_tweets_info_df = pd.read_csv('../CleanedTweetsInfo.csv')

    tweet_info_country_merge_df = pd.merge(cleaned_tweets_info_df, tweet_country_df, how='left', left_on='UserLocation',
                                           right_on='Tweet_Place')

    tweet_info_country_merge_df.drop(['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1'], inplace=True, axis=1)
    tweet_info_country_merge_df.dropna(inplace=True, axis=0)

    print(tweet_info_country_merge_df)

    # The below line is commented in order to avoid rewriting of file. Uncomment for creating new file
    # tweet_info_country_merge_df.to_csv("../TweetRelated/CleanedTweetsInfo.csv")

    return tweet_info_country_merge_df


def plot_tweet_count_countries(tweet_info_country_merge_df):
    grouped_df = tweet_info_country_merge_df.groupby('Geo_Country')['Tweet_content'].count().reset_index()
    grouped_df['Geo_Country'] = grouped_df[grouped_df != 'None']
    grouped_df.dropna(inplace=True)

    ############################################################################
    ax = grouped_df.plot(x=grouped_df.columns[0], y=grouped_df.columns[1])
    ax.set_ylabel("Number of Tweets")
    ax.set_xlabel("Countries")
    plt.show()


# Function calls
df_country = get_tweets_country()
user_location_country_df = get_user_location_country_map(df_country)
tweet_info_country_merge_df = add_country_column(user_location_country_df)

# Plot graph of number of tweets vs countries
plot_tweet_count_countries(tweet_info_country_merge_df)
