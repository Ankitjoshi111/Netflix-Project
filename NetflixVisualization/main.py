import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, d2_absolute_error_score, median_absolute_error, accuracy_score


netflix = pd.read_csv('NetflixVisualization/Netflix.csv')

# seaborn line plot between release_year and imdb score.

sns.lineplot(data=netflix, x="release_year", y="imdb_score")
plt.title('imdb_score of releasing movies yearly')
plt.show()

# seaborn scatter plot between release_year and imdb score.

sns.set(style='whitegrid')
sns.scatterplot(data=netflix, x="release_year", y="imdb_score", color='green')
plt.title('scatterplot between imdb_score of releasing movies yearly')
plt.show()

# seaborn boxen plot between release_year and imdb_score.

sns.boxenplot(data=netflix, x="release_year", y="imdb_score", color='green')
plt.title('boxenplot between imdb_score of releasing movies yearly')
plt.show()

# seaborn joint plot between  release_year and  imdb_score.

sns.jointplot(data=netflix, x="release_year", y="imdb_score", color='red')
plt.show()

# seaborn displot between release_year and imdb_score.

sns.displot(data=netflix, x="release_year", y="imdb_score")
plt.title('displot between imdb_score of releasing movies yearly')
plt.show()

# matplotlib scatter between release_year and imdb score.

plt.scatter(netflix["release_year"], netflix["imdb_score"])
plt.xlabel('release_year')
plt.ylabel('imdb_score')
plt.title('scatter plot of imdb_score of releasing movies yearly')
plt.show()

# matplotlib bar between release year and imdb score.

plt.bar(netflix["release_year"], netflix["imdb_score"])
plt.xlabel('release_year')
plt.ylabel('imdb_score')
plt.title('imdb_score of releasing movies yearly')
plt.show()

# seaborn line plot between runtime and imdb score.

sns.lineplot(data=netflix, x="runtime", y="imdb_score")
plt.title('imdb_score of movies runtime')
plt.show()

# seaborn scatter plot between runtime and imdb score.

sns.set(style='whitegrid')
sns.scatterplot(data=netflix, x="runtime", y="imdb_score", color='green')
plt.title('scatterplot between imdb_score of movies runtime')
plt.show()

# seaborn boxen plot between  runtime and  imdb_score.

sns.boxenplot(data=netflix, x="runtime", y="imdb_score", color='green')
plt.title('boxenplot between imdb_score of movies runtime')
plt.show()

# seaborn joint plot between runtime and imdb_score.

sns.jointplot(data=netflix, x="runtime", y="imdb_score", color='red')
plt.show()

# seaborn displot between runtime and imdb_score.

sns.displot(data=netflix, x="runtime", y="imdb_score")
plt.title('displot between imdb_score of movies runtime')
plt.show()

# seaborn line plot between runtime and imdb_votes.

sns.lineplot(data=netflix, x="runtime", y="imdb_votes")
plt.title('imdb_votes of movies runtime')
plt.show()

# seaborn scatter plot between runtime and imdb_votes.

sns.set(style='whitegrid')
sns.scatterplot(data=netflix, x="runtime", y="imdb_votes", color='green')
plt.title('scatterplot between imdb_votes of movies runtime')
plt.show()

 # seaborn boxen plot between runtime and imdb_votes.

sns.boxenplot(data=netflix, x="runtime", y="imdb_votes", color='green')
plt.title('boxenplot between imdb_votes of movies runtime')
plt.show()

# seaborn joint plot between runtime and imdb_votes.

sns.jointplot(data=netflix, x="runtime", y="imdb_votes", color='red')
plt.show()

# seaborn dis-plot between runtime and imdb_votes.

sns.displot(data=netflix, x="runtime", y="imdb_votes")
plt.title('displot between imdb_votes of movies runtime')
plt.show()

ageCertification = netflix[netflix['age_certification'] == 'R']
print(ageCertification)

