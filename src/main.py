import pandas as pd
import os

salaries = pd.read_csv(os.path.join(os.path.dirname(__file__), '../data/salaries.csv'))
print(salaries)