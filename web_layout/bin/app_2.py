#ex51 Getting Input from a Browser
#Web layout

import web

urls = (
	'/hello', 'Index',
	'/upload', 'Upload'
	
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
	def GET(self):
		return render.hello_form()
		
	def POST(self):
		form = web.input (name = "Nobody", greet = "Hello")
		greeting = "Hello, %s, %s" % (form.greet, form.name)
		return render.index(greeting = greeting)
				
class Upload(object):
	def GET(self):
		return render.upload_form_try()
		
	def POST(self):
		form = web.input (fname = "No file") #, pname = "No path")
		#message = "You chose, %s, %s" % (form.fname, form.pname)
		greeting = "You chose, %s" % (form.fname)
		fpath = form.pname
		#savepath = "E:\!5 Files\Filestock_Python\projects"
		
		#fread = open(fpath)
		#fread
		# fcontent = fread.read
		# fpaste = open(savepath&fname, w)
		# fpaste.write(fcontent)
		
		# fread.close
		# fpaste.close
		#confirm = "Upload done."
		return render.upload_saving (greeting=greeting, fpath=fpath)
							
if __name__ == "__main__":
	app.run()