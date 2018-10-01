import socket
from datetime import datetime
import random
from _thread import *



def IPADDR(adresa_klientit,LidhjaSOKETIT):
    LidhjaSOKETIT.send(str.encode("IP Adresa e klientit është:"+ adresa_klientit[0])) #kthen IP adresene  klientit ne forme dhjetore me pika
def PORTNR(adresa_klientit,LidhjaSOKETIT):# kthen portin me te cilin eshte lidhur klienti me server
    LidhjaSOKETIT.send(str.encode("Klienti është duke përdorur portin: "+ str(adresa_klientit[1])))
  
def ZANORE(teksti,LidhjaSOKETIT):
   numero=0
   zanoret=set("aeiouy\u00EB") # "aeiouy\x89" quhet RegEx i zanoreve
   for shkronje in teksti:
       if shkronje in zanoret:
           numero+=1
   LidhjaSOKETIT.send(str.encode("Teksti i pranuar përmban "+ str(numero)+ " zanore"))

def PRINTO(teksti,LidhjaSOKETIT):
    try:
       tekstiPaHapsiraFILL=teksti.strip() # ne kete menyre nuk merr hapesirat ne fillim dhe ne fund te fjalise
       LidhjaSOKETIT.send(str.encode(tekstiPaHapsiraFILL))
    except error:
        LidhjaSOKETIT.send(str.encode("Diqka shkoi gabim!"))

def HOST(LidhjaSOKETIT):
    try:
        emriHostit=socket.gethostname()
        LidhjaSOKETIT.send(str.encode("Emri I hostit është "+emriHostit))
    except error:
        LidhjaSOKETIT.send(str.encode("Emri I hostit nuk dihet!"))

def TIME(LidhjaSOKETIT):
    koha=datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    LidhjaSOKETIT.send(str.encode(koha))
def LOJA(LidhjaSOKETIT):
    numratRandom=''
    for i in range(20):
        nrRandom=random.randint(1,99) #gjenerimi i numrave random pre 1 deri 99
        stringRand=str(nrRandom)+" " 
        numratRandom+=stringRand   # ruajtja e 20 numrave random ne varg
    LidhjaSOKETIT.send(str.encode(numratRandom))
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

def POLINDROM(teksti,LidhjaSOKETIT):
    a=False
    for i in range(len(teksti)):
        if teksti[i]==teksti[len(teksti)-1-i]:
            a=True
        else:
            a=False
    if a:
        LidhjaSOKETIT.send(str.encode("Fjala "+teksti+" eshte polindrom"))
    else:
        LidhjaSOKETIT.send(str.encode("Fjala "+teksti+" nuk eshte polindrom"))
def ALFABETI(LidhjaSOKETIT):   
    numero=0
    alfabeti="a,b,c,ç,d,dh,e,ë,f,g,gj,h,i,j,k,l,ll,m,n,nj,o,p,q,r,rr,s,sh,t,th,u,v,x,xh,y,z,zh"  
    alfabetii=alfabeti.split(',')#largon presjet nga stringu alfabeti ne menyre qe mund te bejme manipulime me ate string
    zanoret=set("aeiouy\u00EB") # "aeiouy\x89" quhet RegEx i zanoreve
    for shkronje in alfabetii:
       if shkronje in zanoret:
           numero+=1    
    LidhjaSOKETIT.send(str.encode("\n~ Alfabeti i gjuhës shqipe ka "+str(len(alfabetii))+
                                  " shkronja."+"\n~ Shkronja të mëdha: "+alfabeti.upper()+"\n~ Shkronja të vogla: "+alfabeti+
                                  "\n~ "+str(numero)+" zanore dhe "+str(len(alfabetii)-numero)+" bashkëtingëllore."))

ServeriSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_Port=11000

print('Duke startuar serveri në localhost në portin',str(server_Port))
ServeriSocket.bind(('',server_Port))
ServeriSocket.listen(10) #Serveri degjon lidhjet nga klientet
print('Serveri është i gatshëm të pranoj kërkesa.\n')

#Krijojme funksionin klienti_thread ku edhe thirren te gjitha funksionet e definuara me lart
def threadi_klientit(LidhjaKlientit, adresaKlientit):
    while True:
        try:
            fjalia = LidhjaKlientit.recv(1024).decode("utf-8")#pranohet komanda nga klienti dhe dekodohet me utf-8
            komanda=[]
            komanda=fjalia.split() # e ndajme komanden qe vje nga klienti dhe e ruajme ne forme te string array
            komanda1=fjalia.split(' ',1)# variabel e veqante per funksionin PRINTO dhe ZANORE per shkak se na duhet qe te ndahet
            try:                               #komanda vetem ne SPACE-in e pare dhe pjesa tjeter te mirret si string
                if komanda[0]=="IP":
                        IPADDR(adresaKlientit,LidhjaKlientit)
                elif komanda[0]=="PORT":
                        PORTNR(adresaKlientit,LidhjaKlientit)
                elif komanda[0]=="ZANORE":
                    ZANORE(komanda1[1],LidhjaKlientit)
                elif komanda[0]=="PRINTO":
                     PRINTO(komanda1[1],LidhjaKlientit)
                elif komanda[0]=="HOST":
                    HOST(LidhjaKlientit)
                elif komanda[0]=="TIME":
                    TIME(LidhjaKlientit)
                elif komanda[0]=="LOJA":
                    LOJA(LidhjaKlientit)
                elif komanda[0]=="KONVERTO":
                    if komanda[2].isdigit():
                        LidhjaKlientit.send(str.encode(str( KONVERTO(komanda[1],float(komanda[2])))))
                    else:
                        LidhjaKlientit.send(str.encode(str("Ju Lutem shenoni numer si parameter te KONVERTO")))
                    
                elif komanda[0]=="FIBONACCI":
                    if komanda[1].isdigit():
                        LidhjaKlientit.send(str.encode(str(FIBONACCI(float(komanda[1])))))
                    else:
                        LidhjaKlientit.send(str.encode(str("Ju Lutem shenoni numer si parameter te FIBONACCI")))
                elif komanda[0]=="POLYNDROME":
                    POLINDROM(komanda1[1],LidhjaKlientit)
                elif komanda[0]=="AL-ALPHABET":
                    ALFABETI(LidhjaKlientit)
                else:
                    if komanda[0]=="stop":
                        fjaliaNdihmese="Kërkesa juaj ishte \"stop\" kështuqë klienti u ndal, shtyp ENTER"
                    else:
                        fjaliaNdihmese="Kërkesa juaj nuk është në grupin e shërbimeve që i ofron serveri...\n ~ Shëno HELP si kërkesë që të shihni listen e shërbimeve që i ofron serveri..."
                
                    LidhjaKlientit.send(str.encode(fjaliaNdihmese))                  

            except IndexError:
                     print("Diqka shkoi gabim! Serveri po mbyllet...")
                     LidhjaKlientit.close()
        except OSError:
            LidhjaKlientit.close()
    LidhjaKlientit.close()

while True:
   connectionSocket, adresa_Klientit = ServeriSocket.accept()
   print('Klienti u lidh në serverin %s me port %s' % adresa_Klientit)
   start_new_thread(threadi_klientit,(connectionSocket,adresa_Klientit,))
   

   

   


