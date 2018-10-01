import socket


def client_HELP():
    
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
                "12.) stop --> ndal klientin dhe ChangeHost --> për të ndryshuar hostin... \n"
                "----------------------------------------------------------------------------------------------------------------------"]
    for i in Sherbimet:
       print(i)


def ifServerconnected(): # ky funksion eshte definuar per te lehtesuar punen e rastit te riperseritjes se veprimeve
        clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # keshtu qe funksioni perdoret ne menyre rekursive dhe e kryen kete pune 
        message="abc"
        serverConnected=False

        while serverConnected==False:
                serverName=input("Emri i Serverit: ")
                if serverName=="":
                        print('Nuk keni shenuar emrin e  serverit, ju lutem shenojeni sepse nuk mund te vazhdoni tutje...')
                        serverName=input("Emri i Serverit: ")
                serverPort=input("Porti: ")
                if serverPort=="":
                        print('Nuk keni shenuar portin, ju lutem shenojeni sepse nuk mund te vazhdoni tutje...')
                        serverPort=input("Porti: ")
                
                print('\n----------------------------------------------------------------------------------------------------------------------')
                try:         
                    server_address=(serverName,int(serverPort))
                    clientSocket.connect(server_address)#connectohet klienti me server
                    print('Jeni lidhur me serverin %s ne portin %s' % server_address)
                    print('----------------------------------------------------------------------------------------------------------------------\n')

                    serverConnected=True #serveri eshte connectuar keshtu qe nderron variabla boolean ne True ne menyre qe te mos perseritet unaza while prap
                except:
                    print('\n????????????????????????????              Nuk u arrit lidhja me serverin...              ?????????????????????????????')
                    print('\n                                                 PROVONI PERSERI...')
        
        numeruesiDeshtimeve=0

        while message!="stop":
                message=input('- Shëno kërkesën: ') #kerkesa mirret nga klienti me ane te inputit ne console
               
                try:
                    if message=="HELP":
                       client_HELP() 
                       message=input('- Shëno kërkesën: ')
                    elif message=='':
                        print('Ju nuk keni shënuar kërkesën, ju lutem shënoni një kërkesë për të marrë përgjigje nga serveri...')
                        message=input('- Shëno kërkesën: ')

                    elif message=="ChangeHost":
                        print('Ju keni kërkuar të ndërroni hostin...\n')                      
                        print('------------------------------------------         Lidhja e re...          -------------------------------------------\n')
                        ifServerconnected()
                        
                    elif len(message)>128:
                        print('Ju keni shënuar si kërkesë një fjali me numer shumë të madh të karaktereve, një gjë e tillë nuk lejohet, ju lutem shënoni një kërkesë më të shkurtër...')
                        message=input('- Shëno kërkesën: ')
                    clientSocket.sendall(str.encode(message))
                    data=clientSocket.recv(1024).decode("utf-8") #mirren të dhënat nga serveri dhe dekodohen 
                    print('Përgjigja:',data) #shfaqen tw dhenat ne console
                    print('\n----------------------------------------------------------------------------------------------------------------------\n')
                    
                except socket.error:
                    print('Dështoi dërgimi i kërkesës në server...')
            
                    numeruesiDeshtimeve+=1
                    if numeruesiDeshtimeve==3:# numeruesi i deshtimeve eshte krijuar ne ate menyre qe pas 3 deshtimeve te riconnectohet klienti me server
                        print('\n---------------------------------           KONTROLLO LIDHJEN ME SERVER           ------------------------------------\n')
                        serverConnected=False
                        clientSocket.close()# nese lidhja me server deshton atehere mbyllet soketi klientit per tu hapur perseri me thirrjen e funksionit ifServerconnected()
                        ifServerconnected(serverConnected)# nese perçfaredo arsye deshton lidhja me server, atehere eshte mundesia qe te riconnectohet klienti pa u mbyllur dritarja e klientit
                    clientSocket.close()

        
        clientSocket.close()  #mbyllet socketi

try:
    ifServerconnected() #thirret funksioni
except Exception:
    print("Diqka shkoi gabim!")
    ifServerconnected()
       
       

    