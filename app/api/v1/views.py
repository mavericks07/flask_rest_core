from . import v1
from app.api.v1.schemas import UserSchema
from app.core.resources import Resource
from ...core.utils.buleprint import register_api


class UserAPI(Resource):

    schema = UserSchema()


register_api(v1, UserAPI, 'user_api', '/users/', pk='pk')
