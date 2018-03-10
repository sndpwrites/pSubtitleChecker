import requests
from tqdm import tqdm
import zipfile


def downloader(season):
    return "http://www.tvsubtitles.net/download-65-"+season+"-en.html"

season = range(1,11,1)

#download from url and show progress bar
for i in season:
    url = downloader(i.__str__())
    print "Retrieving Season "+i.__str__()+" from "+url
    response = requests.get(url, stream=True)
    with open(i.__str__(), "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)
    print "Zip file retrieved"
#extract downloaded file. Saves in pwd unless argument provided
for j in season:
    zip_ref = zipfile.ZipFile(j.__str__(), 'r')
    zip_ref.extractall()
    zip_ref.close()
    print "Season "+j.__str__()+" extracted"
