import socket
from datetime import datetime
import random
from _thread import *

def IPADDR(LidhjaSOKETIT,adresa_klientit,):
    LidhjaSOKETIT.sendto(str.encode("IP Adresa e klientit eshte:"+ adresa_klientit[0]),adresa_klientit)

def PORTNR(LidhjaSOKETIT,adresa_klientit):
    LidhjaSOKETIT.sendto(str.encode("Klienti eshte duke perdorur portin: "+ str(adresa_klientit[1])),adresa_klientit)
  
def ZANORE(LidhjaSOKETIT,teksti,adresaKlientit):
   numero=0
   zanoret=set("aeiouy\u00EB")
   for shkronje in teksti:
       if shkronje in zanoret:
           numero+=1
   LidhjaSOKETIT.sendto(str.encode("Teksti i pranuar permban "+ str(numero)+ " zanore"),adresaKlientit)
def PRINTO(LidhjaSOKETIT,teksti,adresaKlientit):
    try:
       tekstiPaHapsiraFILL=teksti.strip() # ne kete menyre nuk merr hapesirat ne fillim dhe ne fund te fjalise
       LidhjaSOKETIT.sendto(str.encode(tekstiPaHapsiraFILL),adresaKlientit)
    except error:
        LidhjaSOKETIT.sendto(str.encode("Diqka shkoi gabim!"),adresaKlientit)
def HOST(LidhjaSOKETIT,adresaKlientit):
    try:
        emriHostit=socket.gethostname()
        LidhjaSOKETIT.sendto(str.encode("Emri I hostit eshte "+emriHostit),adresaKlientit)
    except error:
        LidhjaSOKETIT.sendto(str.encode("Emri I hostit nuk dihet!"),adresaKlientit)
def TIME(LidhjaSOKETIT,adresaKlientit):
    koha=datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    LidhjaSOKETIT.sendto(str.encode(koha),adresaKlientit)
def LOJA(LidhjaSOKETIT,adresaKlientit):
    numratRandom=''
    for i in range(20):
        nrRandom=random.randint(1,99) #gjenerimi i numrave random pre 1 deri 99
        stringRand=str(nrRandom)+" " 
        numratRandom+=stringRand   # ruajtja e 20 numrave random ne varg
    LidhjaSOKETIT.sendto(str.encode(numratRandom),adresaKlientit)
def FIBONACCI(n):
     if n<=1:
         return n
     else:
         return(FIBONACCI(n-1)+FIBONACCI(n-2))
def KONVERTO(a,b): #a=> stringu b=>numri       
    if a=="CelsiusToKelvin":
        return b+273.15
    elif a=="CelsiusToFahrenheit":
        return (9/5*b+32)
    elif a=="KelvinToFahrenheit":
        return (9/5*(b-273.15)+32)
    elif a=="KelvinToCelsius":
        return (b-273.15)
    elif a=="FahrenheitToCelsius":
        return ((b-32)*5/9)
    elif a=="FahrenheitToKelvin":
        return (5/9*(b-32)+273.15)
    elif a=="PoundToKilogram":
        return (b/2.2)
    elif a=="KilogramToPound":
        return (b*2.2)
def POLINDROM(LidhjaSOKETIT,teksti,adresaKlientit):
    a=False
    for i in range(len(teksti)):
        if teksti[i]==teksti[len(teksti)-1-i]:
            a=True
        else:
            a=False

    if a:
        LidhjaSOKETIT.sendto(str.encode("Fjala "+teksti+" eshte polindrom"),adresaKlientit)
    else:
        LidhjaSOKETIT.sendto(str.encode("Fjala "+teksti+" nuk eshte polindrom"),adresaKlientit)
def ALFABETI(LidhjaSOKETIT,adresa_klientit):   
    numero=0
    alfabeti="a,b,c,ç,d,dh,e,ë,f,g,gj,h,i,j,k,l,ll,m,n,nj,o,p,q,r,rr,s,sh,t,th,u,v,x,xh,y,z,zh"  
    alfabetii=alfabeti.split(',')#largon presjet nga stringu alfabeti ne menyre qe mund te bejme manipulime me ate string
    zanoret=set("aeiouy\u00EB") # "aeiouy\x89" quhet RegEx i zanoreve
    for shkronje in alfabetii:
       if shkronje in zanoret:
           numero+=1    
    LidhjaSOKETIT.sendto(str.encode("\n~ Alfabeti i gjuhës shqipe ka "+str(len(alfabetii))+
                                  " shkronja."+"\n~ Shkronja të mëdha: "+alfabeti.upper()+"\n~ Shkronja të vogla: "+alfabeti+
                                  "\n~ "+str(numero)+" zanore dhe "+str(len(alfabetii)-numero)+" bashkëtingëllore."),adresa_klientit)
    #krijojme(hapim) socketin per server UDP
ServeriSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_Port=11000

print('Duke startuar serveri ne localhost ne portin',str(server_Port))
ServeriSocket.bind(('localhost',server_Port))
print('Serveri eshte i gatshem te pranoj kerkesa.\n')
   
while True:
   request, adresa_Klientit = ServeriSocket.recvfrom(1024)
   request=request.decode('utf-8')
   print('Klienti u lidh ne serverin %s me port %s' % adresa_Klientit)
   
   komanda=[]
   komanda=request.split() # e ndajme komanden qe vje nga klienti dhe e ruajme ne forme te string array
   komandaperPrint=request.split(' ',1)# variabel e veqante per funksionin PRINTO per shkak se na duhet qe te ndahet
   try:                               #komanda vetem ne SPACE-in e pare dhe pjesa tjeter te mirret si string
        if komanda[0]=="IP":
                IPADDR(ServeriSocket,adresa_Klientit)
        elif komanda[0]=="PORT":
                PORTNR(ServeriSocket,adresa_Klientit)
        elif komanda[0]=="ZANORE":
            ZANORE(ServeriSocket,komanda[1],adresa_Klientit)
        elif komanda[0]=="PRINTO":
                PRINTO(ServeriSocket,komandaperPrint[1],adresa_Klientit)
        elif komanda[0]=="HOST":
            HOST(ServeriSocket,adresa_Klientit)
        elif komanda[0]=="TIME":
            TIME(ServeriSocket,adresa_Klientit)
        elif komanda[0]=="LOJA":
            LOJA(ServeriSocket,adresa_Klientit)
        elif komanda[0]=="KONVERTO":
            ServeriSocket.sendto(str.encode(str( KONVERTO(komanda[1],float(komanda[2])))),adresa_Klientit)
        elif komanda[0]=="FIBONACCI":
            ServeriSocket.sendto(str.encode(str(FIBONACCI(float(komanda[1])))),adresa_Klientit)
        elif komanda[0]=="POLYNDROME":
            POLINDROM(ServeriSocket,komanda[1],adresa_Klientit)
        elif komanda[0]=="AL-ALPHABET":
            ALFABETI(ServeriSocket,adresa_Klientit)
        else:
            if komanda[0]=="stop":
                fjaliaNdihmese="Kerkesa juaj ishte \"stop\" keshtuqe klienti u ndal, shtyp ENTER"
            else:
                fjaliaNdihmese="Kërkesa juaj nuk është në grupin e shërbimeve që i ofron serveri...\n ~ Shëno HELP si kërkesë që të shihni listen e shërbimeve që i ofron serveri..."
       
            ServeriSocket.sendto(str.encode(fjaliaNdihmese),adresa_Klientit)

   except IndexError:
                print("Diqka shkoi gabim! Serveri po mbyllet...")
                     
       



   
