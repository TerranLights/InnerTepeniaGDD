#!/usr/bin/env python3
"""Insert rows at the end of the token log's 'Per notification' table. usage: tokrow.py '<row>' ['<row>' ...]"""
import sys
p='/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/TOKEN_LOG_Ariun_Nuur.md'
L=open(p).read().split('\n')
i=L.index('## Per unit (filled when each unit is recorded)')
j=i-1
while L[j].strip()=='' : j-=1
L[j+1:j+1]=sys.argv[1:]
open(p,'w').write('\n'.join(L)); print('inserted',len(sys.argv)-1,'after line',j+1)
