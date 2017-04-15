Collects english language tweets related to depression

## Installation

* `pip install -r packages.txt`

## Setup
* Sign up for a Twitter [developer account](https://dev.twitter.com/).
* Create an application [here](https://apps.twitter.com/).
* Set the values for the following in the `twitter_keys.py` file.  You can get these values from the app you created:
CONSUMER_KEY = "<YOUR CONSUMER KEY>"
CONSUMER_SECRET = "<CONSUMER SECRET KEY>"

ACCESS_TOKEN = "<ACCESS_TOKEN>"
ACCESS_TOKEN_SECRET = "<ACCESS TOKEN SECRET>"

## Usage

* `python CollectTweets.py` to scrape.  Use `Ctrl + C` to stop.
* Tweets are dumped to depression_tweets.csv file in the same location as script