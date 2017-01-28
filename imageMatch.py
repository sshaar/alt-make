import base64
import httplib
import json
import os
import ssl

headers = {"Content-type": "application/json",
           "app_id": "acec3408",
           "app_key": "dd4950dd98b8c1835be33a84f39cc9d8"
           }
conn = httplib.HTTPSConnection("api.kairos.com", 
       context=ssl.SSLContext(ssl.PROTOCOL_TLSv1))

def delGallery(gallery):
    params = json.dumps({"gallery_name":gallery})
    conn.request("POST", "/gallery/remove", params, headers)
    response = conn.getresponse()
    result = response.read()
    print result


def addImage(url, s_id, gallery):
    
    params = json.dumps({"image": url,
                         "subject_id": s_id,
                         "gallery_name":gallery})
    conn.request("POST", "/enroll", params, headers)
    response = conn.getresponse()
    result = response.read()
    print result
#print result


def findMatch(url, gallery, threshold):
    
    params = json.dumps({"image": url,
                         "gallery_name":gallery,
                         "threshold": threshold})
    conn.request("POST", "/recognize", params, headers)
    response = conn.getresponse()
    result = response.read()
    parsedResult = json.loads(result)
    try:
        if (parsedResult["images"][0]["transaction"]["status"] == "success"):
            print parsedResult["images"][0]["candidates"][0]["subject_id"]
        else :
            print "no match found"
    except:
        print "no match found"


#delGallery("MyGallery")
#addImage("http://orig13.deviantart.net/c28e/f/2017/027/f/f/test1__by_scarecrow0604-dawwia0.png", "img1", "MyGallery")
#findMatch("http://orig13.deviantart.net/c28e/f/2017/027/f/f/test1__by_scarecrow0604-dawwia0.png", "MyGallery", 0.4)


def processMatch(urlChild, urlParent):
    if (urlChild != None):
        print ("child:")
        findMatch(urlChild)
    elif (urlParent != None):
        print ("parent:")
        findMatch(urlParent)

