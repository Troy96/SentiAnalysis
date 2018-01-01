#import TextBlob
from textblob import TextBlob

soul = input("Insert the text for sentiment analysis")

body=TextBlob(soul)

#returns the sentiment of text,
#value between -1.0 to 1.0

sentiment=body.sentiment.polarity

print(sentiment)

#positve value represents that the sentiment is positive else otherwise.