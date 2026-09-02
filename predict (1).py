import joblib as jb
import pandas as pd

# Load the saved model
saved_model = jb.load('linear_regression.joblib')

# Take input from the user for each required feature
input_values = {}
for feature in saved_model['inputs']:
    value = input(f'Enter the {feature.lower()}: ')
    input_values.update({feature: float(value)})

# Create a single-row DataFrame from the input
input_record = pd.DataFrame(input_values, index=[0])

# Make prediction
predicted_performance = saved_model['model'].predict(input_record)

print(f'Predicted performance index: {predicted_performance[0]}')
