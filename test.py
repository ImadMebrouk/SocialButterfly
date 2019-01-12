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
    r.hset(usr, "user_id", index + 1)

    for key, value in kwargs.items():         
        r.hset(usr, key, value)
        
        
    r.incr("compteur")
    return r.hget(usr, "user_id")

def get_user_by_id(user_id):

    keys = {"username", "first_name","last_name"}
    return r.hmget('user.' + user_id, keys)

def add_Friend(user_id, friend_id):
    
    r.lpush('user.'+user_id+'.friendsList', friend_id)
    r.lpush('user.'+friend_id+'.friendsList', user_id)

def  delete_friend(user_id, friend_id): #toDo 
    return null

Imad = {
    'id': '1',
    'username': 'coach',
    'password': 'password',
    'first_name': 'Imad',
    'last_name': 'Mebrouk',
    'age':'23',
    'gender':'male',
    'location': 'Sannois'
}


create_user('coach', **Imad)

print(get_user_by_id('1'))

