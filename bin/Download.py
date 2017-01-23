import urllib

def download_app(publicUrl):
    publicUrl = publicUrl.strip('\n')
    print 'URL' + publicUrl
    urlRoutes = publicUrl.split('/')
    fileName = urlRoutes[len(urlRoutes) - 1]
    response = urllib.urlretrieve(publicUrl, "./bin/" + fileName)

def download_all_apps():
    #apps = open('./apps.txt', 'r')
    #download_app(apps.readline())

    with open('./bin/apps.txt', 'r') as appsList:
        url = appsList.readline()
        while url != '':
            download_app(url)
            url = appsList.readline()

#download_all_apps()
