# mapJSON
## what is mapJSON?
This is a flexible map engine that can be used in audiogames creation.
it is highly customizable, you can create sidescroller, 2d or 3d maps.
The engine it's self uses json when it parses the map in files, so if you want to you could create the maps with raw json data.
## how to use
We will now create a minimal map.
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
We instantiated the map class and added a tile and a zone. After that we dumped the map data in the file, so that it can be loaded later.
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
* the source is implemented only as a map type, you will have to provide your own sound class to get it working
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
set_borders() takes a tuple of 3 parameters which are x, y, and z. With those the map will have a size of the borders defined.
Map.add_tile() Map.add_zone() and Map.add_src() take the same arguments which are
minx, maxx, miny, maxy, minz, maxz, type for tile, name for the zone, and sound for the source.
Those have all a default value, so you could for example easily create a tile that has only the maxx defined, which would be good for a sidescroller.
```python
Map.dump(in_file=False, file='')
```
This method allows you to dump the map data in to a file. This will occur if in_file is true, and if the file name is not blank. If the conditions are not met, the data will be returned.
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