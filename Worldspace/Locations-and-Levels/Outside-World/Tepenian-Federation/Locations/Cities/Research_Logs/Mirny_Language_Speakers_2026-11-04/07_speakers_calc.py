# Mirny: speaker-capable share by language = sum over nations of (nation share x share of that nation's people who can function in the language)
share={'United Kingdom':13.73,'Northern Ireland':0.32,'Australia':6.96,'New Zealand':4.22,'Philippines':4.24,'Malaysia':3.44,'South Africa':1.47,
'Sinian Federation':12.00,'Taiwan':2.86,'Manchuria':0.91,'Mongolia':0.48,'East Turkestan':0.43,'Tibet':0.06,'Korea':13.71,'Japan':7.81,
'Indonesia':12.03,'West Papua':0.21,'Aceh':0.20,'Thailand':3.39,'Patani':0.10,'Vietnam':1.65,
'Idelsk-Uralia':2.14,'Russia (core state)':2.14,'Siberia':0.85,'Donska-Kubania':0.81,'Kunnarantaiga':0.49,'Finland (Karelia)':0.03,
'Belarus':1.49,'Kazakhstan':1.45,'Dagestan':0.15,'Chechnya':0.07,'Kabardino-Balkaria':0.04,'North Ossetia-Alania':0.03,'Ingushetia':0.03,'Karachay-Cherkessia':0.02,'Tuva':0.02}
N=(0,0,0.5)   # "negligible": low 0, best 0, high 0.5 (the research files say <0.5 or <1 each; 0.5 used throughout)
E={ # English
'United Kingdom':(97.5,98.2,98.6),'Northern Ireland':(98.6,99.1,99.5),'Australia':(91.1,96.0,96.6),'New Zealand':(95.1,96.0,97.2),'Philippines':(35,48,56),'Malaysia':(35,50,60),'South Africa':(32,55,64),
'Sinian Federation':(1.3,4.3,7.3),'Taiwan':(3,6,12),'Manchuria':(1,3.5,6),'Mongolia':(1.2,3.0,5.8),'East Turkestan':(0.5,1.5,3),'Tibet':(0.3,1,3),'Korea':(3.3,6.7,13.4),'Japan':(2.5,5,10),
'Indonesia':(3,5,7),'West Papua':(1,2.5,5),'Aceh':(2,4,6.5),'Thailand':(5,10,27),'Patani':(2,4,8),'Vietnam':(5,8,15),
'Idelsk-Uralia':(3,4,12),'Russia (core state)':(5,8,18),'Siberia':(3,4.5,13),'Donska-Kubania':(2.5,4,12),'Kunnarantaiga':(3.5,5.5,13),'Finland (Karelia)':(3,5,13),
'Belarus':(4,8,12),'Kazakhstan':(4,7,10),'Dagestan':(0.7,1.5,2),'Chechnya':(0,1,2),'Kabardino-Balkaria':(0,1,2),'North Ossetia-Alania':(0,1,2),'Ingushetia':(0,1,2),'Karachay-Cherkessia':(0,1,2),'Tuva':(0,1,2)}
R={'Idelsk-Uralia':(98,98.4,99.4),'Russia (core state)':(99.4,99.8,99.9),'Siberia':(99,99.5,99.8),'Donska-Kubania':(99.4,99.8,99.9),'Kunnarantaiga':(99,99.5,99.8),'Finland (Karelia)':(99.4,99.9,99.95),
'Belarus':(90,97,99),'Kazakhstan':(80,85,94),'Dagestan':(87,91,95),'Chechnya':(75,85,95),'Kabardino-Balkaria':(93,97,99),'North Ossetia-Alania':(95,98,99.5),'Ingushetia':(78,88,95),'Karachay-Cherkessia':(93,97,99),'Tuva':(75,85,95),
'Manchuria':(0.1,0.4,1),'Mongolia':(0.7,1.5,3.4),'East Turkestan':(0.1,0.3,1)}
M={'Sinian Federation':(80.5,87.5,92),'Taiwan':(95,96.8,98),'Manchuria':(92,96,99),'Mongolia':(79,84,87),'East Turkestan':(58,66,78),'Tibet':(35,45,55),'Malaysia':(16,19,22),'Australia':(2.7,3.2,4.0),'New Zealand':(2.1,2.6,3.3),
'Indonesia':(0.2,0.5,1.5),'Thailand':(0.5,1.5,3),'Korea':(0,1.5,2),'Japan':(0,1,2),'Kazakhstan':(0,0.1,0.5)}
K={'Korea':(97.3,98.3,99.3),'Kazakhstan':(0,0.3,0.5)}
I={'Indonesia':(94,97,98.1),'West Papua':(88,95,97.3),'Aceh':(95,97.5,98.4),'Patani':(3,10,25)}
J={'Japan':(97.5,98.5,99.5),'Korea':(0.7,1.7,3.4),'Taiwan':(0,0,2)}
Ihi={'Malaysia (Malay counted as Indonesian)':(85,90,95)}
def tot(d,extra=None):
    out=[0,0,0]
    for n,s in share.items():
        v=d.get(n,N)
        for i in range(3): out[i]+=s*v[i]/100
    return out
