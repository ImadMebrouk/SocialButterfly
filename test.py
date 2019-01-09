import redis


r = redis.Redis(
    host = 'localhost',
    port=6379)


def create_user(id_attr, **kwargs):
    user_id =("user." + kwargs['id'])
    user = {}

    for key, value in kwargs.items():
        user[key] = value
   
    r.hmset(user_id,user)
 

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

