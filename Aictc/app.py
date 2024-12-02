from flask import Flask, render_template, request # type: ignore
from sentiment_analysis import analyze_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = ""
    if request.method == 'POST':
        user_input = request.form['text']
        sentiment = analyze_sentiment(user_input)
    return render_template('index.html', sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)