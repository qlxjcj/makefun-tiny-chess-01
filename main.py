import json,os,urllib.request as R
U=os.environ["MAKEFUN_ENV_URL"]
NB=165000;ST=[]
def P(p,x):
 for i in"1234":
  try:return json.load(R.urlopen(U+p,json.dumps(x).encode(),timeout=9))
  except:pass
 return{"error":1}
B=[0]*128;S=1;EP=0
ND=(-33,-31,-18,-14,14,18,31,33);BD=(-17,-15,15,17);RD=(-16,-1,1,16);KD=BD+RD
SL=(0,0,ND,BD,RD,KD,KD);VAL=(0,100,320,330,500,900,0)
W=" pnbrqk"
PS=(b"@@@@ABB<A?>@@@@DAABEBBDFJJJJ@@@@"b"68::8<@A:ABC:@CD:ACD:@BC8<@@68::"b">????@@@?@AB?AAB?@BB?ABB?@@@>@@@"b"DFB@DD@@><<<<::8:886:886:886:886")
M=[0,1,2,3,3,2,1,0]*16
G=[0]*1792
for f in range(128):
 for p in range(1,7):
  for w in(1,-1):
   r=w*(f>>4)+(w<0)*7
   G[f*14+p*w+7]=w*VAL[p] if p in(4,5) else w*(VAL[p]+(PS[32*(p-1 if p<4 else 3)+r*4+M[f]]-64)*5)
def att(f,a):
 for o in ND+BD+RD:
  x=f+o
  if x&136<1 and B[x]==a*(6-(o in ND)*4):return 1
 for o in(15,17):
  x=f-o*a
  if x&136<1 and B[x]==a:return 1
 for ds,ty in((BD,3),(RD,4)):
  for o in ds:
   x=f+o
   while x&136<1:
    v=B[x]
    if v and v in(a*ty,a*5):return 1
    if v:break
    x+=o
 return 0
def gen():
 g=[]
 for f,p in enumerate(B):
  if(t:=p*S)<=0:continue
  if t==1:
   d=f+16*S
   if d&136<1 and not B[d]:
    g+=[(f,d,5*(d&112 in(0,112)))]
    if f&112==16+80*(S<0)and not B[e:=d+16*S]:g+=[(f,e,0)]
   for x in(f+15*S,f+17*S):
    if x&136<1 and(B[x]*S<0 or x==EP>0):g+=[(f,x,5*(x&112 in(0,112)))]
  elif t in(2,6):
   for o in SL[t]:
    x=f+o
    if x&136<1 and B[x]*S<=0:g+=[(f,x,0)]
  else:
   for o in SL[t]:
    x=f+o
    while x&136<1:
     v=B[x]
     if v*S<0:g+=[(f,x,0)]
     if v:break
     g+=[(f,x,0)]
     x+=o
 return g
def mk(m):
 global S,EP
 f,t,pr=m
 p=B[f]
 if t==EP>0 and abs(p)==1 and not B[t]:
  v=B[t-16*S];B[t-16*S]=0
 else:v=B[t]
 B[f]=0
 B[t]=pr*S or p
 if p*p==36 and abs(t-f)==2:
  d=(t>f)*2-1
  B[f+d]=B[t+d];B[t+d]=0
 ST.append((EP,v))
 EP=(t-16*S)*(abs(p)==1<abs(t-f)==32)
 S=-S
def um(m):
 global S,EP
 f,t,pr=m
 S=-S
 ep,v=ST.pop()
 p=B[t]
 if pr:p=(p>0)*2-1
 if t==ep>0 and abs(p)==1<abs(t-f)in(15,17):
  B[t]=0;B[t-16*S]=v
 else:B[t]=v
 B[f]=p
 if p*p==36 and abs(t-f)==2:
  d=(t>f)*2-1
  B[t+d]=B[f+d];B[f+d]=0
 EP=ep
def ev():
 s=0
 for f,p in enumerate(B):
  if p:s+=G[f*14+p+7]
 return s*S
nodes=BUD=0;T={};H={}
def so(m):return-1e9 if m==TM else(VAL[abs(B[m[0]])]or 500)-9*abs(B[m[1]])-700*m[2]
hk=lambda:hash((S,EP,*B))
def neg(d,a,b,ply):
 global nodes,TM
 nodes+=1
 if nodes>BUD:raise KeyError
 r=T.get(k:=hk());A=a;TM=r and r[3]or 0
 if r and r[0]>=d and(r[1]or not a<r[2]<b):return r[2]
 ko=B.index(6*S)
 ch=att(ko,-S)
 if ch*d:d+=1
 ms=gen()
 if d<1:
  if ply>99:return ev()
  if not ch:
   if(st:=ev())>=b:return st
   a=max(a,st)
   ms=[m for m in ms if B[m[1]]+m[2]]
 made=bm=0
 ms.sort(key=so)
 for m in ms:
  pm=B[m[0]];mk(m)
  if att((ko,m[1])[abs(pm)==6],S):
   um(m);continue
  made=1
  s=-neg(d-1,-b,-a,ply+1)
  um(m)
  if s>a:a=s;bm=m
  if a>=b:T[k]=(d,0,a,m);return a
 if not made and(d>0 or ch):return-99999+ply if att(ko,-S)else 0
 T[k]=(d,a>A,a,bm);return a
def st(fn):
 global S,EP
 q=fn.split()
 B[:]=[0]*128
 for r,row in enumerate(q[0].split("/")):
  f=0
  for c in row:
   if c.isdigit():f+=int(c)
   else:B[(7-r)*16+f]=W.index(c.lower())*(1-2*(c>="a"));f+=1
 S=1-2*(q[1]=="b")
 e=q[3];EP=0 if e<"0"else ord(e[0])-97+16*(int(e[1])-1)
def u(m):
 f,t,pr=m
 return"%c%d%c%d%s"%(97+f%8,f//16+1,97+t%8,t//16+1,pr and W[pr]or"")
def pu(s):o=ord;return((o(s[1])-49)*16+o(s[0])-97,(o(s[3])-49)*16+o(s[2])-97,W.index(s[4:5].lower()))
def ch(g):
 global nodes,BUD,TM
 st(g["fen"])
 L=list(map(pu,g["legal_moves"]))
 nodes=0;BUD=NB;ST.clear();T.clear();TM=0
 R={}
 best=L[0]
 for d in range(1,60):
  a=-1e5
  if d>1:L.sort(key=R.__getitem__)
  try:
   for m in L:
    mk(m)
    s=0 if hk() in H else-neg(d-1,-1e5,-a,1)
    um(m);R[m]=-s
    if s>a:a=s;best=m
  except KeyError:st(g["fen"]);break
  if abs(a)>98999:break
 mk(best);H[hk()]=0;um(best);return u(best)
g=P("/game",{})
while not g.get("error")and g.get("status")!="done":
 if g.get("status")=="your_move":
  g=P("/move",{"game":g["game"],"move":ch(g)if g.get("legal_moves")else"0000"})
 else:g=P("/game",{})
