import requests
import pandas as pd
from bs4 import BeautifulSoup

send=requests.get('https://www.flipkart.com/computers/monitors/pr?sid=6bo%2C9no&fm=neo%2Fmerchandising&iid=M_ce1a6f68-d7d2-4ae1-875c-0d0877d9a11f_2_372UD5BXDFYS_MC.ECL5SFI77NSY&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&cid=ECL5SFI77NSY&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.brand%255B%255D%3Dacer&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTY1OTkiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJNb25pdG9ycyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PTkZERkRKVkZNR1k5TlYiLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19fX19&fm=neo%2Fmerchandising&iid=M_163c0cd1-fbdb-47fd-bf74-f6a8a6a8c6ac_3.TXZMLQJZFW8U&ppt=browse&ppn=browse&ssid=pxndnv7nsw0000001668508754898&otracker=hp_omu_Best%2Bof%2BElectronics_1_3.dealCard.OMU_TXZMLQJZFW8U_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_1_NA_view-all_3&cid=TXZMLQJZFW8U')
bs=BeautifulSoup(send.content,'html.parser')
print(send)


name=bs.find_all('div',class_="_4rR01T")
a=[]
for i in name:
    b=i.get_text()
    a.append(str(b))
    print(a)



price=bs.find_all('div',class_="_30jeq3 _1_WHN1")
p=[]
for i in price:
    b=i.get_text()
    p.append(b)
    print(" ",p)

image=bs.find_all('img',class_="_396cs4 _3exPp9")
age=[]
for i in image:
    b=i['src']
    age.append(b)
    print(age)



link=bs.find_all('a',class_="_1fQZEK")
ink=[]
for i in link:
    b="ihttps://www.flipkart.com"+i['href']
    ink.append(b)
    print(ink)


df=pd.DataFrame()
df["Name"]=a
df["Price"]=p
df["Image"]=age
df["link"]=ink
df.to_csv("monitor.csv")












