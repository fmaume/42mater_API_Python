#%%
#import dependancy
import requests
import time

#%%
#function to call the API
def search_by_sdk(token, sdk, limit):
     #perform first query
     query = "https://data.42matters.com/api/v2.0/android/apps/by_sdk.json?any_sdks=" + sdk +  "&limit=" + str(limit) + "&access_token=" + token
     response = requests.request("GET", query)
     #parsen result to Json
     data = response.json()
     

     
     #extract all result for dic
     result = list()
     [result.append(x) for x in data['results']]

     
     
     
     ##
     #Paging:
     #inititat page count
     page = 1
     
     #if there is still page afterware make new query until page 9999 which is the api limit
     while((data["has_next"] == True) & (page < 9999)):
         try:
             query = "https://data.42matters.com/api/v2.0/android/apps/by_sdk.json?any_sdks=" + sdk +  "&limit=" + str(limit) + "&access_token=" + token + "&page=" + str(page)
             response = requests.request("GET", query)
             #parsen result to Json
             data = response.json()
         
            #add result to result list
            [result.append(x) for x in data['results']]
         
         
            #iterate paging
            page = page +1
            time.sleep(1)
        except:
            return result
         
    return result 
    
#%%
#example
token = API_token
sdk = "unity3D"
limit = 50

result = search_by_sdk(token, sdk, limit)
