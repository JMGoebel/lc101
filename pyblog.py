''' Python Blog Module '''

class Blog:
    ''' Blog Class '''
    def __init__(self, init_id_count = 0, init_database = {}):
        self.id_count = init_id_count
        self.db = init_database

    def increase_id(self):
        self.id_count += 1
        return self.id_count

    def add_post(self, post):
        self.db[self.increase_id()] = post

    def list_post(self):
        for item in self.db.items():
            print("ID: {} \n{}".format(item[0], str(item[1])))
    
class Post:
    ''' Blog Class '''
    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body
        self.likes = 0
    
    def __str__(self):
        return "{} \n Title: {} \n Author: {} \n Body: {} \n{}".format(
            "*" * 50, self.title, self.author, self.body, "*" * 50)

    def like(self):
        self.likes += 1


b = Blog()
p = Post("A book", "Jason Goebel", "Once upon a time...")
b.add_post(p)
b.list_post()
p = Post("Three Dogs", "Jason Goebel", "Woof woof woof")
b.add_post(p)
p = Post("Green Fields", "Jason Goebel", "The grass is greener on the other side.")
b.add_post(p)
b.list_post()