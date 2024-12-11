import math

def findRow(teamName, content):
    for i in range(len(content)):
        if content[i][0] == teamName:
            return i
        if content[i][0] == "0":
            content[i][0] = teamName
            content.append(["0"] * 10)
            return i
    raise ValueError(f"Row for team '{teamName}' could not be found or added.")

def RefreshTable(phase):
    content = [["0"] * 10 for _ in range(1)]

    try:
        with open(str(phase) + 'matches.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if not line.strip():
                    continue
                match = line.strip().split(';')
                
                if len(match) < 5:
                    raise ValueError(f"Invalid match data: {line.strip()}")

                try:
                    t1Row = findRow(match[1], content)
                    t2Row = findRow(match[4], content)
                except ValueError as e:
                    print(f"Error processing team: {e}")
                    continue

                if not match[2].isdigit() or not match[3].isdigit():
                    raise ValueError(f"Invalid score data: {match[2]} or {match[3]} is not a number.")
                
                score1 = int(match[2])
                score2 = int(match[3])

                content[t1Row][1] = str(int(content[t1Row][1]) + 1)  # Мt1
                content[t2Row][1] = str(int(content[t2Row][1]) + 1)  # Мt2

                if score1 > score2:
                    content[t1Row][2] = str(int(content[t1Row][2]) + 1)  # П
                    content[t2Row][3] = str(int(content[t2Row][3]) + 1)  # З
                    content[t1Row][8] = str(int(content[t1Row][8]) + 3)  # Toчки
                elif score2 > score1:
                    content[t1Row][3] = str(int(content[t1Row][3]) + 1)  # З
                    content[t2Row][2] = str(int(content[t2Row][2]) + 1)  # П
                    content[t2Row][8] = str(int(content[t2Row][8]) + 3)  # Toчки
                else:
                    content[t1Row][4] = str(int(content[t1Row][4]) + 1)  # Р
                    content[t2Row][4] = str(int(content[t2Row][4]) + 1)  # Р
                    content[t1Row][8] = str(int(content[t1Row][8]) + 1)  # Toчки
                    content[t2Row][8] = str(int(content[t2Row][8]) + 1)  # Toчки

                content[t1Row][5] = str(int(content[t1Row][5]) + score1)  # ОГ
                content[t2Row][5] = str(int(content[t2Row][5]) + score2)  # ОГ

                content[t1Row][6] = str(int(content[t1Row][6]) + score2)  # ДГ
                content[t2Row][6] = str(int(content[t2Row][6]) + score1)  # ДГ

                content[t1Row][7] = str(int(content[t1Row][5]) - int(content[t1Row][6]))  # Раз
                content[t2Row][7] = str(int(content[t2Row][5]) - int(content[t2Row][6]))  # Раз

                content[t1Row][9] = (f"{math.ceil((int(content[t1Row][8]) / int(content[t1Row][1])) * 1000) / 1000:.3f}" if int(content[t1Row][1]) > 0 else "0.000")  # Коефициент
                content[t2Row][9] = (f"{math.ceil((int(content[t2Row][8]) / int(content[t2Row][1])) * 1000) / 1000:.3f}" if int(content[t2Row][1]) > 0 else "0.000")  # Коефициент

        content = sorted(content, key=lambda x: float(x[9]) if x[9] != "0" else 0, reverse=True)

        with open(str(phase) + 'table.txt', 'w', encoding='utf-8') as file:
            for sublist in content:
                if sublist[0] == "0":
                    break
                file.write(';'.join(sublist) + '\n')
    except FileNotFoundError:
        print(f"Error: The file {str(phase)}matches.txt was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

RefreshTable(int(input("Enter phase number: ")))