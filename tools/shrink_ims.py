#!/usr/bin/env python
'''
Shrink all images to normal and thumbnail sizes.
'''
import os
import glob

from consolation.app import Console

app = Console("")

@app.main()
def main(dir):
    os.system('mkdir {0}/pages {0}/thumbnails'.format(dir))
    for img in glob.glob(dir+"/hires_pages/*.jpg"):
        page_out = img.replace("hires_pages", "pages")
        thumb_out = img.replace("hires_pages", "thumbnails")
        os.system("convert {0} -resize 740 {1}".format(img, page_out))
        os.system("convert {0} -resize 50 {1}".format(img, thumb_out))

if __name__ == '__main__':
    app.run()