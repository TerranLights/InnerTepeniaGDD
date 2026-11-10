# Rows typed by hand from SPEC L32-76: name, share, C1 robots, C1 humans, C2 robots, C2 humans
rows = [
("Japan",10.42,64576,61547,37862,47318),
("Sinian Federation",9.72,60212,57384,35301,44117),
("United Kingdom",9.36,58019,55294,34015,42509),
("Germany",8.54,52951,50465,31046,38799),
("Korea",8.35,51763,49332,30349,37925),
("Indonesia",5.74,35590,33922,20870,26081),
("Australia",5.74,35573,33902,20857,26062),
("Thailand",3.23,19989,19050,11719,14645),
("Vietnam",3.10,19228,18326,11274,14088),
("Philippines",3.06,18995,18103,11138,13918),
("Malaysia",2.95,18293,17436,10726,13404),
("Taiwan",2.86,17743,16910,10403,13000),
("Russia (core state)",2.78,17232,16423,10103,12628),
("South Africa",2.75,17066,16264,10005,12504),
("Romania",2.51,15573,14842,9130,11409),
("Ukraine",2.20,13620,12979,7986,9979),
("New Zealand",1.69,10461,9970,6133,7666),
("Idelsk-Uralia",1.67,10338,9854,6060,7573),
("Belarus",1.54,9528,9080,5585,6980),
("Kazakhstan",1.45,9010,8587,5283,6602),
("Bulgaria",1.42,8825,8411,5175,6468),
("Austro-Bavaria",1.39,8622,8218,5054,6317),
("Lithuania",1.18,7306,6963,4284,5354),
("Estonia",1.17,7247,6908,4249,5311),
("Latvia",0.89,5494,5236,3221,4025),
("Manchuria",0.71,4402,4195,2581,3225),
("Siberia",0.66,4108,3915,2409,3011),
("Donska-Kubania",0.64,3940,3756,2310,2885),
("Mongolia",0.40,2457,2343,1442,1800),
("Kunnarantaiga",0.38,2374,2262,1392,1739),
("East Turkestan",0.34,2076,1979,1218,1520),
("Hungary",0.29,1786,1702,1048,1310),
("Northern Ireland",0.23,1408,1341,825,1032),
("Dagestan",0.12,729,695,428,534),
("West Papua",0.100,614,586,362,451),
("Aceh",0.096,595,567,350,435),
("Patani",0.095,585,557,344,427),
("Chechnya",0.056,349,331,204,254),
("Tibet",0.047,293,279,170,215),
("Kabardino-Balkaria",0.034,208,197,122,152),
("North Ossetia-Alania",0.026,158,151,93,116),
("Finland",0.020,123,117,72,90),
("Ingushetia",0.019,118,112,68,86),
("Karachay-Cherkessia",0.018,109,103,63,80),
("Tuva",0.013,78,74,45,57),
]
print("rows", len(rows))
c1r=sum(r[2] for r in rows); c1h=sum(r[3] for r in rows); c2r=sum(r[4] for r in rows); c2h=sum(r[5] for r in rows)
print("C1 robots",c1r,"humans",c1h,"total",c1r+c1h)
print("C2 robots",c2r,"humans",c2h,"total",c2r+c2h)
print("share sum", round(sum(r[1] for r in rows),3))
for lim in (0.1,0.5,1.0):
    sub=[r for r in rows if r[1]<lim]
    print(f"under {lim}%: {len(sub)} rows; C1 sizes {min(r[2]+r[3] for r in sub)} to {max(r[2]+r[3] for r in sub)}; C2 sizes {min(r[4]+r[5] for r in sub)} to {max(r[4]+r[5] for r in sub)}; C1 people in band {sum(r[2]+r[3] for r in sub)}")
print("--- per row C1 total, C1 humans, C2 total, C2 humans (rows under 1%)")
for r in rows:
    if r[1]<1.0:
        print(f"{r[0]:22s} C1 {r[2]+r[3]:6d} (h {r[3]:5d}) C2 {r[4]+r[5]:6d} (h {r[5]:5d})")
print("largest row C1", rows[0][0], rows[0][2]+rows[0][3])
print("Australia C1", rows[6][2]+rows[6][3])
# rows by size band at C1
bands=[(0,500),(500,1000),(1000,5000),(5000,10000),(10000,50000),(50000,10**9)]
for lo,hi in bands:
    n=[r for r in rows if lo<= r[2]+r[3] <hi]
    print(f"C1 size {lo}-{hi}: {len(n)} rows")
for lo,hi in bands:
    n=[r for r in rows if lo<= r[4]+r[5] <hi]
    print(f"C2 size {lo}-{hi}: {len(n)} rows")
# successor groups from CENSUS E
russia=["Chechnya","Dagestan","Donska-Kubania","Finland","Idelsk-Uralia","Ingushetia","Kabardino-Balkaria","Karachay-Cherkessia","Kunnarantaiga","North Ossetia-Alania","Russia (core state)","Siberia","Tuva"]
china=["East Turkestan","Manchuria","Mongolia","Sinian Federation","Tibet"]
d={r[0]:r for r in rows}
for name,grp in (("Russia successors",russia),("China pieces",china)):
    present=[g for g in grp if g in d]
    print(name, len(present), "of", len(grp), "present; C1 total", sum(d[g][2]+d[g][3] for g in present), "share", round(sum(d[g][1] for g in present),3))
