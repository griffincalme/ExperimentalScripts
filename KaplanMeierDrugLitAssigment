#Griffin Calme
#Group 15, week 8 activity
#Kaplan Meier survival curve

import pandas as pd
from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt
kmf = KaplanMeierFitter()

df = pd.DataFrame.from_csv('wk8gp15KapMeier.csv')

print(df)

groups = df['Group']
ix = (groups == 2)

T = df['SERIAL TIME (years)']
E = df['STATUS']

kmf.fit(T[~ix], E[~ix], label='1')
ax = kmf.plot()

kmf.fit(T[ix], E[ix], label='2')
kmf.plot(ax=ax, ci_force_lines=False)

plt.show()
