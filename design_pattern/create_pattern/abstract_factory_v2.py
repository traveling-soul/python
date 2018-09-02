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


class Department:
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


class IDepartment:
    def insert(self, department):
        pass

    def get_department(self, id):
        pass

    class Meta:
        abstract = True


class SqlserverDepartment(Department):
    def insert(self, department):
        print('在SQL Server中给Department表增加一条记录')

    def get_department(self, id):
        print('在SQL Server中根据id得到Department表一条记录')
        return None


class AccessDepartment(IDepartment):
    def insert(self, department):
        print('在Access中给Department表增加Department表一条记录')

    def get_department(self, id):
        print('在Access中根据id得到Department一条记录')
        return None


class IFactory:
    def create_user(self):
        pass

    def create_department(self):
        pass


class SqlServerFactory(IFactory):
    def create_user(self):
        return SqlServerUser()

    def create_department(self):
        return SqlserverDepartment()


class AccessFactory(IFactory):
    def create_user(self):
        return AccessUser()

    def create_department(self):
        return AccessDepartment()


if __name__ == '__main__':
    user = User()
    department = Department()
    factory = AccessFactory()

    iu = factory.create_user()
    id = factory.create_department()

    iu.insert(user)
    iu.get_user(1)

    id.insert(department)
    id.get_department(1)