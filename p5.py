import numpy as np
import pandas as pd

dtype = np.dtype([
    ("area", "U100"),
    ("date", "M8[D]"),
    ("hours", "f4"),
    ("slides", "U10")  
])

lectures = np.array([
    ("Introduction to Python", "2023-10-01", 2, 15),
    ("Introduction to Python", "2023-10-01", 2, 15),
    ("Introduction to Python", "2023-10-01", 2, 15),
    ("Data Science Basics", "2023-10-05", 3, "N/A"),
    ("Machine Learning Overview", "2023-10-10", 4, 20),
    ("Deep Learning Techniques", "2023-10-15", 3, 25),
    ("AI Ethics", "2023-10-20", 1.5, "N/A")

],dtype=dtype)

df =pd.DataFrame(lectures)

df.groupby("area")
#print(df)
print(lectures)

totalH=df['hours'].sum()
print('Total of hours:',totalH)

totalS=df['slides'].sum()
print('Total of slides:',totalS)

unique=np.unique(lectures['area'])

for u in unique:
    print(u)
    print('\n')
    print(lectures[lectures['area']==u])
    #print(np.sum(lectures[lectures['area']==u]),['hours'])
    print(np.sum(lectures[lectures['area']==u]['hours']))
    #print(np.sum(lectures[lectures['area']==u]['slides']))
