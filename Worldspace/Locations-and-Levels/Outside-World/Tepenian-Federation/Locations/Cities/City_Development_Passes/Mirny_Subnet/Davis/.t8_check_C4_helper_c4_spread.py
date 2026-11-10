# Hand-copied from Specs/Mirny subnet/Davis.md L32-76 (admitted span 10-81), as displayed by Read.
# Columns: name, share, CI robots, CI humans, CII robots, CII humans
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
print("sum share", round(sum(r[1] for r in rows), 4))
s = [sum(r[i] for r in rows) for i in range(2, 6)]
print("sums CI R, CI H, CII R, CII H:", s, "| spec headers: 619764 590668 363374 454101")
hr = [(r[0], r[5] / r[3] * 100) for r in rows]
rr = [(r[0], r[4] / r[2] * 100) for r in rows]
cr = [(r[0], (r[4] + r[5]) / (r[2] + r[3]) * 100) for r in rows]
for label, xs in (("human", hr), ("robot", rr), ("combined", cr)):
    lo = min(xs, key=lambda t: t[1]); hi = max(xs, key=lambda t: t[1])
    print(f"{label} retention: min {lo[1]:.3f} ({lo[0]}), max {hi[1]:.3f} ({hi[0]}), spread {hi[1]-lo[1]:.3f} pp")
# Same restricted to rows of 1% share or more
big = [r for r in rows if r[1] >= 1.0]
for label, f in (("human", lambda r: r[5]/r[3]*100), ("robot", lambda r: r[4]/r[2]*100), ("combined", lambda r: (r[4]+r[5])/(r[2]+r[3])*100)):
    v = [f(r) for r in big]
    print(f"rows >=1%: {len(big)}; {label} spread {max(v)-min(v):.3f} pp")
# Robot:human ratio per row, Census I
ratio = [r[2] / r[3] for r in rows]
print("CI robot/human ratio min/max:", round(min(ratio), 4), round(max(ratio), 4), "city:", round(619764/590668, 4))
# The Sinian Federation draw: stated multiplier 0.5719, range 0.55 to 0.65
sf = 9.72
for d in (0.55, 0.5719, 0.65):
    print(f"draw {d}: Sinian Federation share would be {sf * d / 0.5719:.2f}% (Japan now 10.42%, and Japan's own share falls as the draw rises)")
print("break-even draw if Japan held at 10.42%:", round(10.42 * 0.5719 / sf, 4))
