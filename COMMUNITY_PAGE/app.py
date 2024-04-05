from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

app = Flask(__name__)

comments_data = []  

roberta = "cardiffnlp/twitter-roberta-base-sentiment"
sentiment_model = AutoModelForSequenceClassification.from_pretrained(roberta)
sentiment_tokenizer = AutoTokenizer.from_pretrained(roberta)
sentiment_labels = ['Negative', 'Neutral', 'Positive']

@app.route('/')
def index():
    return render_template('community.html', comments=comments_data)

@app.route('/add_comment', methods=['POST'])
def add_comment():
    name = request.form.get('name')
    comment_text = request.form.get('comment')

    sentiment = analyze_sentiment(comment_text)


    comments_data.append({'name': name, 'comment': comment_text, 'sentiment': sentiment})

    
    save_comments_to_excel()

    return redirect(url_for('index'))

def analyze_sentiment(text):
    tweet_words = []
    for word in text.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        elif word.startswith('http'):
            word = "http"
        tweet_words.append(word)
    tweet_proc = " ".join(tweet_words)

    
    encoded_tweet = sentiment_tokenizer(tweet_proc, return_tensors='pt')
    output = sentiment_model(**encoded_tweet)

    scores = output.logits[0].detach().numpy()
    scores = softmax(scores)

    
    sentiment_index = scores.argmax()
    sentiment = sentiment_labels[sentiment_index]

    return sentiment

def save_comments_to_excel():
    df = pd.DataFrame(comments_data)
    df.to_excel(r"C:\Users\sujatha\COMMUNITY_PAGE\Data.xlsx", index=False)
    


if __name__ == '__main__':
    app.run(debug=True)
