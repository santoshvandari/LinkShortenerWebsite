from django.shortcuts import render,redirect
from main.urlshorter import shorttext
from main.models import URLTable

# Create your views here.
def home(request):
    if request.method == "POST":
        url=request.POST.get("url")
        shorten=shorttext()
        print(url,shorten)
        shorternurldata={}
        try:
            obj = URLTable(url=url,short_url=shorten)
            obj.save()
            shorternurl=request.build_absolute_uri('/')+"t/"+shorten
            shorternurldata={
                "shorternurl" : shorternurl
            }
            print(shorternurldata)
        except Exception as ex:
            shorternurldata={
                'error' : True
            }    
            print(shorternurldata)
        print(shorternurldata)

        return render(request,"index.html",{"shorternurldata":shorternurldata}) 
    return render(request,"index.html")



def shorturl(request,slug):
    getdata=URLTable.objects.filter(short_url=slug)[0]
    if getdata: 
        print(getdata)
        url=getdata.url
        return redirect(url)
    else:
        return render(request,"brokenurl.html")