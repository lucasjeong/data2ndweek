import csv, codecs

filename = "부평구 굴포천 모니터링결과_20200721.csv"
file = codecs.open(filename, "r", "euc_kr")
reader = csv.reader(file, delimiter=",", quotechar='"')

for cells in reader:
    print(cells[:11])