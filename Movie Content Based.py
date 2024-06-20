#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import ast


# In[4]:


movies= pd.read_csv('tmdb_5000_movies.csv')
credits= pd.read_csv('tmdb_5000_ credits.csv')


# In[5]:


movies.head(10)


# In[6]:


credits.head(10)


# In[7]:


movies = movies.merge(credits, on ='title') #merging both datasets


# In[8]:


movies


# In[9]:


# dropping the unwanted columns like budget, homepage, original language(95% is english), production company, 
#production country, release date, runtime, spoken languages,status,tagline,original title, vote average and count, 
#movie_id


# In[10]:


movies =  movies[['id','title','overview','genres','keywords','cast','crew']]


# In[11]:


movies


# In[12]:


movies.isnull().sum()


# In[13]:


movies.dropna(inplace=True)


# In[14]:


movies.drop_duplicates(inplace=True)


# In[15]:


movies.duplicated().sum()


# In[16]:


movies.head(10)


# In[17]:


movies.iloc[0]


# In[18]:


movies.iloc[0].genres


# In[19]:


def converting(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L


# In[20]:


movies['genres']=movies['genres'].apply(converting)


# In[21]:


movies['genres']


# In[22]:


movies.head()


# In[23]:


#similarly for keywords
movies['keywords']= movies['keywords'].apply(converting)


# In[24]:


movies['keywords']


# In[25]:


# for cast we take top 3 actors that is first 3 dictionaries
def converting_actor(obj):
    L=[]
    counter=0
    for i in ast.literal_eval(obj):
        if counter !=3:
            L.append(i['name'])
            counter+=1
        else:
            break 
        L.append(i['name'])
    return L


# In[26]:


movies['cast']=movies['cast'].apply(converting_actor)


# In[27]:


movies.head()


# In[28]:


# for crew we take director alone
def converting_crew(obj):
    L=[]
    for i in ast.literal_eval(obj):
        if i['job']=="Director" :           
            L.append(i['name'])
            break
    return L


# In[29]:


movies['crew']=movies['crew'].apply(converting_crew)


# In[30]:


movies.head()


# In[31]:


movies['overview']=movies['overview'].apply(lambda x:x.split())


# In[32]:


movies.head()


# In[33]:


# we have to combine words as "CHRISTOPHER NOLAN" is one persons name, 
#there might be some other entity having the same christopher, or nolan so we have to merge the name
# similarly for genre, keyword,cast,crew


# In[34]:


def remove_space(li):
    li=[]
    for i in li:
        li.append(i.replace(" "," "))
    return li

    


# In[35]:


movies['cast'] = movies['cast'].apply(remove_space)


# In[36]:


movies['genres'] = movies['genres'].apply(remove_space)


# In[37]:


movies['keywords'] = movies['keywords'].apply(remove_space)


# In[38]:


movies['crew'] = movies['crew'].apply(remove_space)


# In[39]:


movies['tags'] = movies['overview'] + movies['crew'] + movies['cast'] + movies['genres'] 


# In[40]:


# since now we have tags to simplify this we create a new df


# In[41]:


df= movies[['id','title','tags']]


# In[42]:


df['tags'].apply(lambda x:" ".join(x))


# In[43]:


df['tags'][0]


# In[44]:


df['tags'][1]


# In[45]:


# now we need to lowercase everything

df['tags'] = df['tags'].apply(lambda x: [tag.lower() for tag in x] if isinstance(x, list) else x)


# In[46]:


df['tags'].head()


# In[73]:


from sklearn.feature_extraction.text import CountVectorizer


# In[71]:





# In[74]:


def custom_preprocessor(tags):
    if isinstance(tags, list):
        return ' '.join(tag.lower() for tag in tags)
    else:
        return str(tags).lower()


# In[101]:


cv = CountVectorizer(max_features=5000, stop_words='english', preprocessor=custom_preprocessor)


# In[102]:


x = cv.fit_transform(df['tags']).toarray()


# In[103]:


cv.fit_transform(df['tags']).toarray().shape


# In[104]:


cv.get_feature_names()


# In[ ]:


# we need to modify, ["adventure","adventures","adventurous"] into ["adventure","adventure","adventure"]


# In[85]:


get_ipython().system('pip install nltk')


# In[86]:


import nltk


# In[87]:


from nltk.stem.porter import PorterStemmer
ps= PorterStemmer()


# In[92]:


def stem_words(word_list):
    stemmed_words = [ps.stem(word) for word in word_list]
    return " ".join(stemmed_words)


# In[96]:


df['tags'] = df['tags'].apply(stem_words)


# In[97]:


df['tags']


# In[99]:


x = cv.fit_transform(df['tags']).toarray()


# In[107]:


cv.get_feature_names()


# In[108]:


from sklearn.metrics.pairwise import cosine_similarity


# In[111]:


similarity = cosine_similarity(x)


# In[112]:


similarity[1]


# In[113]:


sorted(list(enumerate(similarity[0])),reverse=True,key=lambda x:x[1])[1:6]


# In[123]:


def recommending(mov):
    mov_index= df[df['title'] == mov].index[0]
    distance=similarity[mov_index]
    
    mov_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    
    for i in mov_list:
        print(df.iloc[i[0]].title)
    
    


# In[126]:


recommending("Spider-Man 3")


# In[127]:


recommending("Tangled")


# In[128]:


recommending("The Dark Knight Rises")


# In[133]:


recommending("Iron Man")


# In[143]:


recommending("Ice Age")


# In[142]:


recommending("Life of Pi")


# In[135]:


import pickle

#pickle.dump(df,open('movies.pkl','wb'))


# In[137]:


pickle.dump(df.to_dict(),open('movies.pkl','wb'))


# In[138]:


pickle.dump(similarity,open('similarity.pkl','wb'))


# In[ ]:




