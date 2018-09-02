class State:
    def __init__(self, hour):
        self.hour = hour

    def write_program(self):
        pass


class ForenoonState(State):
    def write_program(self):
        if (self.hour < 12):
            print('当前时间：{0}点 上午，精神百倍'.format(self.hour))
        # else:
        #    self.state = NoonState()
        #    self.state.write_program()


class NoonState(State):
    def write_program(self):
        if (self.hour < 13):
            print('当前时间：{0}点 饿了，午饭；犯困，午休。'.format(self.hour))
        else:
            self.state.state = AfternoonState()
            self.state.write_program()


class AfternoonState(State):
    def write_program(self):
        if (self.hour < 17):
            print('当前时间：{0}点 下午状态还不错，继续努力'.format(self.hour))
        else:
            self.state = EveningState()
            self.state.write_program()


class EveningState(State):
    def write_program(self):
        if (self.hour < 21):
            print('当前时间：{0}点 加班哦，疲累之极'.format(self.hour))
        else:
            self.state = SleepingState()


class SleepingState(State):
    def write_program(self):
        print('当前事件：{0}点不行了，睡着了。'.format(self.hour))


class RestState(State):
    def write_program(self, work):
        print('当前事件：{0}下班回家了。'.format(self.hour))


class Work:
    def __init__(self, hour):
        self.hour = hour
        self.state = ForenoonState()

    # finish = False
    # def set_finish(self, value):
    #     self.finish = value
    #
    # def get_finish(self):
    #     return self.finish

    def write_program(self):
        self.state.write_program()


if __name__ == '__main__':
   state1 = ForenoonState(9)
   state1.write_program()

   state2 = NoonState(12)
   state2.write_program()