runtime = ageCertification[ageCertification['runtime'] >= 80]
imdbScore = runtime[runtime['imdb_score'] >= 7]
# print(imdbScore)

# seaborn line plot between runtime and imdb score.

sns.lineplot(data=imdbScore, x='runtime', y='imdb_score')
plt.title('runtime and imdb score of ageCertification R')
plt.show()

# seaborn scatter plot between runtime and imdb_score.

sns.set(style='whitegrid')
sns.scatterplot(data=imdbScore, x="runtime", y="imdb_score", color='green')
plt.title('scatterplot between imdb_score of movies runtime for ageCertification R')
plt.show()

# seaborn boxen plot between runtime and imdb_score.

sns.boxenplot(data=imdbScore, x="runtime", y="imdb_score", color='green')
plt.title('boxenplot between imdb_score of movies runtime for ageCertification R')
plt.show()

# seaborn joint plot between runtime and imdb_score.

sns.jointplot(data=imdbScore, x="runtime", y="imdb_score", color='red')
plt.show()

# seaborn displot between runtime and imdb_score.

sns.displot(data=imdbScore, x="runtime", y="imdb_score")
plt.title('displot between imdb_score of movies runtime for ageCertification R')
plt.show()

ageCertification = netflix[netflix['age_certification'] == 'TV-MA']
print(ageCertification)

runtime = ageCertification[ageCertification['runtime'] >= 80]
imdbScore = runtime[runtime['imdb_score'] >= 7]
print(imdbScore)

# seaborn line plot between runtime and imdb_score of age_certification TV-MA.

sns.lineplot(data=imdbScore, x='runtime', y='imdb_score')
plt.title('runtime and imdb score of age_certification TV-MA')
plt.show()

# seaborn scatter plot between runtime and imdb_score of age_certification TV-MA.

sns.set(style='whitegrid')
sns.scatterplot(data=imdbScore, x="runtime", y="imdb_score", color='green')
plt.title('scatterplot between imdb_score of movies runtime for age_certification TV-MA')
plt.show()

# seaborn boxen plot between runtime and imdb_score of age_certification TV-MA.

sns.boxenplot(data=imdbScore, x="runtime", y="imdb_score", color='green')
plt.title('boxenplot between imdb_score of movies runtime for age_certification TV-MA')
plt.show()

# seaborn joint plot between runtime and imdb_score of age_certification TV-MA.

sns.jointplot(data=imdbScore, x="runtime", y="imdb_score", color='red')
plt.show()

# seaborn dis plot between runtime and imdb_score of age_certification TV-MA.

sns.displot(data=imdbScore, x="runtime", y="imdb_score")
plt.title('displot between imdb_score of movies runtime for age_certification TV-MA')
plt.show()

runtime = netflix[netflix['runtime'] >= 80]
imdbScore = runtime[runtime['imdb_score'] >= 7]
print(imdbScore['title'].head())

# seaborn line plot between runtime and imdb_score with age_certification.

sns.lineplot(data=imdbScore, x='runtime', y='imdb_score', hue='age_certification')
plt.title('lineplot of runtime and imdb_score ')
plt.show()

# seaborn scatter plot between runtime and imdb_score with age_certification.

sns.scatterplot(data=imdbScore, x='runtime', y='imdb_score', hue='age_certification')
plt.title('scatterplot of runtime and imdb_score ')
plt.show()

# seaborn jointplot between runtime and imdb_score with age_certification.

sns.jointplot(data=imdbScore, x='runtime', y='imdb_score', hue='age_certification')
plt.show()

# seaborn displot between runtime and imdb score with age certification.

sns.displot(data=imdbScore, x='runtime', y='imdb_score', hue='age_certification')
plt.title('displot of runtime and imdb_score ')
plt.show()

# seaborn line plot between runtime and imdb score with type.

sns.lineplot(data=imdbScore, x='runtime', y='imdb_score', hue='type')
plt.title('lineplot of runtime and imdb_score ')
plt.show()

# seaborn scatter plot between runtime and imdb_score with type.

