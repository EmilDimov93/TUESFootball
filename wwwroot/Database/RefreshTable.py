def findRow(teamName, content):
    for i in range(len(content)):
        if content[i][0] == teamName:
            return i
        if content[i][0] == "0":
            content[i][0] = teamName
            content.append(["0"] * 10)
            return i
        
def RefreshTable(phase):
    content = [["0"] * 10 for _ in range(1)]

    with open(str(phase) + 'matches.txt', 'r', encoding='utf-8') as file:
        for line in file:
            match = line.strip().split(';')
            t1Row = findRow(match[1], content)
            t2Row = findRow(match[4], content)

            content[t1Row][1] = str(int(content[t1Row][1]) + 1) #Мt1
            content[t2Row][1] = str(int(content[t2Row][1]) + 1) #Мt2

            if match[2] > match[3]:
                content[t1Row][2] = str(int(content[t1Row][2]) + 1) #П
                content[t2Row][3] = str(int(content[t2Row][3]) + 1) #З
                
                content[t1Row][8] = str(int(content[t1Row][8]) + 3) #Toчки
            elif match[3] > match[2]:
                content[t1Row][3] = str(int(content[t1Row][3]) + 1) #З
                content[t2Row][2] = str(int(content[t2Row][2]) + 1) #П

                content[t2Row][8] = str(int(content[t2Row][8]) + 3) #Toчки
            else:
                content[t1Row][4] = str(int(content[t1Row][4]) + 1) #Р
                content[t2Row][4] = str(int(content[t2Row][4]) + 1) #Р

                content[t1Row][8] = str(int(content[t1Row][8]) + 1) #Toчки
                content[t2Row][8] = str(int(content[t2Row][8]) + 1) #Toчки

            content[t1Row][5] = str(int(content[t1Row][5]) + int(match[2])) #ОГ
            content[t2Row][5] = str(int(content[t2Row][5]) + int(match[3])) #ОГ

            content[t1Row][6] = str(int(content[t1Row][6]) + int(match[3])) #ДГ
            content[t2Row][6] = str(int(content[t2Row][6]) + int(match[2])) #ДГ

            content[t1Row][7] = str(int(content[t1Row][5]) - int(content[t1Row][6])) #Раз
            content[t2Row][7] = str(int(content[t2Row][5]) - int(content[t2Row][6])) #Раз

            content[t1Row][9] = str(round(int(content[t1Row][8]) / int(content[t1Row][1]), 3)) #Коефициент
            content[t2Row][9] = str(round(int(content[t2Row][8]) / int(content[t2Row][1]), 3)) #Коефициент

    content = sorted(content, key=lambda x: float(x[9]) if x[9] != "0" else 0, reverse=True)

    with open(str(phase) + 'table.txt', 'w', encoding='utf-8') as file:
        for sublist in content:
            if sublist[0] == "0":
                break
            file.write(';'.join(sublist) + '\n')

RefreshTable(int(input("Enter phase number: ")))