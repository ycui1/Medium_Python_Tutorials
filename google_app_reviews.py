from google_play_scraper import app

import pandas as pd

import numpy as np


from google_play_scraper import Sort, reviews_all


us_reviews = reviews_all(
    'co.digithera.v2.quitgenius',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
)

df_busu = pd.DataFrame(np.array(us_reviews),columns=['review'])


df_busu = df_busu.join(pd.DataFrame(df_busu.pop('review').tolist()))


df_busu.head()

{}.get()