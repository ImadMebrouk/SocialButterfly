
import redis

r = redis.Redis(
    host = 'localhost',
    port=6379)




def create_user( **kwargs):

    id_count= r.exists("id_count")

    if(id_count)==1:
        count = int(r.get("id_count"))
    else:
        count = 0
        r.set("id_count", count)

    user = "user:" + str(count + 1)
    r.hset(user, "user_id", count + 1)

    for key, value in kwargs.items():         
        r.hset(user, key, value)
        
        
    r.incr("compteur")
    return r.hget(user, "user_id")

def user_connection(username, pwd):
    connection_success = False
    if(get_user_by_username(username)):
        current_password = str(r.hget("user:"+str(get_user_by_username(username)), "password"))
        if(current_password == pwd):
            connection_success = True



    return connection_success

def get_user_by_username(username):
    user_id =1
    user = "user:" + str(user_id)
    while r.hget(user,"username") != None:
        current_user =(str(r.hget(user,"username")))
        if current_user == username:
            return user_id  #user id of the corresponding username 
        else:
            user_id+=1
    return false # no user found with this username 

def get_user_by_id(user_id):

    username = r.hget("user:" + str(user_id), "username")

    if username != None:
        return username

    else:
        return False


def add_Friend(user_id, friend_id):
    
    r.lpush('user.'+user_id+'.friendsList', friend_id)
    r.lpush('user.'+friend_id+'.friendsList', user_id)

def  delete_friend(user_id, friend_id): #toDo 
    return null

Imad = {
    "username": "coach",
    "password": "password",
    "first_name": "Imad",
    "last_name": "Mebrouk",
    "age":"23",
    "gender":"male",
    "location": "Sannois",
    "friendsList": "",
    "posts": ""
    }


create_user(**Imad)

print(get_user_by_id(1))

print(user_connection("b'coach'", "b'password'")) # don't understand why "b" is added when i do hget(something)

