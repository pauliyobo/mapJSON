import	json

class	tile(object):
	"""The	tile	class."""
	def	__init__(self,	minx=0,	maxx=0,	miny=0,	maxy=0,	minz=0,	maxz=0,	type=''):
		self.minx	=	minx
		self.maxx	=	maxx
		self.miny	=	miny
		self.maxy	=	maxy
		self.minz	=	minz
		self.maxz	=	maxz
		self.type	=	type

	def	covers(self,	x,	y,	z):
		if	self.minx	<=	x	and	self.maxx	>=	x	and	self.miny	<=	y	and	self.maxy	>=	y	and	self.minz<=z	and	self.maxz>=z:
			return	True
		return	False

class	zone(tile):
	def	__init__(self,	minx,	maxx,	miny,	maxy,	minz,	maxz,	name):
		super(zone,	self).__init__(minx,	maxx,	miny,	maxy,	minz,	maxz,	type='zone')
		self.name	=	name
	
class	Map(object):
	def	__init__(self):
		self.name	=	''
		self.maxx	=	0
		self.maxy	=	0
		self.maxz	=	0
		self.tiles	=	[]
		self.zones	=	[]

	def	add_tile(self,	minx=0,	maxx=0,	miny=0,	maxy=0,	minz=0,	maxz=0,	type='tile'):
		self.tiles.append(tile(minx,	maxx,	miny,	maxy,	minz,	maxz,	type))

	def	add_zone(self,	minx=0,	maxx=0,	miny=0,	maxy=0,	minz=0,	maxz=0,	name='zone'):
		self.zones.append(zone(minx,	maxx,	miny,	maxy,	minz,	maxz,	name))

	def	set_name(self,	name):
		self.name	=	name

	def	set_borders(self,	coords):
		x,	y,	z	=	coords
		self.maxx,	self.maxy,	self.maxz	=	x,	y,	z

	def	get_tile(self,	x=0,	y=0,	z=0):
		try:
			t = get_tile_obj(x, y, z)
			if t:
				return t.type
			else:
				return ""
		except	Exception	as	e:
			pass

	def get_tile_obj(self, x=0, y=0, z=0):
		filter = [i for i in self.tiles if i.covers(x, y, z)]
		try:
			if filter[-1]:
				return filter[-1]
		except Exception as e:
			pass

	def get_zone(self, x=0, y=0, z=0):
		try:
			z = self.get_zone_obj(x, y, z)
			if z:
				return z.name
			else:
				return ""
		except Exception as e:
			pass

	def	get_zone_obj(self,	x=0,	y=0,	z=0):
		filter	=	[i	for	i	in	self.zones	if	i.covers(x,	y,	z)]
		try:
			if filter[-1]:
				return	filter[-1]
		except	Exception	as	e:
			pass

	def delete_tile_at(self, x=0, y=0, z=0):
		try:
			t = self.get_tile_obj(x, y, z)
			if t:
				self.tiles.remove(t)
		except Exception as e:
			pass

	def delete_zone(self, x=0, y=0, z=0):
		try:
			z = self.get_zone_obj(x, y, z)
			if z:
				self.zones.remove(z)
		except Exception as e:
			pass

	def	dump(self,	in_file=False,	file=''):
		try:
			self.tiles	=	[i.__dict__	for	i	in	self.tiles]
			self.zones	=	[i.__dict__	for	i	in	self.zones]
			data2	=	{"name":	self.name,	"borders":	[self.maxx,	self.maxy,	self.maxz],	"items":	self.tiles+self.zones}
			if	in_file==True	and	file!='':	
				with	open(file,	'w')	as	f:
					f.write(json.dumps(data2,	indent=1))
			else:
				return	json.dumps(data2,	indent=1)
		except	Exception	as	e:
			pass

	def	load(self,	data='',	from_file=False,	name=''):
		try:
			if	from_file	and	name!='':
				with	open(name,	'r')	as	f:
					data	=		json.loads(f.read())
			else:
				data	=	json.loads(data)
			self.name	=	data['name']
			self.maxx,	self.maxy,	self.maxz	=	data['borders']
			self.tiles	=	[tile(t['minx'],	t['maxx'],	t['miny'],	t['maxy'],	t['minz'],	t['maxz'],	t['type'])	for	t	in	data['items']	if	t['type']	in	tiles]
			self.zones	=	[zone(t['minx'],	t['maxx'],	t['miny'],	t['maxy'],	t['minz'],	t['maxz'],	t['name'])	for	t	in	data['items']	if	'name'	in	t.keys()]
		except	Exception	as	e:
			pass
