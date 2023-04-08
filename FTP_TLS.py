from ftplib import FTP_TLS
from getpass import getpass

ftpes = FTP_TLS('FTP的帳號')
ftpes.login('帳號', '密碼')  
ftpes.prot_p()         
temp = ftpes.retrlines('LIST') 
print(temp)
os.system("pause")