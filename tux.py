#!/usr/bin/python
#code by Vampy Security
#pagina oficial https://vampysecurity.github.io/vampysecurity/
import  os
import  webbrowser


print "  __                    \n";
print "_/  |_ __ _____  ____ \n";
print "\   __\  |  \  \/  / \n";
print " |  | |  |  />    <     \n";
print " |__| |____//__/\_ \  \n";
print "                  \/  \n";

print "\0          ======================================================\n";
print "\0                           VISIT US ON FACEBOOK:                  \n";
print "\0                 pagina de fb https://www.facebook.com/Killing-Dial-Hackers-108107518448497     \n";
print "\0                 grupo de fb https://www.facebook.com/groups/648748639880339    \n";
print "\0                 grupo de telegram https://t.me/+h6n724JdyF8wOTNh    \n";
print "\0                 canal de yt https://www.youtube.com/channel/UCpCPdnAmsB7DcR7o6vxV04A    \n";
print "\0                            Hecho por [[Vampy Security]]                 \n";
print "\0         ========================================================\n";

print "\0          ======================================================\n";
print "\0               Usar: python tux.py seleciona el numero";
print "\0          ======================================================\n";
print "\n";
print("solamente elige la opcion deseada")
print("menu")
print("")
print ("1.- pagina de la NSA")
print("2.- pagina de la CIA")
print("3.- instalar nmap en termux")
print("4.- instalar lenguajes de programacion en termux")
print("5.- complementos de termux")
opcion = int(input("introduce el num deseado:   "))
if opcion == 1:
	webbrowser.open('https://nsa.gov')
elif opcion == 2:
	webbrowser.open('https://cia.gov')
elif opcion == 3:
	os.system('apt install nmap -y')
elif opcion == 4:
	os.system('apt install python python2 perl php ruby -y')
elif opcion == 5:
	os.system('apt install git curl wget vim -y')
else:
	print("esta opcion no es validad judio")