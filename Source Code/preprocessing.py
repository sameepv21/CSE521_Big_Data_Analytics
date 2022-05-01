pip install texthero

from google.colab import drive

drive.mount('/content/gdrive')

import os
os.chdir("/content/gdrive/MyDrive")
!ls

import texthero as hero
import pandas as pd

df=pd.read_csv("/content/gdrive/MyDrive/combined_csv.csv")

df

df.drop(df.columns[[-1,-2,-3,-4]], axis=1, inplace=True)
df

from texthero import preprocessing

custom_pipeline = [preprocessing.fillna
                   , preprocessing.lowercase
                   , preprocessing.remove_digits
                   , preprocessing.remove_punctuation
                   , preprocessing.remove_diacritics
                   , preprocessing.remove_whitespace
                   , preprocessing.stem]
df['Name'] = hero.clean(df['Name'], custom_pipeline)

hero.top_words(df["Text"].pipe(hero.clean))

from texthero import stopwords
default_stopwords = stopwords.DEFAULT
#add a list of stopwords to the stopwords
custom_stopwords = default_stopwords.union(set(["co","https","rt","long", "made"]))
#Call remove_stopwords and pass the custom_stopwords list
df['Text'] = hero.remove_stopwords(df['Text'], custom_stopwords)

tw = hero.visualization.top_words(df["Text"].pipe(hero.clean)).head(10)
tw.plot.bar()
tw.head(10)



hero.wordcloud(df["Text"].pipe(hero.clean))

#Add pca value to dataframe to use as visualization coordinates
df['pca'] = (
            df['Text']
            .pipe(hero.tfidf)
            .pipe(hero.pca)
   ) 
#Add k-means cluster to dataframe 
df['kmeans'] = (
            df['Text']
            .pipe(hero.tfidf)
            .pipe(hero.kmeans)
   )
df.head()

#generate scatter plot
hero.scatterplot(df, 'pca', color = 'kmeans', hover_data=['Text '] )

df.to_csv('intlstud.csv',index=False)
