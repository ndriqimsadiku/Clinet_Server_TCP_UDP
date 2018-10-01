import socket


def client_HELP(): #funksioni qe permban te gjitha metodat e projektit si forme string array 
    Sherbimet = [               
                "----------------------------------------------------------------------------------------------------------------------",
                "Serveri ofron përgjigje për këto kërkesa:",
                "1.) IP -->kthen IP adresën", 
                 "2.) PORT -->kthen portin",
                "3.) ZANORE<hapësirë>fjalia -->kthen numrin e zanoreve në fjali",
                "4.) PRINTO<hapësirë>fjalia -->kthen fjalinë pa hapësira në fillim dhe në fund",
                "5.) HOST -->kthen hostin",
                "6.) TIME -->kthen kohën aktuale ",
                "7.) LOJA -->kthen 20 numra të rastësishëm prej 1 deri 99 ",
                "8.) FIBONACCI<hapësirë>Numër -->kthen numrin FIBONACCI si rezultat i parametrit të dhënë hyrës ",
                "9.) KONVERTO <hapësirë> Opcioni <hapësirë> Numër -->Kthen si rezultat konvertimin e opcioneve varësisht opcionit të zgjedhur: ",
                "  - Lista e parametrave opcioni janë:",
                "      CelsiusToKelvin",
                "      CelsiusToFahrenheit",
                "      KelvinToFahrenheit",
                "      KelvinToCelsius",
                "      FahrenheitToCelsius",
                "      FahrenheitToKelvin",
                "      PoundToKilogram",
                "      KilogramToPound",
                "10.) POLYNDROME<hapësirë>fjalia --> Kthen a është fjalia e shënuar polindrom apo jo ",
                "11.) AL-ALPHABET --> kthen alfabetin Shqip me shkronja të mëdha dhe të vogla",
                "12.) stop --> ndal klientin dhe ChangeHost --> për të ndryshuar hostin..."
                "----------------------------------------------------------------------------------------------------------------------"]
    for i in Sherbimet: #printimi i te gjitha metodave ne console
       print(i)

def ifServerconnected(): 
    #krijojme socketin per klient UDP
        clientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        message="abc"
        serverConnected=False

        while serverConnected==False:# nese clienti nuk eshte connectuar me server unaza perseritet deri ne connectimin e tij
                serverName=input("Emri i Serverit: ") #emri i serverit permes ketij inputi mirret nga consola
                if serverName=="":
                        print('Nuk keni shenuar emrin e  serverit, ju lutem shenojeni sepse nuk mund te vazhdoni tutje...')
                        serverName=input("Emri i Serverit: ")
                serverPort=input("Porti: ") #edhe porti i serverit mirret nga consola permes ketij inputi
                if serverPort=="":
                        print('Nuk keni shenuar portin, ju lutem shenojeni sepse nuk mund te vazhdoni tutje...')
                        serverPort=input("Emri i Serverit: ")                
                print('\n----------------------------------------------------------------------------------------------------------------------\n')
                try:         
                    server_address=(serverName,int(serverPort)) #emri dhe porti i marrur me input bashkohen ne nje variabel                   
                    print('Jeni lidhur me serverin %s në portin %s' % server_address)
                    serverConnected=True
                except:
                    print('\n???????????????????????              Nuk u arrit lidhja me serverin...              ??????????????????????????????????')
                    print('\n                                            PROVONI PERSERI...')
        
        numeruesiDeshtimeve=0

        while message!="stop":
                message=input('- Shëno kërkesën: ')
               
                try:
                    if message=="HELP":
                       client_HELP() 
                       message=input('- Shëno kërkesën: ')
                    elif message=='':
                        print('Ju nuk keni shënuar kërkesën, ju lutem shënoni një kërkesë për të marrë përgjigje nga serveri...')
                        message=input('- Shëno kërkesën: ')
                    elif message=="ChangeHost":
                        print('Ju keni kërkuar të ndërroni hostin...')                      
                        print('------------------------------------------         Lidhja e re...          -------------------------------------------\n')
                        ifServerconnected()
                    elif len(message)>128:
                        print('Ju keni shënuar si kërkesë një fjali me numer shumë të madh të karaktereve, një gjë e tillë nuk lejohet, ju lutem shënoni një kërkesë më të shkurtër...')
                        message=input('- Shëno kërkesën: ')
                   
                        #kerkesa dergohet ne server
                    clientSocket.sendto(str.encode(message),server_address)

                    #te dhenat pranohen nga serveri- pergjigja e serverit
                    
                    data,addresa=clientSocket.recvfrom(1024)
                    data=data.decode('utf-8')
                    print('Përgjigja:',data)
                    print('\n----------------------------------------------------------------------------------------------------------------------\n')
                    
                except socket.error:
                    print('Dështoi dërgimi i kërkesës në server...')
            
                    numeruesiDeshtimeve+=1
                    if numeruesiDeshtimeve==3:
                        print('\n---------------------------------           KONTROLLO LIDHJEN ME SERVER           ------------------------------------\n')
                        serverConnected=False                        
                        ifServerconnected()
try:
    ifServerconnected()
except Exception:
    print("Diqka shkoi gabim!")
    print('----------------------------------------------------------------------------------------------------------------------\n')

    ifServerconnected()
       
       

    
