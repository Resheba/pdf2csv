import tabula, csv

def pdf2csv(pdfName: str = 'file.pdf')
    csvName = '.'.join(pdfName.split('.')[0:-1])+'.csv'
    try:
        tabula.convert_into(pdfName, csvName, output_format='csv', pages='all')#, java_options="-Dfile.encoding=UTF8")

        csvFile = open(csvName, 'r')
        spamreader = csv.reader(csvFile, delimiter=',')
        rows = []

        for row in spamreader:
            rows += [[e.replace('\n', ' ') for e in row]]
        csvFile.close()
        csvFileEnd = open(csvName, 'w', newline='')
        write = csv.writer(csvFileEnd, delimiter=',')

        for row in rows:
            write.writerow(row)

        csvFileEnd.close()

        print(f'Успешно: {csvName}')
    except Exception as ex:
        print('Нет файла в директории. Проверьте расширения и имена.\n', ex)

