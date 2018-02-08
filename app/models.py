import peewee

from app.core.models import BaseModel


class User(BaseModel):
    username = peewee.CharField(max_length=32)

    common_fields = BaseModel.common_fields + ('username',)
