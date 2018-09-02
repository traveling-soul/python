class State:
    def write_program(self):
        pass


class ForenoonState(State):
    def write_program(self, work):
        if (work.hour < 12):
            print('当前时间：{0}点 上午，精神百倍'.format(work.hour))
        else:
           self.state = NoonState()
           self.state.write_program(work)


class NoonState(State):
    def write_program(self, work):
        if (work.hour < 13):
            print('当前时间：{0}点 饿了，午饭；犯困，午休。'.format(work.hour))
        else:
            self.state = AfternoonState()
            self.state.write_program(work)


class AfternoonState(State):
    def write_program(self, work):
        if (work.hour < 17):
            print('当前时间：{0}点 下午状态还不错，继续努力'.format(work.hour))
        else:
            self.state = EveningState()
            self.state.write_program(work)


class EveningState(State):
    def write_program(self, work):
        if (work.finish):
            self.state = RestState()
            self.state.write_program(work)
        else:
            if (work.hour < 21):
                print('当前时间：{0}点 加班哦，疲累之极'.format(work.hour))
            else:
                self.state = SleepingState()
                self.state.write_program(work)


class SleepingState(State):
    def write_program(self, work):
        print('当前事件：{0}点 不行了，睡着了。'.format(work.hour))


class RestState(State):
    def write_program(self, work):
        print('当前时间：{0}下班回家了。'.format(work.hour))


class Work:
    def __init__(self, hour):
        self.hour = hour
        # 工作状态初始化为FornoonState类
        self.state = ForenoonState()
        # 工作是否完成，初始化为False
        self.finish = False

    def write_program(self):
        self.state.write_program(self)


if __name__ == '__main__':
   work = Work(9)
   work.write_program()

   work.hour = 12
   work.write_program()

   work.hour = 15
   work.write_program()

   work.hour = 17
   work.finish = True
   work.write_program()

   # work.hour = 21
   # work.write_program()


