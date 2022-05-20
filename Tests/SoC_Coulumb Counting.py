import numpy as np
import matplotlib.pyplot as plt

def convert_CSV_List(path): 
    filecsv = open(path, 'r')
    filecsvUnformattedData = filecsv.readlines() 
    filecsvFormattedData = list()

    for line in filecsvUnformattedData:
        initialLine = line.split(',')
        data = int(initialLine[0])
        current =  float(initialLine[1])
        filecsvFormattedData.append([data, current])
    return filecsvFormattedData

def SoC_Determination(data):
    current = list()
    dataMeasurement = list()
    for data in data:
        dataMeasurement.append(data[0])
        current.append(data[1])

    dataMeasurement_arr = np.array(dataMeasurement)
    voltage_arr = np.array(current)

    dataMeasurement_diff_arr = np.diff(dataMeasurement)

    SoC_Prev = 100
    SoC_Current = 0
    C = 198
    SoC = list()
    for i in range(0, len(dataMeasurement_diff_arr)):
        SoC_Current = SoC_Prev + (dataMeasurement_diff_arr[i]*current[i]) / C
        SoC.append(SoC_Current)
        SoC_Prev = SoC_Current
    return (SoC,dataMeasurement_diff_arr.tolist())

def main():
    path = r""
    battery_Data = convert_CSV_List(path)
    (soc, time_diff) = SoC_Determination(battery_Data)
    plt.plot(time_diff, soc)
main()
    