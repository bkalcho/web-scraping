import requests
from lxml import html
import sys
import urlparse
import re


url = 'http://poslovi.infostud.com'
response = requests.get(url)
parsed_body = html.fromstring(response.text)

# grab links to all images
images = parsed_body.xpath('//img/@src')
if not images:
    sys.exit('Found no images')

# convert any relative urls to absolute urls
images = [urlparse.urljoin(response.url, u) for u in images if re.findall('^/img.*(png|jpg|jpeg)', u)]
print "Found %s images" % len(images)
print images
# only download first 10
for u in images[0:10]:
    r = requests.get(u)
    f = open('downloaded_images/%s' % u.split('/')[-1], 'wb')
    print u.split('/')[-1]
    f.write(r.content)
    f.close()