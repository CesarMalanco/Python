# Author: reDragonCoder
# Last update: 21/11/2024

import tweepy

# Access to Twitter account (add here your Twitter API keys)
bearer_token='' 
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''

# Create a client object for API v2
client=tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Create an API object
auth=tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api=tweepy.API(auth)

# Functions
def profile_image(filename):
    try:
        api.update_profile_image(filename)  
        print("Profile image updated successfully...")
    except tweepy.TweepyException as e:
        print(f"Error updating profile image: {e}")

def update_profile_info(api, name, url, location, description):
    try:
        api.update_profile(
            name=name,
            url=url,
            location=location,
            description=description
        )
        print("Profile info updated successfully....")
    except tweepy.TweepyException as e:
        print(f"Error updating profile info: {e}")

def post_tweet(text):
    try:
        client.create_tweet(text=text)
        print("Tweet uploaded successfully....")
    except tweepy.TweepyException as e:
        print(f"Error uploading tweet: {e}")

def upload_media_and_tweet(text, filename):
    try:
        media=api.media_upload(filename)
        media_id=media.media_id_string
        client.create_tweet(text=text, media_ids=[media_id])
        print("Tweet posted successfully!")
    except tweepy.TweepyException as e:
        print(f"Error uploading tweet: {e}")



#-----------------TESTING ZONE-----------------       
# Test updating profile image
#profile_image('Pepe.jpg')

# Test updating profile info
#update_profile_info(api, "BestBot", "https://www.youtube.com/watch?v=LlgWqcHXD8w", "The Matrix", "Hey! I'm a bot now")

# Test posting a tweet
#post_tweet("Hello World! I'm using Tweepy!")

# Test uploading media and tweeting
#upload_media_and_tweet("Check out this image!", "Bitcoin.jpg")

