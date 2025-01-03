from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

# Preprocess the tweet
def preprocess_tweet(tweet):
    tweet_words = []
    for word in tweet.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        elif word.startswith('http'):
            word = 'http'
        tweet_words.append(word)
    return ' '.join(tweet_words)

# Load model and tokenizer
roberta = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative', 'Neutral', 'Positive']

def sentiment_analysis():
    # Get user input
    tweet = input("Enter a tweet or sentence: ")

    # Preprocess the input
    tweet_proc = preprocess_tweet(tweet)

    # Perform sentiment analysis
    encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
    output = model(**encoded_tweet)

    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    # Print sentiment scores
    print("\nSentiment Analysis Results:")
    for i in range(len(scores)):
        l = labels[i]
        s = scores[i]
        print(f"{l}: {s:.4f}")

if __name__ == "__main__":
    sentiment_analysis()
