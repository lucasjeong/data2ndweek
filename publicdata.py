import codecs

filename = "부평구 굴포천 모니터링결과_20200721.csv"
csv = codecs.open(filename, "r", "euc_kr").read()

splitted = csv.split("\n")
for item in splitted:
    list_trip = item.split(",")
    print(list_trip[:11])