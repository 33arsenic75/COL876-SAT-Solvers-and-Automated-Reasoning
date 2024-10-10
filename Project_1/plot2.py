import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('results.csv')

# Group by 'r' and calculate the mean of other columns
grouped_data = data.groupby('r').mean().reset_index()

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(grouped_data['r'], grouped_data['Satisfiability'], label='Satisfiability', marker='o')
plt.plot(grouped_data['r'], grouped_data['Conflicts'], label='Conflicts', marker='o')
plt.plot(grouped_data['r'], grouped_data['Decisions'], label='Decisions', marker='o')
plt.plot(grouped_data['r'], grouped_data['Propagations'], label='Propagations', marker='o')
plt.xlabel('r Value')
plt.ylabel('Mean Values')
plt.title('Mean Values Grouped by r')
plt.legend()
plt.grid()
plt.savefig('ground_truth.png')
