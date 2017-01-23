import subprocess


def app_install(appName):
    apps_to_be_installed = get_filenames_for_install()
    for app in apps_to_be_installed:
        output = subprocess.check_output(["sudo", "-S" ,"installer", "-pkg", "./bin/" + app, "-target", "/"])
        print output


def get_filenames_for_install():
    file_names = []
    with open('./bin/apps.txt', 'r') as appsList:
        url = appsList.readline()
        while url != '':
            url = url.strip('\n')
            url_routes = url.split('/')
            file_names.append(url_routes[len(url_routes) - 1])
            url = appsList.readline()
    return file_names
