from bson import ObjectId

def user_serializer(user: dict) -> dict:
    return {
        'id': str(ObjectId(user.get('_id'))),
        'username': user.get('username'),
        'password': user.get('password')
    }
    
def users_serializer(users: list) -> list:
    return [user_serializer(user) for user in users]
    