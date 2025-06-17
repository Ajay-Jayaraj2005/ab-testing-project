# A/B Testing Analysis

This project demonstrates a complete A/B testing workflow using Python. It simulates a real-world scenario of comparing two user groups — control and treatment — to determine if a UI change improves user conversion.

#Objective
Determine if changing the design increases conversions using hypothesis testing (Z-test).

#Dataset
- 2,000 users
- 1,000 in control group (12% conversion rate)
- 1,000 in treatment group (14.5% conversion rate)

#Tools Used
- Python 3
- Pandas
- SciPy (Z-test)
- Matplotlib

#Key Findings
- Control conversion rate: ~12%
- Treatment conversion rate: ~14.5%
- P-value < 0.05 → **Statistically significant improvement** in conversion

#How to Run
open bash
pip install pandas matplotlib scipy
python ab_testing_analysis.py
