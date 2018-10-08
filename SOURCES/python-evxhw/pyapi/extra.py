# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
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

class _ExtraArray(object):
  def __init__(self, parent, position, width, total_items):
    self._parent = parent
    self._position = position
    self._width = width
    self._total_items = total_items

  def __len__(self):
    return self._total_items

  def __getitem__(self, it):
    if not it in xrange(self._total_items):
      raise IndexError('')
    if self._width == 4:
      return self._parent.GetVal32(self._position + it*self._width)
    elif self._width == 2:
      return self._parent.GetVal16(self._position + it*self._width)

  def __setitem__(self, it, val):
    if not it in xrange(self._total_items):
      raise IndexError('')
    if self._width == 4:
      return self._parent.SetVal32(self._position + it*self._width, val)
    elif self._width == 2:
      return self._parent.SetVal16(self._position + it*self._width, val)
  
  

class _ExtraStruct(object):
  _basics = ['_parent', '_position']

  def __init__(self, parent, position):
    self._parent = parent
    self._position = position

  def __getattr__(self, name):
    props =  self.FIELDS.get(name)
    if props is None:
      raise AttributeError(str(self.__class__.__name__) + " has no attribute " + str(name))
    begin, width, dims = props
    if dims == []:
      if width == 4:
        return self._parent.GetVal32(self._position + begin)
      elif width == 2:
        return self._parent.GetVal16(self._position + begin)
      else:
        AttributeError(str(self.__class__.__name__) + " attribute " + str(name) + " is not properly defined")
    else:
      if width == 4:
        return _ExtraArray(self._parent, self._position + begin, width, dims[0])
      elif width == 2:
        return _ExtraArray(self._parent, self._position + begin, width, dims[0])
      else:
        AttributeError(str(self.__class__.__name__) + " attribute " + str(name) + " is not properly defined")
      

  def __setattr__(self, name, value):
    if name in self._basics:
      return object.__setattr__(self, name, value)

    props =  self.FIELDS.get(name)
    if props is None:
      raise AttributeError(str(self.__class__.__name__) + " has no attribute " + str(name))

    begin, width, dims = props
    if dims == []:
      if width == 4:
        return self._parent.SetVal32(self._position + begin, value)
      elif width == 2:
        return self._parent.SetVal16(self._position + begin, value)
    else:
      AttributeError(str(self.__class__.__name__) + " attribute " + str(name) + " is not properly defined")


  def __str__(self):
    r = '<%s = {' % self.__class__.__name__ + '\n'
    for name in self.__slots__:
      r += '   ' + name + ': ' + str(getattr(self, name)) + ',\n'
    r += '}>'
    return r
