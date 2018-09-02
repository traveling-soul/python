class User:
    _id = 0
    _name = ''

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class IUser:
    def insert(self, user):
        pass

    def get_user(self, id):
        pass

    class Meta:
        abstract = True


class SqlServerUser(IUser):
    def insert(self, user):
        print('在SQL Server中给User表增加一条记录')

    def get_user(self, id):
        print('在SQL Server中根据id得到User表一条记录')
        return None


class AccessUser(IUser):
    def insert(self, user):
        print('在Access中给User表增加User表一条记录')

    def get_user(self, id):
        print('在Access中根据id得到User一条记录')
        return None


class IFactory:
    def create_user(self):
        pass

    class Meta:
        abstract = True


class SqlServerFactory(IFactory):
    def create_user(self):
        return SqlServerUser()


class AccessFactory(IFactory):
    def create_user(self):
        return AccessUser()


if __name__ == '__main__':
    user = User()
    # factory = SqlServerFactory()
    factory = AccessFactory()
    iu = factory.create_user()

    iu.insert(user)
    iu.get_user(1)