import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('benchmark_results.csv')
# Convert serial_number to numeric
# df['serial_number'] = pd.to_numeric(df['serial_number'])
# df['r_value'] = pd.to_numeric(df['r_value'])

# Group by r value and calculate the mean of the time columns
time_columns = ['dynamic_time', 'jeroslow_time']
mean_times_by_r = df.groupby('r')[time_columns].mean()

# Plotting the mean times for each heuristic as per r value
plt.figure(figsize=(10, 6))
for column in time_columns:
    plt.plot(mean_times_by_r.index, mean_times_by_r[column], label=column)

plt.xlabel('r value')
plt.ylabel('Mean Time (s)')
plt.title('Mean Time Taken by Each Heuristic as per r Value')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('plot1.png')

# Calculate the number of SAT values for each r value
sat_columns = ['dynamic_satisfiability', 'jeroslow_satisfiability']
df['sat_count'] = df[sat_columns].apply(lambda row: row.str.count('SAT').sum(), axis=1)
sat_counts = df.groupby('r')['sat_count'].sum()

# Calculate the mean time for each heuristic
mean_heuristic_times = df[time_columns].mean()

# Print the results
print("Mean times by r:")
print(mean_times_by_r)
print("\nSAT counts by r value:")
print(sat_counts)
print("\nMean times for each heuristic:")
print(mean_heuristic_times)

# Calculate the decision counts for each heuristic
decision_columns = ['dynamic_decision', 'jeroslow_decision']
df['decision_count'] = df[decision_columns].sum(axis=1)
decision_counts = df.groupby('r')['decision_count'].sum()

# Calculate the ratio of decision counts for the two heuristics
df['decision_ratio'] = df[decision_columns[0]] / df[decision_columns[1]]
decision_ratios = df.groupby('r')['decision_ratio'].mean()

# Plotting the decision counts for each heuristic vs r
plt.figure(figsize=(10, 6))
for column in decision_columns:
    plt.plot(decision_counts.index, df.groupby('r')[column].sum(), label=column)

plt.xlabel('r value')
plt.ylabel('Decision Count')
plt.title('Decision Count for Each Heuristic vs r Value')
plt.legend()
plt.grid(True)
# plt.show()
plt.savefig('plot2.png')
# Plotting the ratio of decision counts for the two heuristics vs r
plt.figure(figsize=(10, 6))
plt.plot(decision_ratios.index, decision_ratios, label='Decision Ratio', color='orange')

plt.xlabel('r value')
plt.ylabel('Decision Ratio')
plt.title('Ratio of Decision Count for Two Heuristics vs r Value')
plt.legend()
plt.grid(True)
# plt.show()
plt.savefig('plot3.png')

# Calculate the execution time vs decision count for both heuristics
execution_time = df[time_columns].mean(axis=1)
decision_count = df[decision_columns].mean(axis=1)

# Calculate the mean decision count and mean time for each r value
mean_decision_counts = df.groupby('r')['decision_count'].mean()
mean_times = mean_times_by_r.mean(axis=1)  # Assuming mean_times_by_r is already calculated

# Calculate the ratio of mean decision count to mean time
decision_time_ratio = mean_decision_counts / mean_times

# Plotting the ratio of mean decision count to mean time
plt.figure(figsize=(10, 6))
plt.plot(decision_time_ratio.index, decision_time_ratio, label='Decision Count to Time Ratio', color='green')

plt.xlabel('r value')
plt.ylabel('Decision Count to Mean Time Ratio')
plt.title('Ratio of Mean Decision Count to Mean Time for Each Heuristic vs r Value')
plt.legend()
plt.grid(True)
plt.savefig('plot4.png')
# plt.show()