sns.scatterplot(data=imdbScore, x='runtime', y='imdb_score', hue='type')
plt.title('scatterplot of runtime and imdb_score ')
plt.show()

# seaborn joint plot between runtime and imdb_score with type.

sns.jointplot(data=imdbScore, x='runtime', y='imdb_score', hue='type')
plt.show()

# seaborn displot between runtime and imdb_score with type.

sns.displot(data=imdbScore, x='runtime', y='imdb_score', hue='type')
plt.title('displot of runtime and imdb_score ')
plt.show()

netflix = netflix.drop('description', axis=1)
print(netflix.head())


#  Linear regression of imdb_score and release_year.

x = netflix[['imdb_score']]
y = netflix[['release_year']]
print(x.shape)
print(y.shape)

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3)
print(xTrain.shape)
print(xTest.shape)
print(yTrain.shape)
print(yTest.shape)

lr = LinearRegression()
lr.fit(xTrain, yTrain)
yPredict = lr.predict(xTest)
# print(yPredict.shape)

data = {}
data['ytest'] = np.reshape(yTest, (-1))
data['ypredict'] = np.reshape(np.array(yPredict), (-1))
# print(data)
df = pd.DataFrame(data=data)
print(df)

# reg plot between ytest and y predict.

sns.regplot(data=df, x='ytest', y='ypredict')
plt.title('regplot between ytest and y predict')
plt.show()

sns.scatterplot(data=df, x='ytest', y='ypredict')
plt.title('scatter plot between ytest and y predict')
plt.show()

mse = mean_squared_error(yTest,yPredict)
# print(mse)

d2Error = d2_absolute_error_score(yTest,yPredict)
print(d2Error)

medianError = median_absolute_error(yTest,yPredict)
print(medianError)

# Linear regression of imdb_votes and runtime.

netflix['imdb_votes'] = netflix['imdb_votes'].astype('int',errors='ignore')
netflix['imdb_votes'] = netflix['imdb_votes'].fillna(0)
netflix['imdb_votes'] = netflix['imdb_votes'].astype(int)

x = netflix[['runtime']]
y = netflix[['imdb_votes']]
print(x.head())
print(y.head())

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3)
print(xTrain.head())
print(xTest.head())
print(yTrain.head())
print(yTest.head())

lr = LinearRegression()
lr.fit(xTrain, yTrain)
yPredict = lr.predict(xTest)
print(yPredict.shape)

data = {}
data['ytest'] = np.reshape(yTest, (-1))
data['ypredict'] = np.reshape(np.array(yPredict), (-1))
# print(data)
df = pd.DataFrame(data=data)
print(df)

sns.regplot(data=df, x='ytest', y='ypredict')
plt.show()

mse = mean_squared_error(yTest,yPredict)
# print(mse)

d2Error = d2_absolute_error_score(yTest,yPredict)
print(d2Error)

medianError = median_absolute_error(yTest,yPredict)
print(medianError)

# LinearRegression of imdb_score and runtime.

netflix = netflix.astype({'imdb_score': 'int'})
netflix['imdb_score'] = netflix['imdb_score'].fillna(0)
netflix['imdb_score'] = netflix['imdb_score'].astype(int)

x = netflix[['imdb_score']]
y = netflix[['runtime']]
print(x.head())
print(y.head())

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3)
print(xTrain.head())
print(xTest.head())
print(yTrain.head())
print(yTest.head())

lr = LinearRegression()
lr.fit(xTrain, yTrain)
yPredict = lr.predict(xTest)
# print(yPredict.shape)

data = {}
data['ytest'] = np.reshape(yTest, (-1))
data['ypredict'] = np.reshape(np.array(yPredict), (-1))
# print(data)
df = pd.DataFrame(data=data)
# print(df)
sns.regplot(data=df, x='ytest', y='ypredict')
plt.title('reg plot between ytest and y predict')
plt.show()

mse = mean_squared_error(yTest,yPredict)
print(mse)

