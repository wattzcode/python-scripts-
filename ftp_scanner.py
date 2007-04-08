#! /usr/bin/evn python
'''this script is desiged to use the tcp full conection to determine
the status of port 21 on systems, by aending certain mount of data it
can receive data in form of a banner containing details about the scanned
ftp server. you only have to supply the script with an ip addr and it
will attempt to connect using the defualt ftp port 21'''

from socket import *
import optparse
from time import *

#creating a fuction that will try to connect to the remote machine 
#using the ip addr & the port to determine the status of the port

def connect(host):
   port = 21
   t1=time()
   try:
       #socket 0bject to handle tcp connections
       socket_obj = socket(AF_INET, SOCK_STREAM)
       socket_obj.connect((host,port))
       #the object sends data to the port to receive a banner that will contain the de#tails of the ftp server
       socket_obj.send("sending packets")
       banner = socket_obj.recv(200)
       print'[+] ftp server banner: ' + banner
       print'[+] ftp port %d is open ' % port
   except:
       print'[-] ftp port %d closed ' % port
   t2=time()
   print'scanning took %s seconds' % (t2-t1) #will print the processing time taken while scanning

#the main subroutine contains optionparser methods used to read command line arg

def main():
   pars_obj = optparse.OptionParser('usage:'+'Ftp vul scanner \n   -H < host ip addr >')
   pars_obj.add_option('-H', dest='host', type='string')
   #parser object creates a command line arg '-H' and set to handle ip addr
   (options, args) = pars_obj.parse_args()
   host = options.host
 

   if (host == None):#if the script is run without args it will display the usage
      print pars_obj.usage
   else:
      connect(host)

if __name__ == '__main__':
   main()







