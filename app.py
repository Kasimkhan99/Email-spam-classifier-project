import streamlit as st
import pickle
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string

ps=PorterStemmer()


def transform_data(text):
    text=text.lower()

    text=nltk.word_tokenize(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)

    text=y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text=y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)
model=pickle.load(open('train_model\\spam_model .pkl','rb'))
tfif=pickle.load(open('train_model\\vectorizer.pkl','rb'))


st.title("Email/sms spam classifier")

input_sms=st.text_area("Enter your Email/sms")

if st.button('predict'):
    transform_sms=transform_data(input_sms)
    vector_input=tfif.transform([transform_sms])
    result=model.predict(vector_input)[0]

    if result==1:
        st.header("spam")
    else:
        st.header("not spam")

