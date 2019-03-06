import traceback
import requests
import shutil
from bs4 import BeautifulSoup
import json as j
import pprint
def downloader(url,path):
    try:

        headers= {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
        r=requests.get(url, headers=headers)
        htmlcode = r.text
        soup = BeautifulSoup(htmlcode,features="lxml")
        tags = soup('script')
        json=""
        
        for tag in tags:
            if "PxPreloadedData" in tag.text:
                json=j.loads(tag.text[28:-2])
                break
        images=json["photo"]["images"]
        
        biggest_image=images[0]
        for i in images:
            if biggest_image["size"] < i["size"]:
                biggest_image=i
        
        print("Title: ",json["photo"]["name"])
        print("Author: ",json["photo"]["user"]["username"])
        title = json["photo"]["name"]+"_500px_"+json["photo"]["user"]["username"]
        # Remove unsafe characters
        title="".join([c for c in title if re.match(r'\w', c)])+"."+biggest_image["format"]
        
        
        print("File name: ",title)
        print("Url: ", biggest_image["url"])
       
        try:
            r = requests.get(biggest_image["url"], stream=True)
            if r.status_code == 200:
                with open(path+"/"+title, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)        
                    
        except Exception as e:
            traceback.print_exc()
            print("Error downloading: "+ str(e))

                    
    except Exception as e:
        traceback.print_exc()
        print("Error decoding image path: "+ str(e))




