import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('benchmark_results.csv')
df.drop(columns=['FileName'], inplace=True)
heuristic = [
    # 'dynamic',   
    # 'jeroslow',  
    'twoclause',
    'random',    
]
# Convert 'SAT' to 1 and assume 'UNSAT' to 0 (if present)
for x in heuristic:
    df[f'{x}_satisfiability'] = df[f'{x}_satisfiability'].apply(lambda x: 1 if x == 'SAT' else 0)

time_column = [f'{x}_time' for x in heuristic]
sat_column = [f'{x}_satisfiability' for x in heuristic]
decision_column = [f'{x}_decision' for x in heuristic]

# Group by 'r' and take the mean for time and decision count, but sum for SAT count
grouped_time_decision = df.groupby('r').mean()
sat_counts = df.groupby('r')[sat_column].sum()  # Summing for SAT count

# Plotting Time for both heuristics on the same graph
plt.figure(figsize=(8,6))
for x in heuristic:
    plt.plot(grouped_time_decision[f'{x}_time'], label=f'{x} Time')
plt.title('Time Comparison')
plt.xlabel('r')
plt.ylabel('Time')
plt.legend()
plt.savefig('time_comparison_plot.png')
plt.close()

# Plotting SAT counts for both heuristics on the same graph
plt.figure(figsize=(8,6))
for x in heuristic:
    plt.plot(sat_counts[f'{x}_satisfiability'], label=f'{x} SAT Count')
plt.title('SAT Count Comparison')
plt.xlabel('r')
plt.ylabel('SAT Count')
plt.legend()
plt.savefig('satisfiability_comparison_plot.png')
plt.close()

# Plotting Decision Count for both heuristics on the same graph
plt.figure(figsize=(8,6))
for x in heuristic:
    plt.plot(grouped_time_decision[f'{x}_decision'], label=f'{x} Decision Count')
plt.title('Decision Count Comparison')
plt.xlabel('r')
plt.ylabel('Decision Count')
plt.legend()
plt.savefig('decision_count_comparison_plot.png')
plt.close()

# Compute decision count / time ratio for both heuristics
for x in heuristic:
    df[f'{x}_decision_time_ratio'] = df[f'{x}_decision'] / df[f'{x}_time']
    grouped_ratio = df.groupby('r')[f'{x}_decision_time_ratio'].mean()

plt.figure(figsize=(8,6))
for x in heuristic:
    plt.plot(grouped_ratio, label=f'{x} Decision/Time')

plt.title('Decision/Time Ratio Comparison')
plt.xlabel('r')
plt.ylabel('Decision Count / Time')
plt.legend()
plt.savefig('decision_time_ratio_comparison_plot.png')
plt.close()

# Compute decision count / time ratio for both heuristics
for x in heuristic:
    df[f'{x}_decision_time_ratio'] = df[f'{x}_decision'] / df[f'{x}_time']

# Group by 'r' and calculate the mean for the decision/time ratio
for x in heuristic:
    grouped_ratio = df.groupby('r')[f'{x}_decision_time_ratio'].mean()

plt.figure(figsize=(8,6))
for x in heuristic:
    plt.plot(grouped_ratio, label=f'{x} Decision/Time')

plt.title('Decision/Time Ratio Comparison')
plt.xlabel('r')
plt.ylabel('Decision Count / Time')
plt.legend()
plt.savefig('decision_time_ratio_comparison_plot.png')
plt.close()