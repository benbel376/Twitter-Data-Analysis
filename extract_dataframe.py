import json
import pandas as pd
from textblob import TextBlob
import re

def read_json(json_file: str)->list:
    """
    json file reader to open and read json files into a list
    Args:
    -----
    json_file: str - path of a json file
    
    Returns
    -------
    length of the json file and a list of json
    """
    
    tweets_data = []
    for tweets in open(json_file,'r'):
        tweets_data.append(json.loads(tweets))
    
    
    return len(tweets_data), tweets_data

class TweetDfExtractor:
    """
    this function will parse tweets json into a pandas dataframe
    
    Return
    ------
    dataframe
    """
    def __init__(self, tweets_list):
        
        self.tweets_list = tweets_list


    # a function that extracts the created_at variable and returns a list of date strings
    def find_created_time(self)->list:
        created_at = [] # aholds a list of all created time and date
        for items in self.tweets_list:
            created_at.append(items['created_at'])
        return created_at
    
    # a function that extracts the source variable and returns a list of html hyperlink reference strings
    def find_source(self)->list:
        source = [] # a list that holds hyper link references
        for items in self.tweets_list:
            source.append(items['source'])
        return source
    
    # a function that extracts the text variable and returns a list of tweet strings
    def find_full_text(self)->list:
        cl_text = [] # holds the clean text
        uncl_text = [] # original text
        for items in self.tweets_list:
            uncl_text.append(items['text'])
            cl_text.append(re.sub("^RT.*:","",items['text']))
        
        return cl_text, uncl_text


    # a function that extracts polarity and subjectivity from the list of tweet strings.
    def find_sentiments(self, text: list)->list:
        polarity = [] # contains the polarity values from the sentiment analysis.
        self.subjectivity = [] # contains the subjectivity values from the sentiment analysis.
        for items in text:
            self.subjectivity.append(TextBlob(items).sentiment.subjectivity)
            polarity.append(TextBlob(items).sentiment.polarity)
        
        return polarity, self.subjectivity
    
    
    # a function that extracts authors name.
    def find_screen_name(self)->list:
        screen_name = [] # list of screen names.
        for items in self.tweets_list:
            screen_name.append(items['user']['screen_name'])
        
        return screen_name

    # a function that extracts the language used in the tweet.
    def find_lang(self)->list:
        lang = [] # list of languages
        for items in self.tweets_list:
            lang.append(items['lang'])
        
        return lang

    # a function that extracts the number of retweets.
    def find_retweet_count(self)->list:
        retweet_count = [] # list of number of retweets.
        for items in self.tweets_list:
            retweet_count.append(items['retweet_count'])
        
        return retweet_count

    # a function that extracts the hashtags used in the tweet.
    def find_hashtags(self)->list:
        hashtags = [] # list of hashtags
        for items in self.tweets_list:
             hashtags.append(items['entities']['hashtags'])
        
        return hashtags

    # a function that extracts the number of friends.
    def find_friends_count(self)->list:
        friends_count = [] # list of number of friends.
        for items in self.tweets_list:
            friends_count.append(items['user']['friends_count'])
        
        return friends_count

    # a function that extracts the statuses count in the tweet.
    def find_statuses_count(self)->list:
        statuses = [] # list of statuses
        for items in self.tweets_list:
            statuses.append(items['user']['statuses_count'])
        
        return statuses

    # a function that extracts the number of friends.
    def find_followers_count(self)->list:
        followers_count = [] # list of number of followers.
        for items in self.tweets_list:
            followers_count.append(items['user']['followers_count'])
        
        return followers_count


    # a function that extracts the mentions in the tweet.
    def find_mentions(self)->list:
        mentions = [] # list of mentions
        for items in self.tweets_list:
             mentions.append(items['entities']['user_mentions'])
        
        return mentions

    # a function that extracts sensitivity status.
    def is_sensitive(self)->list:
        sensitivity = [] # list of sensitivity status.
        for items in self.tweets_list:
            sensitivity.append(items['possibly_sensitive'])
        
        return sensitivity


    # a function that inserts the extracted value lists for each variable into a dataframe.       
    def get_tweet_df(self, save=False)->pd.DataFrame:
        """required column to be generated you should be creative and add more features"""
        
        columns = ['created_at', 'source', 'original_text', 'clean_text', 'polarity', 'subjectivity', 'original_author', 'language', 'retweet_count', 'friends_count', 'hashtags', 'statuses', 'followers_count', 'possibily_sensitive', 'user_mentions']
        created_at = self.find_created_time()
        source = self.find_source()
        clean_text, text = self.find_full_text()
        polarity, subjectivity = self.find_sentiments(clean_text)
        screen_name = self.find_screen_name()
        lang = self.find_lang()
        retweet_count = self.find_retweet_count()
        friends_count = self.find_friends_count()
        hashtags = self.find_hashtags()
        statuses_count = self.find_statuses_count()
        followers_count = self.find_followers_count()
        mentions = self.find_mentions()
        sensitive = self.is_sensitive()

        data = zip(created_at, source, text, clean_text, polarity, subjectivity, screen_name, lang, retweet_count, friends_count, hashtags, statuses_count, followers_count, sensitive, mentions)
        df = pd.DataFrame(data=data, columns=columns)

        if save:
            df.to_csv('processed_tweet_data.csv', index=False)
            print('File Successfully Saved.!!!')
        
        return df

                
if __name__ == "__main__":
    # required column to be generated you should be creative and add more features
    
    _, tweet_list = read_json("E:/10/Twitter-Data-Analysis/data/Economic_Twitter_Data.json")
    tweet = TweetDfExtractor(tweet_list)
    tweet_df = tweet.get_tweet_df(True) 

    # use all defined functions to generate a dataframe with the specified columns above

    