d2Error = d2_absolute_error_score(yTest,yPredict)
print(d2Error)

medianError = median_absolute_error(yTest,yPredict)
print(medianError)

# LinearRegression of release_year and runtime.

x = netflix[['release_year']]
y = netflix[['runtime']]

print(x.head())
print(y.head())

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3)
print(xTrain.head())
print(xTest.head())
print(yTrain.head())
print(yTest.head())

lr = LinearRegression()
lr.fit(xTrain, yTrain)
yPredict = lr.predict(xTest)
print(yPredict.shape)

data = {}
data['ytest'] = np.reshape(yTest, (-1))
data['ypredict'] = np.reshape(np.array(yPredict), (-1))
# print(data)
df = pd.DataFrame(data=data)
print(df)

# reg plot between ytest and ypredict

sns.regplot(data=df, x='ytest', y='ypredict')
plt.title('reg plot between ytest and ypredict')
plt.show()

# joint plot between ytest and ypredict
sns.jointplot(data=df, x='ytest', y='ypredict')
plt.show()

mse = mean_squared_error(yTest,yPredict)
print(mse)

d2Error = d2_absolute_error_score(yTest,yPredict)
print(d2Error)

medianError = median_absolute_error(yTest,yPredict)
print(medianError)

#  LogisticRegression of type  and runtime.

netflix['type'] = netflix['type'] == 'MOVIE'

x = netflix[['runtime']]
y = netflix[['type']]

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3)
print(xTrain.head())
print(xTest.head())
print(yTrain.head())
print(yTest.head())

lr = LogisticRegression()
lr.fit(xTrain, yTrain)
yPredict = lr.predict(xTest)
prediction = np.reshape(yPredict, (-1, 1))
print(prediction.shape)

acc = accuracy_score(yTest,yPredict)
print(acc)

yPredict = lr.predict_proba(xTest)[:, 1]

plt.scatter(xTest, yTest, color='green')
xValue = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
yValue = lr.predict_proba(xValue)[:, 1]
plt.xlabel('x')
plt.ylabel('y')

plt.title('LogisticRegression sigmoid line')
plt.plot(xValue, yValue, color='blue')
plt.show()

sns.violinplot(data=netflix, x= 'type', y='runtime',color='green')
plt.title('violin plot of LogisticRegression between type and runtime.')
sns.set(style='whitegrid')
plt.show()

sns.jointplot(data=netflix, x='type', y= 'runtime',color='red')
plt.show()

# LogisticRegression of type  and IMDB SCORE.

netflix['type'] = netflix['type'] == 'MOVIE'

x = netflix[['imdb_score']]
y = netflix[['type']]

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3)

print(xTrain.head())
print(xTest.head())
print(yTrain.head())
print(yTest.head())

lr = LogisticRegression()
lr.fit(xTrain, yTrain)
yPredict = lr.predict(xTest)
prediction = np.reshape(yPredict, (-1, 1))
print(prediction.shape)
#
acc = accuracy_score(yTest,yPredict)
print(acc)

yPredict = lr.predict_proba(xTest)[:, 1]

plt.scatter(xTest, yTest, color='green')
xValue = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
yValue = lr.predict_proba(xValue)[:, 1]
plt.xlabel('x')
plt.ylabel('y')
plt.title('LogisticRegression sigmoid line')
plt.plot(xValue, yValue, color='blue')
plt.show()

sns.violinplot(data=netflix, x= 'type', y='imdb_score',color='green')
plt.title('violin plot of LogisticRegression between type and imdb_score.')
sns.set(style='whitegrid')
plt.show()

# LogisticRegression of age_certification  and RUNTIME.

netflix['age_certification'] = netflix['age_certification'] == 'R'

x = netflix[['imdb_score']]
y = netflix[['age_certification']]

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3)

print(xTrain.head())
print(xTest.head())
print(yTrain.head())
print(yTest.head())

