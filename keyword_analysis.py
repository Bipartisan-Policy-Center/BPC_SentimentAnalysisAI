import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
# matplotlib inline

# Privacy Legislation keywords
privacy_df = pd.read_csv(r"/Users/rachaelharris/Desktop/computer science/work-stuffs/bipartisanpolicy/sentiment analysis rerun/sentiment.csv", index_col=0, encoding= 'unicode_escape')

# Join all keywords together:
keyword1 = " ".join(review for review in privacy_df.keyword1)
keyword2 = " ".join(review for review in privacy_df.keyword2)
keyword3 = " ".join(review for review in privacy_df.keyword3)
keyword4 = " ".join(review for review in privacy_df.keyword4)
keyword5 = " ".join(review for review in privacy_df.keyword5)
text = keyword1 + keyword2 + keyword3 + keyword4 + keyword5

# Create and generate a word cloud image:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("/Users/rachaelharris/Desktop/computer science/work-stuffs/bipartisanpolicy/sentiment analysis rerun/src/keyword.png", format="png")
