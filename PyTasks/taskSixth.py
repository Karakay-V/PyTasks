import csv

def taskSixth():
    info = [
        [ 1, "Taras Shevchenko", 5, 10, 15 ],
        [ 2, "Oleksa Biloschura", 3, 7, 80 ],
        [ 3, "Oleksandr Mamonov", 4, 8, 60 ],
        [ 4, "Andy Ibrahim", 5, 9, 30 ],
        [ 5, "Denji Benzopila", 2, 4, 20 ]
    ]
    with open('marks.csv', "+a",) as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['INDEX'] + ['STUDENT'] + ['GRADE'])
        for i in range(len(info)):
            csvwriter.writerow([info[i][0]] + [info[i][1]] + [info[i][2]])
    
    with open("statistics.txt", "+a") as txtfile:
        corAns = [4, 4, 4, 3, 4, 4, 5, 5, 3, 3]
        for i in range(len(corAns)):
            txtfile.write('Запитання ' + str(i + 1) + ': ' 
                          +'\n    Вірних відповідей: ' + str((corAns[i] / len(info))*100) + '%'
                          +'\n    Невірних відповідей: ' + str(100-(corAns[i] / len(info))*100) + '%'
                          +'\n\n'
                         )
        txtfile.write('\nНайвищі оцінки отримали: ' 
                      +'\n    ' + str(info[1][1]) 
                      +'\n    та '
                      +'\n    ' + str(info[3][1])
                     )