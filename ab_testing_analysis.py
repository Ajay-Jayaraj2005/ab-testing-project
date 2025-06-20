import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest

data = pd.DataFrame({
    'user_id': range(1, 2001),
    'group': ['control'] * 1000 + ['treatment'] * 1000,
    'converted': [0]*880 + [1]*120 + [0]*855 + [1]*145
})

summary = data.groupby('group')['converted'].agg(['count', 'sum', 'mean'])
summary.columns = ['Users', 'Conversions', 'Conversion Rate']
print("=== Group Summary ===")
print(summary)

control_conv = summary.loc['control', 'Conversions']
treatment_conv = summary.loc['treatment', 'Conversions']
n_control = summary.loc['control', 'Users']
n_treatment = summary.loc['treatment', 'Users']

z_score, p_value = proportions_ztest(
    [control_conv, treatment_conv], [n_control, n_treatment]
)

print("\n=== Z-Test Results ===")
print(f"Z-Score: {z_score:.4f}")
print(f"P-Value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Statistically significant result: Treatment outperformed control.")
else:
    print("No statistically significant difference found.")

summary['Conversion Rate'].plot(kind='bar', color=['skyblue', 'lightgreen'])
plt.title('Conversion Rate by Group')
plt.ylabel('Conversion Rate')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
