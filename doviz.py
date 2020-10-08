from selenium import webdriver  #sayfayı açmak için
import time  #assayfa yüklenmesi sırasında bekleme yapmak için
from bs4 import BeautifulSoup   #sayfa içerisinde ki sadece ilgili kısımları bulup almak için



browser=webdriver.Chrome()  #chrome aracılığılya iligli siteye bağlanılacağı belirtildi.

degerler = set() #set değişkeni tanımlandı
#set'in önemi:her elemanı özeldir. yani aynı değer iki defa yazılamaz.
browser.get("https://kur.doviz.com")   #degerlerin alınacağı site
html = browser.page_source      
time.sleep(2)
soup = BeautifulSoup(html, 'html.parser')
ilkParca=soup.find("div",{"class": "header-secondary"})   #sayfada bulmasını isteiğimiz kısım.sayfada 1 tane olduğu için find_all değilde find yazıldı.
#print(ilkparca)    #sayfada istenilen kısımlara aşama aşama giriliyor. görmek için yorumdan çıkar.
bilgiler=ilkParca.find_all("div",{"class": "item"})  #sayfada tür(dolar vs.) ve fiyatların tanımlanma şeklindeki item classlarını bul

for bilgi in bilgiler:   #altın,dolar,euro için ayrı ayrı alt item oldugu için döngü yapıldı
    name = bilgi.find("span",{"class": "name"}).text     #herbir kurun isimlerini al(usd,euro vs.)
    value = bilgi.find("span",{"class": "value"}).text   #her bir kurun fiyatını al
    #sondaki .text ile ilgili classın içindeki text değerini yani gerçek bilgiyi alıyoruz.
    degerler.add(name+"="+value) #döngü şeklinde olduğu için 8 farklı bilgiyi name=value altın=500 şeklinde set'e kaydet.

degerlerListesi=list(degerler)#deegerler set'ini listeye çeviriyoruz. 8 ayrı kuru ayrı okumak istersek diye
print(degerlerListesi) #tüm degeleri yazdır
print(degerlerListesi[0])    #1. değeri yazdır.
#kurları yazarken sıralama kayabilir. ilk denemede 1.kur altın iken 2.denemede dolar olabilir.
browser.close()#browserı kapat