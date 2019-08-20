'''
Copyright (C) 2019 CG Cookie
http://cgcookie.com
hello@cgcookie.com

Created by Jonathan Denning, Jonathan Williamson, and Patrick Moore

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from .rftool_contours.contours     import Contours
from .rftool_polystrips.polystrips import PolyStrips
from .rftool_polypen.polypen       import PolyPen
from .rftool_strokes.strokes       import Strokes
from .rftool_patches.patches       import Patches
from .rftool_loops.loops           import Loops
from .rftool_relax.relax           import Relax
from .rftool_tweak.tweak           import Tweak

from .rftool import RFTool

class RetopoFlow_Tools:
    def setup_tools(self):
        self.rftools = [rftool(None) for rftool in RFTool.registry]

