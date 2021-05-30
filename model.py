import pandas
ds = pandas.read_csv('Salary_Data.csv')
ds.columns
ds.info()
x = ds['YearsExperience'].values.reshape(30,1)
type(x)
x.shape
y = ds['Salary']
from sklearn.linear_model import LinearRegression
model = LinearRegression() 
model.fit(x , y)
model.coef_
model.predict([[ 1.1 ]] )
print(f"The result is:{model.predict([[ 1.1 ]] )}")