lr = LogisticRegression()
lr.fit(xTrain, yTrain)
yPredict = lr.predict(xTest)
prediction = np.reshape(yPredict, (-1, 1))
print(prediction.shape)

acc = accuracy_score(yTest,yPredict)
print(acc)

yPredict = lr.predict_proba(xTest)[:, 1]

plt.scatter(xTest, yTest, color='green')
xValue = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
yValue = lr.predict_proba(xValue)[:, 1]
plt.xlabel('x')
plt.ylabel('y')
plt.title('LogisticRegression sigmoid line')
plt.plot(xValue, yValue, color='blue')
plt.show()

sns.violinplot(data=netflix, x= 'age_certification', y='imdb_score',color='red')
plt.title('violin plot of LogisticRegression between imdb_score and age_certification.')
sns.set(style='whitegrid')
plt.show()

# LogisticRegression of age_certification  and RUNTIME.

netflix['age_certification'] = (netflix['age_certification'] == 'R')

x = netflix[['runtime']]
y = netflix['age_certification']

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3, random_state=42)

print(xTrain.head())
print(xTest.head())
print(yTrain.head())
print(yTest.head())

lr = LogisticRegression()
lr.fit(xTrain, yTrain)
yPredict = lr.predict(xTest)
prediction = np.reshape(np.array(yPredict),(-1,1))
print(prediction.shape)

acc = accuracy_score(yTest,yPredict)
print(acc)

yPredict = lr.predict_proba(xTest)[:, 1]

plt.scatter(xTest, yTest, color='green')
xValue = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
yValue = lr.predict_proba(xValue)[:, 1]

plt.plot(xValue, yValue, color='blue')
plt.show()

sns.violinplot(data=netflix, x= 'age_certification', y='imdb_score',color='red')
plt.title('violin plot of LogisticRegression between imdb_score and age_certification.')
sns.set(style='whitegrid')
plt.show()

# LogisticRegression of age_certification  and imdb_score.

netflix['age_certification'] = (netflix['age_certification'] == 'TV-Y').astype(int)

x = netflix[['imdb_score']]
y = netflix['age_certification']

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3, random_state=42)

# print(xTrain.head())
# print(xTest.head())
# print(yTrain.head())
# print(yTest.head())

lr = LogisticRegression()
lr.fit(xTrain, yTrain)
yPredict = lr.predict(xTest)
prediction = np.reshape(np.array(yPredict),(-1,1))
print(prediction.shape)

acc = accuracy_score(yTest,yPredict)
print(acc)

yPredict = lr.predict_proba(xTest)[:, 1]

plt.scatter(xTest, yTest, color='green')
xValue = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
yValue = lr.predict_proba(xValue)[:, 1]

plt.plot(xValue, yValue, color='blue')
plt.show()

sns.violinplot(data=netflix, x= 'age_certification', y='imdb_score',color='red')
plt.title('violin plot of LogisticRegression between imdb_score and age_certification.')
sns.set(style='whitegrid')
plt.show()

# LogisticRegression of age_certification  and runtime.

netflix['age_certification'] = (netflix['age_certification'] == 'R').astype(int)

x = netflix[['runtime']]
y = netflix['age_certification']

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3, random_state=42)
# print(xTrain.head())
# print(xTest.head())
# print(yTrain.head())
# print(yTest.head())

lr = LogisticRegression()
lr.fit(xTrain, yTrain)
yPredict = lr.predict(xTest)
prediction = np.reshape(np.array(yPredict),(-1,1))
print(prediction.shape)

acc = accuracy_score(yTest,yPredict)
print(acc)

yPredict = lr.predict_proba(xTest)[:, 1]

plt.scatter(xTest, yTest, color='green')
xValue = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
yValue = lr.predict_proba(xValue)[:, 1]

plt.plot(xValue, yValue, color='blue')
plt.show()

sns.violinplot(data=netflix, x= 'age_certification', y='runtime',color='black')
plt.title('violin plot of LogisticRegression between runtime and age_certification.')
sns.set(style='whitegrid')
plt.show()
