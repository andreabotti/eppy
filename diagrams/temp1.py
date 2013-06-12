# Copyright (c) 2012 Santosh Philip

# This file is part of eppy.

# Eppy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Eppy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with eppy.  If not, see <http://www.gnu.org/licenses/>.

"""update referenced object names
this can only replace names that are object names.

need to explore how to change node names.
node names are not object names
usage:
python 
"""

import sys
import getopt
sys.path.append('../EPlusInputcode')
from EPlusCode.EPlusInterfaceFunctions import readidf

from EPlusCode.EPlusInterfaceFunctions import parse_idd
from EPlusCode.EPlusInterfaceFunctions import eplusdata
import eplus_functions


help_message = '''
The help message goes here.
'''


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg



iddfile = "../iddfiles/Energy+V6_0.idd"
block,commlst,commdct=parse_idd.extractidddata(iddfile)
theidd=eplusdata.idd(block,2)


fname = "../idffiles/a.idf"
data, commdct = readidf.readdatacommdct(fname, iddfile=theidd,
                            commdct=commdct)
idd = eplus_functions.Idd(commdct, commlst, theidd, block)
idfw = eplus_functions.IdfWrapper(data, idd)

# ---
key = 'zone'.upper()
fieldid = 1
oldname = 'SPACE1__1'
newname = 'LOBBY'

eplus_functions.rename_name(idfw, key, oldname, newname)
txt = `data`
fname = 'a.idf'
open(fname, 'w').write(txt)

        