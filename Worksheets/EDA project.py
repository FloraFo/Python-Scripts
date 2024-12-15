import random
random.seed(2024)

import missingno as msno
import numpy as np
from scipy.stats import shapiro
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.datasets import load_wine
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

from fasteda import fast_eda

# You can also use this section to suppress warnings generated by your code:
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

sns.set_context('notebook')
sns.set_style('white')


#import dataset
wine = load_wine()
#print(wine['DESCR'])
data, target = load_wine(return_X_y=True, as_frame=True)

wines_df = pd.concat([data,pd.Series(target)],axis=1).rename({0: 'target'}, axis=1)

#check if nan
numb_of_nan = wines_df.isna().max(axis=1).max()
if numb_of_nan : 
    print("Some empty vlaues are there. They should be suppressed or replaced with mean or median (SimpleImputer)")
else:
    print("No np.nan, you can go haead!")

#check if we can encode 
print("There are no values indicating classification (ex. red vs white) neither categorical features (ex. text)")

#fast exploratory data analysis 
#fast_eda(wines_df)
print("The results of EDA provides some indicators, like ouliers and logaritmic distribution. We will now train and test the model with outliers and then with log and without outliers and see if performances are better")

# train and test model
x_train, x_test, y_train, y_test = train_test_split(wines_df.iloc[:,:-1], wines_df.iloc[:, [-1]], test_size=0.30, random_state=8)
lr = LinearRegression()
lr.fit(x_train, y_train)
ypred = lr.predict(x_test)
print("R2 equals: ", lr.score(x_test, y_test))
print("Rootm mean squared error equals : ", root_mean_squared_error(y_test,ypred))

# adjust features distribution
print("\nWe will now check if features are normally distributed and if not if a logarithimc distribution could be used\n")

alpha = 0.05
for i, col in enumerate(wines_df.iloc[:, :-1].columns):
    stat, p = shapiro(wines_df[col])
    if p>alpha:
         print('Sample looks normally distributed (fail to reject %s)' % (col))
    else:
        print('Sample does not look normally distributed. We will now check if logarithm could be taken for %s' % (col))
        stat, p = shapiro(np.log(wines_df[col]))
        if p>alpha:
            print('Sample looks log-normally distributed. %s will be replaced with log' % (col))
            x_train[col] = np.log(x_train[col])
            x_test[col] = np.log(x_test[col])
        else:
            print("Neither log-normally distribution is possible for %s" % (col))

print("\nAfter logarithmic distribution adjustment:\n")
lr.fit(x_train, y_train)
ypred = lr.predict(x_test)
print("R2 equals: ", lr.score(x_test, y_test))
print("Rootm mean squared error equals : ", root_mean_squared_error(y_test,ypred))

#outliers : linear regression with removal of outliers
print("\nWe will now remove outliers.")

for i, col in enumerate(x_train.columns):
    x_train_nonoutliers_index = x_train.index[x_train[col] <= x_train[col].quantile(0.999)]
    if len(x_train_nonoutliers_index) !=0:
        print("Removing outliers for %s: nulber of lines removed : %s" % (col, x_train.shape[0] - len(x_train_nonoutliers_index)))
        x_train = x_train.loc[x_train_nonoutliers_index]
        y_train = y_train.loc[x_train_nonoutliers_index]

print("\nAfter removal of outliers:\n")
lr.fit(x_train, y_train)
ypred = lr.predict(x_test)
print("R2 equals: ", lr.score(x_test, y_test))
print("Rootm mean squared error equals : ", root_mean_squared_error(y_test,ypred))
