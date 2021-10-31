from os import walk
import csv
import pandas as pd

main_path = "./"

files_2019 = []
for (dirpath, dirnames, filenames) in walk(main_path + "2019"):
    files_2019.extend(dirnames)
    break

files_2020 = []
for (dirpath, dirnames, filenames) in walk(main_path + "2020"):
    files_2020.extend(dirnames)
    break

files_2021 = []
for (dirpath, dirnames, filenames) in walk(main_path + "2021"):
    files_2021.extend(dirnames)
    break

files = []

for month in files_2019:
    for (dirpath, dirnames, filenames) in walk(main_path + "2019/" + month + "/"):
        for day in dirnames:
            for (dirpath, dirnames, filenames) in walk(main_path + "2019/" + month + "/" + day + "/"):
                for filess in filenames:
                    a = dirpath + filess
                    files.append(a)
                    break

for month in files_2020:
    for (dirpath, dirnames, filenames) in walk(main_path + "2020/" + month + "/"):
        for day in dirnames:
            for (dirpath, dirnames, filenames) in walk(main_path + "2020/" + month + "/" + day + "/"):
                for filess in filenames:
                    a = dirpath + filess
                    files.append(a)
                    break

for month in files_2021:
    for (dirpath, dirnames, filenames) in walk(main_path + "2021/" + month + "/"):
        for day in dirnames:
            for (dirpath, dirnames, filenames) in walk(main_path + "2021/" + month + "/" + day + "/"):
                for filess in filenames:
                    a = dirpath + filess
                    files.append(a)
                    break

print(files)

#yayincilar = ["89408007","97716686","209139976","71761252","103237625","177249859","138111494","145202260","104781313","31443685","155642616","638580878","84898167","149232299","131403189","160677372","121552014","93853857","82388424","62178548","83399952"," 124368186","257049727","156203554","139041475","74020259","79442833","65539427","23076916","49508092","143794475","565560095","707467841","119149424","28541821","145875996","44055744","139848119","490374023","29512470","702773684","236619638","38287412","100630863","547326451"]
yayincilar = ["125387632"]
for yayinci in yayincilar:
    data = []
    header = []
    id = yayinci

    count = 0

    for path in files:
        count += 1
        file = open(path)
        csvreader = csv.reader(file)
        header = next(csvreader)
        print(count)
        for row in csvreader:
            if row[0] == id:
                data.append(row)
        file.close()

    df = pd.DataFrame(data,columns=header)

    print(df)

    from pandas import ExcelWriter

    writer = ExcelWriter('result_' + str(yayinci) + '.xlsx')
    df.to_excel(writer,'summary')
    writer.save()