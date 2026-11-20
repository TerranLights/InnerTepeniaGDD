#!/usr/bin/env python3
"""Build the Step 8 reading lists and frozen briefs. usage: build.py <errata_span e.g. 600-900>"""
import sys, re, hashlib
G="/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/"
U=G+"Worldspace/Locations-and-Levels/Universal_Location_Methodology/"
P=G+"Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/"
S="/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/f3e3ba60-3018-46e7-b33a-2aecaa179ab5/scratchpad/t8/"
span=sys.argv[1]
common=[U+"00_RUNBOOK.md :: 2978-3005", U+"Disciplines/00f_Review_Panel.md :: 1-2,4-85,87-834", P+"Datasheets/Step_8.md",
        P+"00.2_Position_Coverage_Ledger.md", P+"07_QA_Gates.md :: "+span, U+"DEVELOPER_RULINGS_LOG.md :: 2058-2065"]
units={
 "R1":("the frame, the spine, Phases 2–4",
       [P+"00_Frame.md :: 1-282,301-343,412-431", P+"02_Spine.md :: 57-424", P+"04_Phase_02_Composition_and_Arrival.md :: 1-29,97-424,512-533",
        P+"04_Phase_03_Surface_and_Texture.md :: 1-30,106-411,519-547", P+"04_Phase_04_Ordinary_Life.md :: 1-26,164-474,595-622"],
       "7 the frame; 8 the spine (§1–§8); 9 Phase 2; 10 Phase 3; 11 Phase 4"),
 "R2":("Phases 5–8, with the spine's shape",
       [P+"02_Spine.md :: 233-272", P+"04_Phase_05_Relation_and_Geometry.md :: 1-29,255-624", P+"04_Phase_06_Meaning.md :: 1-38,132-608",
        P+"04_Phase_07_Order.md :: 1-87,256-1020,1117-1156", P+"04_Phase_08_Making.md :: 1-25,126-384"],
       "7 the spine's shape (§5); 8 Phase 5; 9 Phase 6; 10 Phase 7; 11 Phase 8"),
 "R3":("Phases 9–10 and the Step 5 reconciliation, with the spine's shape",
       [P+"02_Spine.md :: 233-272", P+"04_Phase_09_Populations.md :: 1-28,193-520", P+"04_Phase_10_Catalog.md :: 1-47,236-465,579-1107,1197-1933",
        P+"05_Reconciliation.md :: 1-914,1023-1491"],
       "7 the spine's shape (§5); 8 Phase 9; 9 Phase 10; 10 Step 5 (stage A and stage B)"),
}
tmpl=open(S+"step8_brief_template.md").read()
q1=open(P+".t8_brief_07_Step7Q1.md").read()
standing=q1.split("## 1 · Standing lines (copied from `T8_Standing_Brief_Lines.md`; the wording is the contract)\n",1)[1].split("\n## 2 · ",1)[0].strip("\n")
task=open(S+"step8/task.md").read().strip("\n")
for u,(scope,files,ents) in units.items():
    lst=common+files+[P+".t8_Step8_findings_index.md"]
    open(P+f".t8_required_08_Step8{u}.txt","w").write("\n".join(lst)+"\n")
    b=tmpl.replace("{U}",u).replace("{SCOPE}",scope).replace("{N}",str(len(lst))).replace("{ENTRIES}",ents).replace("{STANDING}",standing).replace("{TASK}",task)
    assert "{" not in re.sub(r"`[^`]*`","",b).replace("{N}",""), [m for m in re.findall(r"\{[A-Z]+\}",b)]
    fn=P+f".t8_brief_08_Step8{u}.md"; open(fn,"w").write(b)
    print(u, len(lst), "entries;", len(b.splitlines()), "lines; sha256[:16]", hashlib.sha256(b.encode()).hexdigest()[:16])
