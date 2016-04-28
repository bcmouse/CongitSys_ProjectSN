import facebook
import json
import requests
import unicodedata
import time
import datetime
import math

def ConvOffTime(OffD,OffH,OffM,OffS):
    #Define time window from Day,Hour,Minute,Sec
    return (OffD*86400)+(OffH*3600)+(OffM*60)+OffS

#Print Python objects as JSON
def pp(o,myfile):
    #print json.dumps(o, indent=1)
    json.dump(o,myfile,sort_keys=False,indent=0, separators=(',', ': '))
    return json.dumps(o, indent=1)

FAPPID = '945455498898604'
FAPPST = '6860c1e5dc694375147a323b1cd4ef24'
user_id = '497992153678490' #Enrique Serrano
IniDate = "2016-04-26T23:00:00" #Date to start mining (Starts from here to the first post of the account or when LimError is reached)
EndDate = "2016-04-16T00:00:00" #Date to end mining
OffDate = ConvOffTime(1,0,0,0) #Time Window
ErrorLim = 5 #Error Limit Offset
NonCleanName = 'NonClean.txt'
CleanName = 'Clean.txt'

IniTimestamp = int(time.mktime(datetime.datetime.strptime(IniDate, "%Y-%m-%dT%H:%M:%S").timetuple())-18000) #Initial Date in our time zone
EndTimestamp = int(time.mktime(datetime.datetime.strptime(EndDate, "%Y-%m-%dT%H:%M:%S").timetuple())-18000) #Initial Date in our time zone

TPosts = 0 #Total Posts
TRequests = 0 #Total Requests
Error = "{\n \"id\": \"" + user_id + "\"\n}" #Error Pattern detection
ECount = 0 #Error Counter
ErrorPrev = 0 #Previous Error State

NonCleanFile = open(NonCleanName,'a+')

print "####### Facebook Mining #######\n  "
print "Getting access to facebook, please wait...\n"

#tok = 'CAACEdEose0cBAKnP3W5RMkOQZAzFGyeDIDeZBT3QPsAohiIGN8Uml6ciGWMUMfjReEX5lfsNw88ILxvGEFQzp16FNoXvTn2Qu3pgOZBt3RNnxpht9QkD5Uy5ZCG0BJ4fupb3BNbJZCEvQZCtkExKJys3ZAXH2ZBJsnFG192xcFFqpoxJRCE00ZCfoqsjmDB2lmitgdg63Fj7Hx649QfdxuEmf'
try:
    oauth_access_token = facebook.get_app_access_token(FAPPID,FAPPST)
    print "Token has been obtained successfully"
except:
    print "Token could not be obtained, run the script again"
    exit()

# Create a connection to the Graph API with your access token
try:
    g = facebook.GraphAPI(oauth_access_token)
    print "Access to Facebook has been granted\n"
except:
    print "Access to Facebook has been rejected,Run the script again\n"
    exit()

item = g.get_object(user_id,field = 'name')
print "###### Page to be analyzed:",item['name']," ######"

print "Starting Posts recovering process...\n"
Tstart = time.time() #Initial Time
TInsPrev = Tstart #Delay -1 Instantaneous Time

while True:
    if (ECount >= ErrorLim) or (IniTimestamp < OffDate) or (IniTimestamp < EndTimestamp):
        print "\nRecovering Posts process has finished successfully"
        break
    PDate = datetime.datetime.fromtimestamp(IniTimestamp).strftime('%d-%m-%Y') # %H:%M:%S')
    print "****** Obtaining Posts from " + PDate + " ******"
    #pp(g.get_object(user_id, fields = 'posts.offset('+str((Plim*i)+Olim)+').limit('+str(Plim)+').fields(created_time,message,comments.fields(created_time,from,message))'),NonCleanFile)
    Post = pp(g.get_object(user_id, fields = 'posts.until('+str(IniTimestamp)+').since('+str(IniTimestamp-OffDate)+').fields(created_time,message,comments.fields(created_time,from,message))'),NonCleanFile)
    TRequests += 1
    if Post == Error:
        if ErrorPrev == 0:
            ErrorPrev = 1
            ECount = 1
        if ErrorPrev == 1:
            ECount += 1
        print "No posts available for this day"
    else:
        ErrorPrev = 0
        ECount = 0
        TPosts += 1
    IniTimestamp -= OffDate
    TIns = time.time()
    print "E.T.:","%.1f" %(TIns-TInsPrev),"sec"
    TInsPrev = TIns

Tend = time.time() #End Time
print "The posts of",TPosts,"days has been retrieved\n"
print "The total requests done to facebook were:",TRequests
print "Total Elapsed time of the process:","%.1f" %(Tend-Tstart),"seconds\n"
NonCleanFile.close()

print "******* Creating files with obtained info"
print "File with RAW Data created:",NonCleanName

NonCleanFile = open(NonCleanName,'a+')
CleanFile = open(CleanName,'a+')
for line in NonCleanFile: #Prefiltering (Diacritics Removal)
    Cline = line.decode('unicode_escape')
    Sline = ''.join((c for c in unicodedata.normalize('NFD', Cline) if unicodedata.category(c) != 'Mn'))
    try:
        CleanFile.write(Sline)
    except:
        RemInv = Sline.encode('ASCII', 'ignore')
        CleanFile.write(RemInv)

NonCleanFile.close()
CleanFile.close()
print "File with Prefiltered Data created:",CleanName