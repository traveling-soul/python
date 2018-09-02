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


class SqlServerDepartment(Department):
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


class DataAccess:
    # 数据库名称，可替换成SqlServer
    def __init__(self, db):
        self.db = db

    def create_user(self):
        result = None
        if self.db == 'SqlServer':
            result = SqlServerUser()
        elif self.db == 'Access':
            result = AccessUser()
        return result

    def create_department(self):
        result = None
        if self.db == 'SqlServer':
            result = SqlServerDepartment()
        elif self.db == 'Access':
            result = AccessDepartment()
        return result


if __name__ == '__main__':
    user = User()
    department = Department()

    da = DataAccess('Access')

    iu = da.create_user()
    iu.insert(user)
    iu.get_user(1)

    id = da.create_department()
    id.insert(department)
    id.get_department(1)