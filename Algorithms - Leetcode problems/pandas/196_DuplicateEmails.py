import pandas as pd

df = pd.DataFrame({'id':['1','2','3'],'email':['john@example.com','bob@example.com','john@example.com']},index=[0,1,2])
def solution(df):
    df.sort_values(by='id',ascending=True,inplace=True)

    mask = df['email'].duplicated(keep='first')
    df = df.loc[mask==False,:]
    return df

z = solution(df)
print(z)