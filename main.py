from tkinter import *
import os
import requests
from bs4 import BeautifulSoup 
import webbrowser

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
    Label_Weather.place(x=40,y=95)    

    Label_luogo = Label(root, text=Luogo,font = ('ABeeZee',13),bg='#33363B', fg= '#878585' )
    Label_luogo.place(x=50,y=185) 

    Label_wind = Label(root,text='Wind:'+wind_speed,font = ('ABeeZee',12),bg='#33363B', fg= '#878585' )
    Label_wind.place(x=130,y=140)
    
    Label_rainfall = Label(root,text='Rainfall:'+rainfall,font = ('ABeeZee',12),bg='#33363B', fg= '#878585')
    Label_rainfall.place(x=129,y=160)

    Label_temp = Label(root,text=temp+'°C',font = ('ABeeZee',20),bg='#33363B', fg= '#878585')
    Label_temp.place(x=130,y=88)


    Label_cond =Label(root, text=condizione,font = ('ABeeZee',12),bg='#33363B', fg= '#878585' )
    Label_cond.place(x=130,y=120)


def time_now(link,head):
    
    page = requests.get(link, headers=head)
    soup = BeautifulSoup(page.content, 'html.parser')

    curr_time = str(soup.find("div", {"class": "gsrt vk_bk FzvWSb XcVN5d YwPhnf"}).get_text())
    curr_date =str(soup.find('div',{'class':'vk_gy vk_sh'}).get_text())
    
    list_time = curr_time.split(':')
   
    label_hour_time = Label(root, text=list_time[0],font = ('Bungee',40,'bold'),bg='#33363B', fg= '#656565')
    label_hour_time.place(x=292,y=78)

    label_min_time = Label(root, text=list_time[1],font = ('Bungee',40,'bold'),bg='#33363B', fg= '#656565')
    label_min_time.place(x=292,y=140)

    label_date = Label(root, text = curr_date,font = ('Bungee',13),bg='#33363B', fg= '#878585' )
    label_date.place(x=28,y=28)

def Searchbar():
    
    search_word =str(entry_google.get())
    
    webbrowser.open('https://www.google.com/search?q='+ search_word)
    
    entry_google.delete(0,'end')

root = Tk()
root.title('Essential Widget')
root.geometry('400x300+50+50')
root.wm_attributes('-alpha',0.8)



if os.name == "posix":
    root.overrideredirect(False)
    root.config(bg='#1F2226')
    

else:
    root.overrideredirect(True)
    root.wm_attributes('-alpha',0.8)
    root.wait_visibility(root)
    root.wm_attributes('-transparentcolor','red')
    root.config(bg='red')


image_bg= PhotoImage(file='Web 1280 – 1.png')
weather_sunny = PhotoImage(file='sunny.png')
weather_cloudy = PhotoImage(file='cover.png')
weather_rainy = PhotoImage(file='rain.png')
weather_temp = PhotoImage(file='temporal.png')
weather_hailstorm = PhotoImage(file='hailstorm.png')
weather_snowing = PhotoImage(file='snow.png')
weather_par_cloudy = PhotoImage(file='par_cloudy.png')
b_google = PhotoImage(file='google.png')
close_icon = PhotoImage(file='close.png')



Label_bg = Label(root, image = image_bg,bg='#1F2226')
Label_bg.pack()

Frame_bg = Frame(root,bg='white')
Frame_bg.pack()

entry_google = Entry(root,width=20,bg='#656565',fg='#1F2226',font = ('ABeeZee',13),highlightthickness = 0,borderwidth=0,selectbackground='white')
entry_google.place(x=38,y=246)

Button_search = Button(root,image = b_google,bg='#33363B',command = Searchbar,highlightthickness = 0,borderwidth=0,activebackground='#33363B')
Button_search.place(x=315,y=243)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Section Weather Web Scraping


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36' }


URL = 'https://www.google.com/search?q=weather+location&oq=weather+location&aqs=chrome..69i57.3274j0j7&sourceid=chrome&ie=UTF-8'

URL_time = 'https://www.google.com/search?q=ora&oq=ora&aqs=chrome..69i57j69i61l2.2138j0j7&sourceid=chrome&ie=UTF-8'

weather(URL,headers)
time_now(URL_time,headers)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

root.bind('<F1>', lambda event: root.destroy())
root.bind('<Enter>',Searchbar)


root.mainloop()