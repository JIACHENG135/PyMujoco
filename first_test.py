from pyh import *
page = PyH('My wonderful PyH page')
# page.addCSS('myStylesheet1.css', 'myStylesheet2.css')
# page.addJS('myJavascript1.js', 'myJavascript2.js')
page << h1('My big title', cl='center')
page << div(cl='myCSSclass1 myCSSclass2', id='myDiv1') << p('I love PyH!', id='myP1')
mydiv2 = page << div(id='myDiv2')
mydiv2 << h2('A smaller title') + p('Followed by a paragraph.')
page << div(id='myDiv3')
page.myDiv3.attributes['cl'] = 'myCSSclass3'
page.myDiv3 << p('Another paragraph')
# page.printOut()
print(page.render())

GEN_HTML = "demo_1.html"  #命名生成的html
f = open(GEN_HTML,'w')
message = page.render()
f.write(message)
f.close()