import urllib2
import bs4
import csv

raw_html = urllib2.urlopen('https://buses.cardekho.com/filter/bus.html')
soup = bs4.BeautifulSoup(raw_html, 'html.parser')
data = soup.find_all('div', class_='list_top')
buses = soup.find_all('li', {'class': 'result_list'})
image = soup.find_all('img', class_='lazy')
print(len(buses))
for i in range(len(buses)):
    data1 = data[i].text.strip()
    bus = data1.split('\n', 1)[0]
    print(bus)
    bus1 = buses[i].a['href']
    print(bus1)
    im = image[i]
    img = im['data-original']
    url1 = urllib2.urlopen('https://buses.cardekho.com' + bus1)
    soup = bs4.BeautifulSoup(url1, 'html.parser')
    data1 = soup.find_all('td', class_='kmpl')
    cc = data1[2].text.strip()
    Fuel = data1[3].text.strip()
    url2 = urllib2.urlopen('https://buses.cardekho.com' + bus1 + '/price')
    soup = bs4.BeautifulSoup(url2, 'html.parser')
    data2 = soup.find_all('select', class_='custom-select')
    price = data2[0].text.strip()
    url3 = urllib2.urlopen('https://buses.cardekho.com' + bus1 + '/specifications')
    soup = bs4.BeautifulSoup(url3, 'html.parser')
    data3 = soup.find_all('div', class_='engineright')
    GVW = data3[26].text.strip()
    seat_count = data3[30].text.strip()
    print(cc)
    print(Fuel)
    print(price)
    print(GVW)
    print(seat_count)
    print(img)
    print('--------------------')
    f = open('file_car.csv', 'a')
    writer = csv.writer(f)
    writer.writerow([bus, cc, Fuel, price, GVW, seat_count, img])
    f.close()
    i += 1










