#! /usr/bin/env python

# Copyright (c) 2013 Victor Terron. All rights reserved.
# Institute of Astrophysics of Andalusia, IAA-CSIC
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

import distutils.core

distutils.core.setup (name = 'DownloadSDSSFindingCharts',
                      description = "Automatically download finding charts "
                                    "from Data Release 9 (DR9) of the Sloan "
                                    "Digital Sky Survey (SDSS).",
                      author = 'Juan de Dios Santander',
                      author_email = 'jdsant@iaa.es',
                      url = 'https://github.com/juandesant/DownloadSDSSFindingCharts/',
                      license = "GNU General Public License, version 3 (GPLv3)",
                      scripts = ['sdssDR9findingChart'],
                      )

