# https://towardsdatascience.com/multi-class-text-classification-with-scikit-learn-12f1e60e0a9f

#create dataframe
import pandas as pd
df = pd.DataFrame({'Category': ['General','Loan','Passbook'], 
               'Complaint_Details': ['General Bank is not opend, really bad','Bank This is the second sentence', 'This is the third sentence']})
         
#TfIdVectorizer         
from sklearn.feature_extraction.text import TfidfVectorizer
v = TfidfVectorizer(sublinear_tf=True, norm='l2', encoding='latin-1', stop_words='english')
x = v.fit_transform(df['Complaint_Details'])
features = x.toarray()
labels = df.Category
features.shape


x.toarray()
