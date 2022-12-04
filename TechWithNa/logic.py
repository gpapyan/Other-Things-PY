from user import  User
from post import  Post

app_user_one = User("nnn@gmail.com", "Johny Smith", "Pa$$w0rd", "Developer")
app_user_one.get_user_info()

new_post = Post("on a secret mission today", app_user_one.name)
new_post.get_post_info()
