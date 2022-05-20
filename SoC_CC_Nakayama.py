import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def convert_CSV_List(path): 
    df = pd.read_csv(path)
    timestamp = df["time"].astype(str)
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
    path = r"C:\Users\Admin\Desktop\IoT-BMS-Roy\BMS Project\Soc_Determination\Data\BMS_test1.csv"
    (df_SoC, Time_Difference_Data) = convert_CSV_List(path)
    (SoC_Data) = SoC_Determination(df_SoC["BatCur"], Time_Difference_Data)


    plt.plot(df_SoC["time"], SoC_Data)
    plt.legend()
    plt.title('SoC Estimation using Coulumb Counting')
    plt.xlabel('Time')
    plt.ylabel('SoC(%)')
    
    plt.show()

main()