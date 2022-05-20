import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use("seaborn")
plt.rc('xtick', labelsize = 8) 

def convert_Excel_List(path): 
    df = pd.read_excel(path, sheet_name= 0)
    timestamp = df["timestamp"].astype(str)
    hour = timestamp.str[11:13]
    min = timestamp.str[14:16]
    hour = pd.to_numeric(hour)
    min = pd.to_numeric(min)
    time = hour + min/60
    time_arr = np.array(time)
    time_diff_arr = abs(np.diff(time_arr))
    return df, time_diff_arr

def SoC_Determination(current, time_diff):
    Current = current.tolist()
    Time_Diff = time_diff
    soc_prev = 74.9
    soc_current = 0
    soc = list()
    soc.append(soc_prev)
    c = 198

    for i in range(0, len(Time_Diff)):
        soc_current = soc_prev + (Time_Diff[i]*current[i])/(c)
        soc.append(soc_current)
        soc_prev = soc_current
    return(soc)

def main():
    path = r"C:\Users\Admin\Desktop\IoT-BMS-Roy\BMS Project\Soc_Determination\Data\Management Laboratory Data ITB.xlsx"
    (df_SoC, Time_Difference_Data) = convert_Excel_List(path)
    (SoC_Data) = SoC_Determination(df_SoC["Current"], Time_Difference_Data)

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
    ax1.scatter(df_SoC["timestamp"], SoC_Data, s = 1)
    ax1.legend()
    ax1.set_title('SoC Estimation using Coulomb Counting')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('SoC(%)')

    ax2.scatter(df_SoC["timestamp"], df_SoC["SoC (Hybrid Inverter Sunny Island)"], s = 1)
    ax2.legend()
    ax2.set_title('SoC Estimation using Hybrid Inverter Sunny Island')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('SoC(%)')

    plt.tight_layout()
    plt.show()

main()