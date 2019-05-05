# mapJSON
## what is mapJSON?
This is a flexible map engine that can be used in audiogames creation.
it is highly customizable, you can create sidescroller, 2d or 3d maps.
The engine it's self uses json when it parses the json data  from the  files, so if you want to you could create the maps with raw json data.
## usage
We will now create an example map.
```python
import mapjson
m = mapjson.Map()
m.set_name('testing map')
m.set_borders((50, 50, 50))
m.add_tile(0, 50, 0, 50, 0, 50, 'testing')
m.add_zone(0, 50, 0, 50, 0, 50, 'testing zone')
m.dump(in_file=True, file='test.json')
```
So what we did was importing the mapjson module
We instantiated the map class and added a tile and a zone. After that we dumped the map data in the file named test.json so that it can be loaded later.
What does the file data look like?
```json
{
 "name": "test",
 "borders": [
  50,
  50,
  50
 ],
 "items": [
  {
   "minx": 0,
   "maxx": 50,
   "miny": 0,
   "maxy": 50,
   "minz": 0,
   "maxz": 50,
   "type": "testing"
  },
  {
   "minx": 0,
   "maxx": 50,
   "miny": 0,
   "maxy": 50,
   "minz": 0,
   "maxz": 50,
   "type": "zone",
   "name": "testing zone"
  }
 ]
}
```
if we were to load  the map class from the json file, we would get the tile and the zone previously added.
## notes
* the test.json has been left in the repository so that you can mess around with it
## methods
Here is a list of methods, which you can use when interacting with the map class.
```python
Map.set_name(name)
```
this will set the map name to the parameter given
```python
Map.set_borders((x, y, z))
```
set_borders() takes a tuple of 3 parameters which are x, y, and z. Those define the borders of the map, therefore the size of the map can be managed from this function.
Map.add_tile() and Map.add_zone() take the same arguments which are
minx, maxx, miny, maxy, minz, maxz, type for tile and name for the zone.
Map.get_tile_at() Map.get_zone() Map.get_tile_obj() and map.get_zone_obj() take respectively 3 parameters which are x, y and z. Those parameters have a default value of 0.
get_tile_at() and get_zone() will return the string of the tile type, or the zone name. While, get_tile_obj() and get_zone_obj() will return the tile or zone's object.
Map.delete_tile_at() and Map.delete_zone() take 3 parameters which are x, y, and z. Those have a default value of 0
Those functions are useful to delete certain tiles or zones from your map.
Those have all a default value, so you could for example easily create a tile that has only the maxx defined, which would be good for a sidescroller.
```python
Map.dump(in_file=False, file='')
```
This method allows you to dump the map data in to a file. This will occur if in_file is true, and if the file name is not blank. If the conditions are not met, the data will be returned as a string.
```python
Map.load(data='', from_file=False, name='')
```
This instead loads the map data either from a string, or from a file.
## license
This project is under the MIT license.
MIT License

Copyright (c) 2018 Paul Iyobo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
## contributing
If you'd like to contribute new improvements, or fix any bug, feel free to send a pull request.