res={'English':tot(E),'Mandarin':tot(M),'Korean':tot(K),'Indonesian':tot(I),'Russian':tot(R),'Japanese':tot(J)}
print('share total',round(sum(share.values()),3))
for k,v in sorted(res.items(),key=lambda kv:-kv[1][1]): print(f"{k:11s} low {v[0]:6.2f}  best {v[1]:6.2f}  high {v[2]:6.2f}")
# sensitivity: Indonesian incl. Malaysia's Malay speakers (mutual intelligibility)
sens=[x+share['Malaysia']*h/100 for x,h in zip(res['Indonesian'],(85,90,95))]
print('Indonesian incl. Malaysian Malay speakers', [round(x,2) for x in sens])
top=res['English']
print('\n12-point test (speaker shares)')
for k,v in res.items():
    if k=='English': continue
    print(f"English best - {k} best = {top[1]-v[1]:6.2f}   closest case (English LOW - {k} HIGH) = {top[0]-v[2]:6.2f}")
print('closest case with Indonesian incl. Malay:', round(top[0]-sens[2],2))
# also composition-only (old method: whole nation = its language) for reference
print('\nContributions (best), top 8 per language')
for name,d in [('English',E),('Mandarin',M),('Korean',K),('Indonesian',I),('Russian',R),('Japanese',J)]:
    c=sorted(((n,s*d.get(n,N)[1]/100) for n,s in share.items()),key=lambda x:-x[1])
    print(name, '; '.join(f"{n} {v:.2f}" for n,v in c[:8] if v>0.005))
nat=['United Kingdom','Northern Ireland','Australia','New Zealand']
print('English from the four native-English nations (best):', round(sum(share[n]*E[n][1]/100 for n in nat),2),' from all others:', round(res['English'][1]-sum(share[n]*E[n][1]/100 for n in nat),2))
print('Russian: successor states of Russia (13 rows) best:', round(sum(share[n]*R[n][1]/100 for n in R if n not in('Manchuria','Mongolia','East Turkestan','Belarus','Kazakhstan')),2), ' Belarus+Kazakhstan:', round(share['Belarus']*.97+share['Kazakhstan']*.85,2))
print('\nSensitivity: English from native-English nations only')
for i,lab in enumerate(['low','best','high']):
    nat_only=sum(share[n]*E[n][i]/100 for n in nat)
    print(lab,'native-only English',round(nat_only,2),'L2 English elsewhere',round(res['English'][i]-nat_only,2))
nb=sum(share[n]*E[n][1]/100 for n in nat)
for k in ['Mandarin','Korean','Indonesian','Russian','Japanese']:
    print(f"native-only English (best) - {k} best = {nb-res[k][1]:.2f};  L2 English needed for gap > 12: {max(0,res[k][1]+12-nb):.2f}")
