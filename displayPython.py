import urllib.request
import requests
from PIL import Image

names_and_urls=dict()
icons_names=[]



def display_by_keyword():
    response = requests.get("https://api.github.com/emojis")
    if response.status_code == 200:
        names_and_urls = response.json()
        icons_names = list(names_and_urls.keys())
    flag=False
    while(flag==False):
        keyword=input("which image do you want to display?")
        final = [word for word in icons_names if keyword.lower() in word.lower()]

        if len(final)==1:
            print(type(names_and_urls))
            display_image(names_and_urls[final[0]],final[0])
            flag=True
        elif len(final)>1:
            print("Several results matching your search were found. Please select the number of image you want to view: ")
            res=dict()
            count=0
            name: object
            for name in final:
                count=count+1
                res[count]=name
                print(count,res[count])
            num=input()
            if int(num.isdigit()):
                num=int(num)
                print("num",num)
                print("res",res)

                print("name",res[num])
                # print("url",names_and_urls[res[num]])
                display_image(names_and_urls[res[num]], res[num])
        elif len(final)==0:
            print("No results matching your search were found. pleas try again:")

def display_all():
    response = requests.get("https://api.github.com/emojis")
    if response.status_code == 200:
        names_and_urls = response.json()
        icons_names = list(names_and_urls.keys())
    print(icons_names)
    for name in icons_names:
        print(name)
def display_image(img_url,name):
    print(f"going to show {img_url,name}")
    # response = requests.get("https://api.github.com/emojis")
    # if response.status_code == 200:
    #     emojis = response.json()
    #     for name, p_url in emojis.items():
    urllib.request.urlretrieve(f"{img_url}",f"{name}")
    img = Image.open(name)
    img.show()



