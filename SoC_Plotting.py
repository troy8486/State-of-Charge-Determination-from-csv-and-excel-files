import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use("seaborn")
plt.rc('xtick', labelsize = 8) 

def convert_Excel_List(path, n): 
    df = pd.read_excel(path, sheet_name= n)
    return df

def scatterPlot(DF):
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1)
    ax1.scatter(DF["timestamp"], DF["SoH"], s = 1)
    ax1.legend()
    ax1.set_title('SoH vs Time')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('SoH')

    ax2.scatter(DF["timestamp"], DF["Voltage"], s = 1)
    ax2.legend()
    ax2.set_title('Voltage vs Time')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Voltage')

    ax3.scatter(DF["timestamp"], DF["Current"], s = 1)
    ax3.legend()
    ax3.set_title('Curent vs Time')
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Current')

    ax4.scatter(DF["timestamp"], DF["Temperature"], s = 1)
    ax4.legend()
    ax4.set_title('Temperature vs Time')
    ax4.set_xlabel('Time')
    ax4.set_ylabel('Temperature')

    plt.tight_layout()
    plt.show()


def main():
    path = r"C:\Users\Admin\Desktop\IoT-BMS-Roy\BMS Project\Soc_Determination\Data\Management Laboratory Data ITB.xlsx"
    SoC_df1 = convert_Excel_List(path, 0)
    SoC_df2 = convert_Excel_List(path, 1)

    scatterPlot(SoC_df1)
    scatterPlot(SoC_df2)

main()