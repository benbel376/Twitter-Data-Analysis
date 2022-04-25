import json
import pandas as pd
from textblob import TextBlob

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
        created_at = []
        for items in self.tweets_list:
            created_at.append(items['created_at'])
        return created_at
    
    # a function that extracts the source variable and returns a list of html hyperlink reference strings
    def find_source(self)->list:
        source = []
        for items in self.tweets_list:
            source.append(items['source'])
        return source
    
    # a function that extracts the text variable and returns a list of tweet strings
    def find_full_text(self)->list:
        text = []
        for items in self.tweets_list:
            text.append(items['text'])
        return text

    # a function that inserts the extracted value lists for each variable into a dataframe.       
    def get_tweet_df(self, save=False)->pd.DataFrame:
        """required column to be generated you should be creative and add more features"""
        
        columns = ['created_at', 'source', 'original_text']
        
        created_at = self.find_created_time()
        source = self.find_source()
        text = self.find_full_text()

        data = zip(created_at, source, text)
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

    