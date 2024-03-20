import joblib
import random
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings(action="ignore")



# create data
random.seed(0)

numbers_1 = [random.randint(0, 60) for _ in range(60)]
numbers_2 = [random.randint(0, 60) for _ in range(60)]
results = [numbers_1[i] + numbers_2[i] for i in range(60)]

data = pd.DataFrame(
    data={
        "x": numbers_1,
        "y": numbers_2,
        "sum": results
    }
)

plt.scatter(data['x'], data['sum'], label='X Data')
plt.scatter(data['y'], data['sum'], label='Y Data')

plt.title('Scatter Plot of X and Y Data', fontsize=16, fontweight='bold', color='blue', style='italic')
plt.xlabel('X Values', fontsize=14, fontweight='bold', color='green')
plt.ylabel('Sum Values', fontsize=14, fontweight='bold', color='green')
plt.legend()

plt.show()

X = data[["x", "y"]]
y = data["sum"]



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression() 
model.fit(X_train,y_train)

model.score(X_train, y_train)
model.score(X_test, y_test)

y_pred = model.predict(X_test)
data_predict = pd.DataFrame(
    data={
        "Acual": y_test,
        "Predicted": y_pred
    }
)

joblib.dump(model,'model_')
