import csv
import json
import os
import pandas as pd
import matplotlib.pyplot as plt


def get_process_names():
    process_list = []
    filePath = ""
    if os.name == "nt":
        filePath = os.path.dirname(__file__) + os.sep + "process_id.csv"
    else:
        filePath = os.path.dirname(__file__) + os.sep + "process_id_mac.csv"

    status = os.path.exists(filePath)
    print("Is process csv file present? :" + str(status))

    with open(filePath, 'r') as csv_file:  # Opens the file in read mode
        csv_reader = csv.reader(csv_file)  # Making use of reader method for reading the file

        for line in csv_reader:  # Iterate through the loop to read line by line
            if any(line):
                process_list.append(line[0])
    return process_list


def create_file(name, memory_values, filePath):
    s = ''
    s += name + ','
    for key in memory_values.keys():
        s += str(memory_values[key]) + ','
    s = s[:-1]
    s += '\n'

    file = open(filePath, 'a')
    file.write(s)
    file.close()
    pass


def create_csv_file(process_list):
    filePath = os.path.dirname(__file__) + os.sep + "csvfile.csv"

    if os.path.exists(filePath):
        os.remove(filePath)

    for process in process_list:
        # print("Creating CSV file for: %s" % process.name)
        create_file(str(process.name.replace(".exe", "")), process.memory_values, filePath)


def create_html(process_list):
    html = '<html><head> <style> table, td, th { border: 1px solid black; } table { width: 100%; border-collapse: collapse;} </style></head><body><h1>Memory report</h1>'

    process_details = "'"
    for process in process_list:
        html += '<p><b>' + process.name + ' PID: ' + str(process.pid) + '</b></p><table>'
        html += '<tr><td>Time</td>'
        process_details += process.name + str(process.pid) + "name_end"
        for time_val in process.memory_values:
            html += '<td>' + str(time_val) + '</td>'
            process_details += str(time_val) + "time_end"
        html += '</tr><tr><td>Memory(MB)</td>'
        for memory_val in process.memory_values.values():
            html += '<td>' + str(memory_val) + '</td>'
            process_details += str(memory_val) + "memory_end"
        process_details += 'process_end'
        html += '</tr> </table>'
    html += "</body></html>"
    html_file = open(os.path.dirname(__file__) + os.sep + "MemoryReport.html", "w")
    html_file.write(html)
    html_file.close()


def plot_graph():
    pd.read_csv(os.path.dirname(__file__) + os.sep + 'csvfile.csv', header=None).T.to_csv(
        os.path.dirname(__file__) + os.sep + 'readings.csv', header=False, index=False)
    df = pd.read_csv(os.path.dirname(__file__) + os.sep + 'readings.csv')
    df = df.replace('\n', '', regex=True)

    df.plot.line()

    plt.legend(title="Processes", loc='upper center', bbox_to_anchor=(0.5, 1.05),
               ncol=3, fancybox=True, shadow=True, fontsize='x-small')
    x1, x2, y1, y2 = plt.axis()
    plt.axis((x1, x2, y1, y2 + 30))
    plt.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom=False,  # ticks along the bottom edge are off
        top=False,  # ticks along the top edge are off
        labelbottom=False)

    plt.title('Memory Usage of Processes', pad=40, fontsize='xx-large')

    plt.ylabel('Ram Consumed (MB)', fontsize='large')
    plt.xlabel('Time ->', fontsize='large')

    fig1 = plt.gcf()
    fig1.set_size_inches(16, 9)
    fig1.autofmt_xdate()
    path = graphPath()
    fig1.savefig(path, format='jpg', dpi=300)


def clear_graph_data():
    with open("MemoryReportGraph.html", "r") as f:
        lines = f.readlines()
    with open("MemoryReportGraph.html", "w") as f:
        for line in lines:
            if "<script>var s =" not in line.strip("\n"):
                f.write(line)


def graphPath():
    modifiedPath = "ccd" + os.sep + "commonutils" + os.sep + "mailutils" + os.sep + "chart.jpg"
    finalPath = getProjectRootDir() + os.sep + modifiedPath
    return finalPath

def getProjectRootDir():
    head, tail = os.path.split(os.path.dirname(__file__))
    project_root, t1 = os.path.split(head)
    return project_root

def readJsonFile(filePath):
    f = open(filePath)
    return json.load(f)


