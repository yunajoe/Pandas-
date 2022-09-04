class Post:
    # 게시글 클래스 
    def __init__(self, date, content):
        self.date= date 
        self.content= content 
        
    def __str__(self):
        return "게시일: {}\n내용: {}".format(self.date, self.content)
    
    
class BlouUser:
    # 유저 클라쓰 
    def __init__(self, name):
        self.name = name 
        self.posts = []
        
    def add_post(self, date, content):
        new_post = Post(date, content)
        self.posts.append(new_post)
        
    def show_all_posts(self):
        for post in self.posts:
            print(post) 
                  
    def __str__(self):
        return "안녕하세요 {}입니다.\n".format(self.name)
        
    
user1 = BlouUser("yuna")
print(user1)

user1.add_post("2019년 8월 30일", """오늘은 내 생일이였다.
많은 사람들이 축하해줬다.
행복했다.""")

user1.show_all_posts()