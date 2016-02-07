import requests
import bs4
import os

os.chdir('C:\Users\sony\Desktop')
if not os.path.exists("C:\Users\sony\Desktop\cyanide comics"):
    os.mkdir('cyanide comics')
os.chdir('C:\Users\sony\Desktop\cyanide comics')

begin=input('Enter the first comic you want:')
number_of_com=input('Enter the number of comics you want:')
count=1
while count <=number_of_com :
    com_url=requests.get('http://explosm.net/comics/'+str(begin)+'/')
    if com_url.status_code== 200:
        
        com_soup=bs4.BeautifulSoup(com_url.content,'lxml')
        main_com_div=com_soup.find(id='main-comic')
        src=main_com_div.get('src')
        finallycom=open('cyanide'+str(count)+'.jpeg',"wb+")
        final2=requests.get('https:'+src)
        finallycom.write(final2.content)
        finallycom.close()
        count+=1
    begin+=1
    
        
        



    
