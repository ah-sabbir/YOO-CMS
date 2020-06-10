from wsgiref.simple_server import make_server
from Template import temp_rend

class app(object):
  def __init__(self):
    #self.host = "0.0.0.0"
    pass
  def run(self):
    with make_server('',8080,self.conf) as server:
      server.serve_forever()
  
  def conf(self,environ,response):
    response("200 OK",[self.headers()])
    return self.template()
  
  def template(self):
    temp = temp_rend('index.html')
    # now we are trying to run with our own custom TEMPLATE RENDERING SYSTEM so, lets
    return [temp]
    
  def headers(self):
    return ("content-type","text/html;charset=UTF-8")


if __name__=='__main__':
  ap = app()
  ap.run()
