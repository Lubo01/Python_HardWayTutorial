try:
	from setuptools import setup
except ImportError:
	from distutils.core	import setup
	
config = [
	'description':'My Project ex49',
	'author':'My Name LL',
	'url':'URL to get it at.',
	'download url':'Where to download it',
	'author email':'My email',
	'version':'0.1',
	'install requires':['nose'],
	'packages': [ex49],
	'scripts':[],
	'name':'projectname'	
]

setup (**config)
