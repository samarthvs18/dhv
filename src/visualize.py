import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def plot_sentiment_bar(df, filename="sentiment_plot.png"):
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 6))
    sns.countplot(x="Sentiment", data=df)
    plt.title("Tweet Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Tweets")
    plt.savefig(filename)
    plt.close()


def show_wordcloud(df):
    text = " ".join(t for t in df["Cleaned_Tweet"])
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
