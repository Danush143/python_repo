import pandas as pd
from sqlalchemy import text,create_engine
import oracledb

dms=oracledb.makedsn('orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com', '1521', service_name='orcl')
user='deMTIET_venkatdanush'
password='deMTIET_venkatdanush'
engine=create_engine(f'oracle+oracledb://{user}:{password}@{dms}')
conn=engine.connect()

data_frame=pd.read_csv(r'C:\Users\viral\Desktop\ds 2025\Student Depression Dataset.csv')
# print(data_frame)
avg_age=data_frame['Age'].mean()
# print(avg_age)
srinagar_people=data_frame[data_frame['City']=='Srinagar']
# print(len(srinagar_people))
sd_max=data_frame['Sleep Duration'].max()
sd_min=data_frame['Sleep Duration'].min()
# print(sd_max)
# print(sd_min)
ss=data_frame[(data_frame['Study Satisfaction']<=2) & (data_frame['CGPA']>7)]
# print(ss)
ss1=data_frame[(data_frame['Gender']=='Male') & (data_frame['Depression']>50)]
# """'''07- Group the dataset by Gender and calculate the average depression score for each group. '''
# '''08- Number of people are having suicidal thoughts '''
# '''09- find out how many people are graduated in LLB and avg of their cgpa ''' """
# print(ss1)
ss2=data_frame[data_frame['Dietary Habits']=='Unhealthy']
# print(ss2)
ss3=data_frame[data_frame['Gender']=='Female']
ss4=data_frame[data_frame['Gender']=='Male']
ss5=ss3['Depression'].mean()
ss6=ss4['Depression'].mean()
# print(ss5)
# print(ss6)
st=data_frame[data_frame['Have you ever had suicidal thoughts ?']=='Yes']
# print(len(st))
ss7=data_frame[data_frame['Degree']=='LLB']
# print(len(ss7))
ss8=ss7['CGPA'].mean()
# print(ss8)
# '''10- display all the distinct city names '''
# '''11- find out how who has the maximum work/study hours and display with their cgpa '''
# '''12- display the gender wise average age '
city_names=data_frame['City'].unique()
# print(city_names)
sh_max=data_frame['Work/Study Hours'].idxmax()
print(data_frame.loc[sh_max])
cgpa_x=data_frame.loc[sh_max,'CGPA']
print(cgpa_x)
ge1=ss3['Age'].mean()
ge2=ss4['Age'].mean()
# print('female average age',ge1)
# print('male average age',ge2)




