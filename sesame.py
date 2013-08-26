# -*- coding: utf-8 -*-
#
# This file is part of DownloadSDSSFindingCharts.
#
# This is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib
import functools

cdsMirrorUrls = {
    'cds': 'http://cdsws.u-strasbg.fr/axis/services/Sesame',
    'cfa': 'http://vizier.cfa.harvard.edu/viz-bin/Sesame'
}

sesameMethod = '?method=sesame&resultType=p&all=true&service=NSVA' +\
               '&name=%(name)s'

separator_prefix = "#="
ned_prefix       = '#=N=NED'
simbad_prefix    = '#=S=Simbad'
vizier_prefix    = '#=V=Simbad'
last_prefix      = '#====Done'


class Source(object):
    """docstring for Source"""
    def __init__(self, source_name):
        self.source_name = source_name
        self.properties = None
    
    def properties(self):
        if self.properties != None:
            return self.properties
    

class SesameHelper(object):
    """SesameHelper is a class with static methods for accessing de CDS Sesame service"""
    def __init__(self, mirror='cds'):
        self.url = cdsMirrorUrls[mirror]+sesameMethod
    
    @staticmethod
    def find_prefix(x, prefix=None):
        result = False
        if (x[1].find(prefix) == 0):
            result = True
        return result
    
    @staticmethod
    def separators(sesame_response):
        def fn(x):
            result = -1
            if (x[1].find(separator_prefix) == 0):
                result = x[0] 
            return result
        
        separators = filter(lambda x: x != -1,
               map(
                   fn,
                   zip(
                       range(len(sesame_response)),
                       sesame_response
                   )
               )
        )
        separators.sort()
        return separators
    
    @staticmethod
    def get_value(sesame_list, prefix, transform=str):
        value = None
        prefix = prefix.strip()
        values = filter(lambda x: x.find(prefix) == 0, sesame_list)
        if len(values) >= 1:
            value = transform(values[0][len(prefix)+1:])
        return value
    
    @staticmethod
    def get_values(sesame_list, prefix):
        values = None
        prefix = prefix.strip()
        values = map(
                    lambda x: x[len(prefix)+1:],
                    filter(
                        lambda x: x.find(prefix) == 0,
                        sesame_list
                    )
        )
        return values
    
    @staticmethod
    def process_ned(sesame_fragment):
        ned_dict = {
            'ra': None,
            'dec': None,
            'ra_err': None,
            'dec_err': None,
            'radec_ref': None,
            'alias': None,
            'otype': None,
            'oname': None,
            'mag': None,
            'Vel_v': None,
            'Vel_err': None,
            'Vel_ref': None,
            'MType': None
        }
        
        # object names
        object_names = get_values(sesame_fragment, '%I')
        ned_dict['oname'] = object_names[0][2:] # removes the '0 '
        ned_dict['alias'] = object_names[1:] # all the rest
        
        # magnitude
        ned_dict['mag'] = get_value(
                            sesame_fragment, '%MAG', transform=float
        )
        
        # object class
        ned_dict['otype'] = get_value(sesame_fragment, '%C')
        
        # morphological class
        ned_dict['MType'] = get_value(sesame_fragment, '%T')
        
        return ned_dict
    
    @staticmethod
    def process_fragment(sesame_fragment, properties):
        # properties is passed by reference, so that we can
        # modify it
        # We check the corresponding processor using the first line
        if sesame_fragment[0].find(ned_prefix):
            properties['NED']    = process_ned(sesame_fragment)
        else if sesame_fragment[0].find(simbad_prefix):
            properties['Simbad'] = process_simbad(sesame_fragment)
        else if sesame_fragment[0].find(vizier_prefix):
            properties['VizieR'] = process_vizier(sesame_fragment)
    
    @staticmethod
    def properties_from_cds_response(sesame_response):
        properties = {
            'NED':    {},
            'Simbad': {},
            'VizieR': {}
        }
        # Filter NED
        separator_positions = separators(sesame_response)
        # we zip the starts with the ends of the sections
        # if they start at lines 1, 30, 55, fragments will be
        # [(1, 30), (30, 55)]
        fragments = zip(
                separator_positions[:-1],
                separator_positions[1:]
        )
        
        # We pass properties by value, so that it can be updated
        for start,end in fragments:
            process_fragment(sesame_response[start:end], properties)
        
        
    @staticmethod
    def clean_response(sesame_response):
        cleaned_response = map(lambda x: x.strip(), sesame_response)
        cleaned_response = filter(
                                # #! marks a section not returned 
                                lambda x: x.find('#!') != 0 and (
                                            x.find('#') == 0 or
                                            x.find('%') == 0
                                          ) ,
                                cleaned_response
        )
        return cleaned_response
    
    def query(self, source):
        resultDict = {}
        sesameQuery = self.url % {
                        'name': urllib.quote(source.strip())
        }
        
        sesame_response = urllib.urlopen(sesameQuery).readlines()
        # Remove line endings, and retain only responses starting
        # with a hash (#) or percent (%)
        sesame_response = clean_response(sesame_response)
        