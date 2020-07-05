import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia=SentimentIntensityAnalyzer()

df_news1 = pd.read_json('headlines07.json',convert_dates=['Date'])
df_news1 = pd.DataFrame.from_records(df_news1['news'])

filenames = ['headlines08.json','headlines09.json','headlines10.json','headlines11.json','headlines12.json','headlines13.json','headlines14.json','headlines15.json','headlines16.json','headlines17.json','headlines18.json','headlines19.json']

for filename in filenames:
    df_news2 = pd.read_json(filename,convert_dates=['Date'])
    df_news2 = pd.DataFrame.from_records(df_news2['news'])
    df_news1=df_news1.append(df_news2,ignore_index = True)

df_merged = df_news1
df_merged['compound']=''
df_merged['neg']=''
df_merged['neu']=''
df_merged['pos']=''

for index,sentence in enumerate(df_merged['headlines']):
    ps=sia.polarity_scores(sentence)
    df_merged['compound'][index]=ps['compound']
    df_merged['neg'][index]=ps['neg']
    df_merged['neu'][index]=ps['neu']
    df_merged['pos'][index]=ps['pos']

final_df = df_merged[['Date','compound','neg','neu','pos']]
print(final_df.head())
final_df.to_csv('sentiment_result.csv',index=False)