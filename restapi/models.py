import logging
import datetime

from peewee import SqliteDatabase, Model, CharField, BooleanField, IntegerField

from config import Config


logging.basicConfig(format='===========My:%(levelname)s:%(message)s=========', 
    level=logging.DEBUG)


conf = Config()
# create a peewee database instance -- our models will use this database to
# persist information
database = SqliteDatabase('account.sqlite3')

# model definitions -- the standard "pattern" is to define a base model class
# that specifies which database to use.  then, any subclasses will automatically
# use the correct storage.
class BaseModel(Model):
    class Meta:
        database = database


class AccountModel(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = CharField()
    account_level = IntegerField()

    class Meta:
        order_by = ('username',)


def create_tables():
    database.connect()
    database.create_tables([AccountModel], safe=True)


def test():
    # AccountModel.create(username='username', 
    #                 password='password',
    #                 email='email',
    #                 join_date=str(datetime.datetime.now())+' GMT+8',
    #                 account_level=0)
    logging.debug('in account post create except')

            # `username` is a unique column, so this username already exists,
            # making it safe to call .get().
    old_user = AccountModel.get(AccountModel.username == 'user1')
    logging.debug('user exists:%s'%old_user.email)
# create_tables()

# test()