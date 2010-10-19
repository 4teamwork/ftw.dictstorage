
try:
    from z3c.saconfig import named_scoped_session
except:
    raise Exception("`ftw.dictstorage` should be installed with "
                    "`saconfig` extras")


class SAConfigDictStorage(object):

    def __init__(self, context, session_name):
        self.context = context
        self.session = named_scoped_session(session)

    def __getitem__(self, key):
        return self.session.query(Model).filter_by(key=key).one()

    def __setitem__(self, key, value):
        pass
        #model = Model()
        #self.session.update(Model).(Model.key==value)
        #self.session.execute()
