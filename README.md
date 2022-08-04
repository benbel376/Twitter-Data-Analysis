# Twitter-Data-Analysis

It is an analysis done on data extracted from Twitter based on chosen hashtags. The tweets focus on the war between Ukraine and Russia as well as global inflation rates.

## Usage
1. Docker(Recommended)

You need to have docker
```
   1. git clone https://github.com/benbel376/Twitter-Data-Analysis.git
   2. Extract the file
```
```python
cd Twitter-Data-Analysis
docker-compose up
```
2. Manual build
   Run the extract and clean modules
```python
python extract_dataframe.py
python clean_tweets_dataframe.py
```
```python
pip3 install -r requirements.txt
streamlit run app.py
```

    This will up a Postgres database on local pc and connect with streamlit app

## Test
To test the methods written in the modules use the pytest package and run:
```python
pytest
```
## Usage


![image](https://user-images.githubusercontent.com/44437166/182877191-96ede8ac-7cb0-42aa-b11e-9a26a1db6a54.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
