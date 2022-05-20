from numpy.lib.function_base import append
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn")

path = r"C:\Users\Admin\Desktop\IoT-BMS-Roy\BMS Project\Soc_Determination\Test_Data.xlsx"
df = pd.read_excel(path, sheet_name= 0)
timestamp = df["timestamp"].astype(str)
hour = timestamp.str[11:13]
min = timestamp.str[14:16]
hour = pd.to_numeric(hour)
min = pd.to_numeric(min)
time = hour*3600 + min*60
time_arr = np.array(time)
time_diff_arr = abs(np.diff(time_arr))

current = df["Current"].tolist()

soc_prev = 74.9
soc_current = 0
soc = list()
soc.append(soc_prev)
c = 198

for i in range(0, len(time_diff_arr)):
    soc_current = soc_prev + (time_diff_arr[i]*current[i])/(3600*c)
    soc.append(soc_current)
    soc_prev = soc_current

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

ax1.scatter(df["timestamp"], soc)
ax1.legend()
ax1.set_title('SoC Estimation using Coulumb Counting')
ax1.set_xlabel('SoC(%)')
ax1.set_ylabel('Time')

ax2.scatter(df["timestamp"], df["SoC (Hybrid Inverter Sunny Island)"])
ax2.legend()
ax2.set_title('SoC Estimation using Hybrid Inverter Sunny Island')
ax2.set_xlabel('SoC(%)')
ax2.set_ylabel('Time')

plt.tight_layout()

plt.show()

df_soc = pd.DataFrame()
df['SoC'] = soc
df.to_excel('SoC_New.xlsx', index = False)

    