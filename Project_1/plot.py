import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('benchmark_results_last UIP Cut.csv')

# Convert 'SAT' to 1 and assume 'UNSAT' to 0 (if present)
df['dynamic_satisfiability'] = df['dynamic_satisfiability'].apply(lambda x: 1 if x == 'SAT' else 0)
df['jeroslow_satisfiability'] = df['jeroslow_satisfiability'].apply(lambda x: 1 if x == 'SAT' else 0)

# Heuristics
heuristic = ['dynamic', 'jeroslow']
time_column = [f'{x}_time' for x in heuristic]
sat_column = [f'{x}_satisfiability' for x in heuristic]
decision_column = [f'{x}_decision' for x in heuristic]

# Group by 'r' and take the mean for time and decision count, but sum for SAT count
grouped_time_decision = df.groupby('r').mean()
sat_counts = df.groupby('r')[sat_column].sum()  # Summing for SAT count

# Plotting Time for both heuristics on the same graph
plt.figure(figsize=(8,6))
plt.plot(grouped_time_decision[time_column[0]], label='Dynamic Time', color='blue')
plt.plot(grouped_time_decision[time_column[1]], label='Jeroslow Time', color='orange')
plt.title('Time Comparison (Dynamic vs Jeroslow)')
plt.xlabel('r')
plt.ylabel('Time')
plt.legend()
plt.savefig('time_comparison_plot.png')
plt.close()

# Plotting SAT counts for both heuristics on the same graph
plt.figure(figsize=(8,6))
plt.plot(sat_counts[sat_column[0]], label='Dynamic SAT Count', color='blue')
plt.plot(sat_counts[sat_column[1]], label='Jeroslow SAT Count', color='orange')
plt.title('SAT Count Comparison (Dynamic vs Jeroslow)')
plt.xlabel('r')
plt.ylabel('SAT Count')
plt.legend()
plt.savefig('satisfiability_comparison_plot.png')
plt.close()

# Plotting Decision Count for both heuristics on the same graph
plt.figure(figsize=(8,6))
plt.plot(grouped_time_decision[decision_column[0]], label='Dynamic Decision Count', color='blue')
plt.plot(grouped_time_decision[decision_column[1]], label='Jeroslow Decision Count', color='orange')
plt.title('Decision Count Comparison (Dynamic vs Jeroslow)')
plt.xlabel('r')
plt.ylabel('Decision Count')
plt.legend()
plt.savefig('decision_count_comparison_plot.png')
plt.close()

# Compute decision count / time ratio for both heuristics
df['dynamic_decision_time_ratio'] = df['dynamic_decision'] / df['dynamic_time']
df['jeroslow_decision_time_ratio'] = df['jeroslow_decision'] / df['jeroslow_time']

# Group by 'r' and calculate the mean for the decision/time ratio
grouped_ratio = df.groupby('r')[['dynamic_decision_time_ratio', 'jeroslow_decision_time_ratio']].mean()

# Plot the mean decision/time ratio for both heuristics
plt.figure(figsize=(8,6))
plt.plot(grouped_ratio['dynamic_decision_time_ratio'], label='Dynamic Decision/Time', color='blue')
plt.plot(grouped_ratio['jeroslow_decision_time_ratio'], label='Jeroslow Decision/Time', color='orange')
plt.title('Decision/Time Ratio Comparison (Dynamic vs Jeroslow)')
plt.xlabel('r')
plt.ylabel('Decision Count / Time')
plt.legend()
plt.savefig('decision_time_ratio_comparison_plot.png')
plt.close()

# Compute decision count / time ratio for both heuristics
df['dynamic_decision_time_ratio'] = df['dynamic_decision'] / df['dynamic_time']
df['jeroslow_decision_time_ratio'] = df['jeroslow_decision'] / df['jeroslow_time']

# Group by 'r' and calculate the mean for the decision/time ratio
grouped_ratio = df.groupby('r')[['dynamic_decision_time_ratio', 'jeroslow_decision_time_ratio']].mean()

# Plot the mean decision/time ratio for both heuristics
plt.figure(figsize=(8,6))
plt.plot(grouped_ratio['dynamic_decision_time_ratio'], label='Dynamic Decision/Time', color='blue')
plt.plot(grouped_ratio['jeroslow_decision_time_ratio'], label='Jeroslow Decision/Time', color='orange')
plt.title('Decision/Time Ratio Comparison (Dynamic vs Jeroslow)')
plt.xlabel('r')
plt.ylabel('Decision Count / Time')
plt.legend()
plt.savefig('decision_time_ratio_comparison_plot.png')
plt.close()
