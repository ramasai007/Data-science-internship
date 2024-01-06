#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# **1. How many ".csv" files are available in the dataset?**

# In[42]:


csv_files=4


# In[10]:


data=pd.read_csv(r"C:/Users/kuret\Downloads\movie_data\movies.csv")
data


# In[5]:


df=data.copy()


# In[6]:


df


# **2. What is the shape of "movies.csv"?**

# In[12]:


data=pd.read_csv(r"C:\Users\kuret\Downloads\movie_data\movies.csv")
df=data.copy()
df.shape


# In[15]:


ratings=pd.read_csv(r"C:\Users\kuret\Downloads\movie_data\ratings.csv")
ratings


# **3. What is the shape of "ratings.csv"?**

# In[ ]:


ratings.shape


# In[16]:


tags=pd.read_csv(r"C:\Users\kuret\Downloads\movie_data\tags.csv")
tags


# In[17]:


links_df=pd.read_csv(r"C:\Users\kuret\Downloads\movie_data\links.csv")
links_df


# **4. How many unique "userId" are available in "ratings.csv"?**

# In[18]:


ratings['userId'].nunique()


# **5. Which movie has recieved maximum number of user ratings?**

# In[19]:


rating_movie = pd.merge(df,ratings, how = 'inner', on = ['movieId'])


# In[20]:


rating_movie.head()


# In[21]:


rating_movie.groupby('title')['rating'].count().idxmax()


# **6. Select all the correct tags submitted by users to "Matrix, The (1999)" movie?**

# In[22]:


tag_movies = pd.merge(df,tags, how = 'inner', on = ['movieId'])


# In[23]:


tag_movies.head()


# In[24]:


tag_movies[tag_movies["title"]=="Matrix, The (1999)"]


# **7. What is the average user rating for movie named "Terminator 2: Judgment Day (1991)"?**

# In[25]:


avg_rating_movies = pd.merge(df,ratings, how = 'inner', on = ['movieId'])


# In[26]:


avg_rating_movies.head()


# In[27]:


avg_rating_movies[avg_rating_movies['title'] == 'Terminator 2: Judgment Day (1991)']["rating"].mean()


# **8. How does the data distribution of user ratings for "Fight Club (1999)" movie looks like?**

# In[28]:


sns.histplot(data=rating_movie[rating_movie['title']=="Fight Club (1999)"]['rating'],kde=True)


# **IMPORTANT NOTE 1 🟢
# Now that you have a good enough understanding of the given data, apply the "Mandatory Operation" given below before solving any of the following questions.
# 
# Mandatory Operations:
# 1. Group the user ratings based on movieId and apply aggregation operations like count and mean on ratings. 
# 2. Apply inner join on dataframe created from movies.csv and the grouped df from step 1.
# 3. Filter only those movies which have more than 50 user ratings (i.e. > 50).
# 
# Above steps will make sure that your data contains only those movies which has recieved more than 50 user ratings.**

# **Group the user ratings based on movieId and apply aggregation operations like count and mean on ratings.**

# In[29]:


grouped_ratings = ratings.groupby('movieId').agg({'rating': ['count', 'mean']}).reset_index()

grouped_ratings.columns = ['movieId', 'rating_count', 'rating_mean']


# In[30]:


grouped_ratings


# In[31]:


merged_df = pd.merge(df,grouped_ratings,how='inner',on=['movieId'])


# In[32]:


merged_df.head(10)


# **Filter only those movies which have more than 50 user ratings (i.e. > 50).**

# In[33]:


merged_rating = merged_df[merged_df['rating_count'] > 50]
merged_rating


# **9. Which movie is the most popular based on  average user ratings?**

# In[34]:


merged_rating.loc[merged_rating['rating_mean'].idxmax()]


# **10. Select all the correct options which comes under top 5 popular movies based on number of user ratings.**
# 
# Answer this question only after applying the above mentioned "Mandatory Operration".

# In[35]:


merged_rating.sort_values(by='rating_count', ascending=False).head(5)


# **11. Which Sci-Fi movie is "third most popular" based on the number of user ratings?**

# In[36]:


Sci_fi = merged_rating[merged_rating['genres'].str.contains('Sci-Fi')]
Sci_fi.head()


# In[37]:


Sci_fi.sort_values(by='rating_count', ascending=False).head(3)


# **IMPORTANT NOTE 2:**
# You already have a subset of data containing only those movies which has recieved more than 50 user ratings.**
# 
# Using "links.csv", scrape the IMDB reviews of each movie with more than 50 user ratings. "README.md" file contains the required details.
# 
# If you are unable to write the webscraping script yourself, you can request the same by commenting LinkedIn Post.**

# In[45]:


movie_imdb= pd.merge(merged_rating,links_df,on='movieId',how='inner')


# In[46]:


movie_imdb


# **12. Mention the movieId of the movie which has the highest IMDB rating?**

# In[40]:


movie_imdb.sort_values(by='rating_count', ascending=False).head(1)


# In[ ]:





# In[ ]:





# In[ ]:




