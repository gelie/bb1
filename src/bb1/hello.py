class Hello(object):

    def getText(self):
        name = self.request.get('name')
        if name:
            return "Hello %s !" % name
        else:
            return "Hello ! What's your name ?"
