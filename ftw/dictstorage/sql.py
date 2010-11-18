
try:
    from sqlalchemy import Column
    from sqlalchemy import String
    from sqlalchemy import Text
    from sqlalchemy.ext.declarative import declarative_base
except:
    raise Exception("`ftw.dictstorage` should be installed with "
                    "`sqlalchemy` extra")


Base = declarative_base()
class DictStorageModel(Base):

    __tablename__ = 'dictstorage'

    key = Column(String(255), primary_key=True)
    value = Column(Text())

    def __init__(self, key, value=''):
        self.key = key
        self.value = value

    def __repr__(self):
        return "<DictStorageModel for key '%s'>" % self.key


class DictStorage(object):

    def __init__(self, context, session):
        self.context = context
        self.session = session

    def __getitem__(self, key):
        item = self.session.query(DictStorageModel) \
                    .filter_by(key=key) \
                    .first()
        if item is None:
            raise KeyError
        return item.value

    def __setitem__(self, key, value):
        status = self.session.query(DictStorageModel) \
                    .filter_by(key=key) \
                    .update(dict(value=value))
        if not status:
            self.session.add(DictStorageModel(key, value))

    def __delitem__(self, key):
        status = self.session.query(DictStorageModel) \
                    .filter_by(key=key) \
                    .delete()
