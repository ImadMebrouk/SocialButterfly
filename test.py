import redis

r = redis.Redis(
    host = 'localhost',
    port=6379)


#r.set('foo', 'bar')
#value = r.get('foo')
#print(value)

def create_user(id_attr, **kwargs):
    user_id =("user." + kwargs['id'])
    user = {}

    for key, value in kwargs.items():
        user[key] = value
   
    r.hmset(user_id,user)
 

def get_user_by_id(user_id):

    keys = {"username", "first_name","last_name"}
    return r.hmget('user.' + user_id, keys)

Imad = {
    'id': '1',
    'username': 'coach',
    'password': 'password',
    'first_name': 'Imad',
    'last_name': 'Mebrouk',
    'location': 'Sannois'
}


create_user('coach', **Imad)

print(get_user_by_id('1'))
