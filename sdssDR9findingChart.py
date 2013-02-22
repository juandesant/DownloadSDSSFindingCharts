#!/usr/bin/env python
import sys
import urllib
sesameQueryUrl="http://cdsws.u-strasbg.fr/axis/services/Sesame?method=sesame&resultType=p&all=true&service=NSVA&name=%(name)s"
sdssQueryUrl = 'http://skyservice.pha.jhu.edu/DR9/ImgCutout/getjpeg.aspx'

with open(sys.argv[1],'r') as f:
    # Get only non-empty lines, stripped of trailing blanks and \n
    objects = filter(lambda x: len(x)>0, map(lambda x: x.strip(), f.readlines()))
    
    for obj in objects:
        # Perform the Sesame query
        try:
            sesameQuery = sesameQueryUrl % {'name': urllib.quote(obj.strip())}
            print "Processing Sesame query for %s" % obj
            
            sesameResponse = urllib.urlopen(sesameQuery).readlines()
            ra, dec = filter(lambda x: x.find('%J') == 0, sesameResponse)[0].split(' ')[1:3]
            
            # SDSS DR9
            sdssParamsDict = {
                'ra':     ra,
                'dec':    dec,
                'scale':  0.396127,
                'width':  1024,
                'height': 1024,
                'opt':   'G',
                'query': 'SR(10,10)'
            }
            
            try:
                print "Trying to query SDSS for coords %s %s" % (ra, dec)
                sdssResponse = urllib.urlopen(sdssQueryUrl+'?'+urllib.urlencode(sdssParamsDict))
                sdssImageData = sdssResponse.read()
            
                try:
                    jpegName = obj.strip()+'.jpg'
                    print "Trying to write %s" % jpegName
                    with open(jpegName,'w') as jpegFile:
                        jpegFile.write(sdssImageData)
                except Exception, e:
                    print "Failed while writing %s" % jpegName
            except Exception, e:
                print "Failed during SDSS search"
        
        except Exception, e:
            print "Failed during coordinates search for %s" % obj
            print e
        
