import pandas as pd
import re
class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Data cleaning in Action...!!!')
        
    def drop_unwanted_column(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        unwanted_rows = df[df['retweet_count'] == 'retweet_count' ].index
        df.drop(unwanted_rows , inplace=True)
        df = df[df['polarity'] != 'polarity']

        print('Unwanted_columns successfully removed')
        
        return df
    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows from selected columns where duplicates are not expected.
        """
        df.drop_duplicates(['screen_name','original_text','created_at'],keep="first")

        print('Duplicate rows successfully removed')
        
        return df
    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """
        df['created_at'] = pd.to_datetime(df['created_at'])
        
        df = df[df['created_at'] >= '2020-12-31' ]

        print('Strings successfully converted to datetime object')
        
        return df
    
    def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        
        df['polarity'] = pd.to_numeric(df['polarity'])
        df['favourites_count'] = pd.to_numeric(df['favourites_count'])
        df['subjectivity'] = pd.to_numeric(df['subjectivity'])
        df['retweet_count'] = pd.to_numeric(df['retweet_count'])
        df['friends_count'] = pd.to_numeric(df['friends_count'])
        df['followers_count'] = pd.to_numeric(df['followers_count'])
       
        print('Strings successfully converted to numeric object')
        
        return df
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        
        df = df[df['language']=='en']

        print('Non-English languages succesfully removed')
        
        return df

    def get_source_name(self, source: str):
        """
        returns device name from source text
        """
        res = re.split('<|>', source)[2].strip()
        
        return res  