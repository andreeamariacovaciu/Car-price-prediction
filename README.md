## Car price prediction

This is a demo project which shows how Machine Learning Models are deployed on production using **Flask API**

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Learning Model) and Flask (for API) installed.

### What is the project Structure
This project has three major parts :
1. model.py - This contains code for the Machine Learning model. to predict cars price based on training data in 'cars.csv' file. The algorithm used is Linear Regression. Taking into consideration that the original dataframe contains 10 features that predict the car price, I chose only the 6 most important features. The other 4 features do not have significant impact on the predicted value.
2. app.py - This contains Flask APIs that receives car details through GUI or API calls, computes the predicted value based on the model and returns it.
3. templates - This folder contains the HTML template to allow user to enter car details and displays the predicted car price.

### How to run the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python model.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000

Enter valid numerical values in all 6 input boxes and hit Predict Car Price.
Then you should  be able to see the predicted car price on the HTML page!


![image](https://user-images.githubusercontent.com/86802852/152191089-fa42546c-3f47-4311-b2bc-68821c80e440.png)
