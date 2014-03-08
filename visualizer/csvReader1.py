import csv
#import geonamescache
#gc = geonamescache.GeonamesCache()
a=[]
#dt={'state':('year','number')}
with open('Neo-Natal_Mortality_Rate.csv', 'rb') as myFile:
    reader = csv.reader(myFile, delimiter=',', quotechar='|')
    for row in reader:
        print row[0] + '\t' + row[1] + '\t' + row[2] + ' \t' + row[3] + ' \t' + row[4] + '\t' + row[5] + ' \t' + row[6]+ ' \t' + row[7] + '\n'
        a.append(row[1])
    print a

