from tkinter import *
import os
import requests
from bs4 import BeautifulSoup 

def weather(link,head):   # funzione che fa web scraping e cerca meteo nella posizione corrente

    page = requests.get(link, headers=head)
    soup = BeautifulSoup(page.content, 'html.parser')

    condizione = str(soup.find(id='wob_dc').get_text())
    Luogo = str(soup.find(id='wob_loc').get_text())

    wind_speed = str(soup.find(id='wob_ws').get_text()) # da rivedere wind speed , temp and rainfall percentage
    rainfall = str(soup.find(id='wob_pp').get_text())

    temp = str(soup.find(id='wob_tm').get_text())

    
    
    
    if condizione == 'Soleggiato' or condizione == 'Sereno':
        weather_img =weather_sunny
    
    
    elif condizione == 'Parzialmente nuvoloso'or condizione == 'Per lo più soleggiato':
        weather_img =weather_par_cloudy
    

    elif condizione == 'Temporale':
        weather_img =weather_temp



    elif condizione == 'Rovesci' or condizione == 'Pioggia':
        weather_img =weather_rainy
    
    
    
    elif condizione == 'Rovesci nevosi':
        weather_img =weather_snowing
    
    
    elif condizione == 'Grandine':
        weather_img =weather_hailstorm

    elif condizione == 'Per lo più nuvoloso':
        weather_img = weather_cloudy
    
    Label_Weather = Label(root, image = weather_img,bg='#33363B')
    Label_Weather.place(x=40,y=85)    

    Label_luogo = Label(root, text=Luogo,font = ('ABeeZee',13),bg='#33363B', fg= 'white' )
    Label_luogo.place(x=40,y=165) 

    Label_wind = Label(root,text='Wind:'+wind_speed,font = ('ABeeZee',12),bg='#333B41', fg= 'white' )
    Label_wind.place(x=110,y=110)
    
    Label_rainfall = Label(root,text='Raifall:'+rainfall,font = ('ABeeZee',12),bg='#333B41', fg= 'white')
    Label_rainfall.place(x=110,y=130)

    Label_temp = Label(root,text=temp+'°C',font = ('ABeeZee',28),bg='#202329', fg= '#757778')
    Label_temp.place(x=220,y=19)


    Label_cond =Label(root, text=condizione,font = ('ABeeZee',12),bg='#333B41', fg= '#757778' )
    Label_cond.place(x=220,y=322)





root = Tk()
root.title('Essential Widget')
root.geometry('400x300+50+50')
root.overrideredirect(True)
root.wm_attributes('-transparentcolor','red')
root.config(bg='red')


if os.name == "posix":
    fonts = ("Courier", 16)
    border='white'    
else:
    fonts = ("Courier", 12)
    border='black'

image_bg= PhotoImage(file='bg_main.png')
weather_sunny = PhotoImage(file='sunny.png')
weather_cloudy = PhotoImage(file='cover.png')
weather_rainy = PhotoImage(file='rain.png')
weather_temp = PhotoImage(file='temporal.png')
weather_hailstorm = PhotoImage(file='hailstorm.png')
weather_snowing = PhotoImage(file='snow.png')
weather_par_cloudy = PhotoImage(file='par_cloudy.png')
b_google = PhotoImage(file='google.png')

Label_bg = Label(root, image = image_bg,bg='red')

Label_bg.pack()

Frame_bg = Frame(root,bg='white')
Frame_bg.pack()




#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Section Weather Web Scraping


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36' }


URL = 'https://www.google.com/search?q=weather+location&oq=weather+location&aqs=chrome..69i57.3274j0j7&sourceid=chrome&ie=UTF-8'

weather(URL,headers)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

root.bind('a', lambda event: root.destroy())


root.mainloop()