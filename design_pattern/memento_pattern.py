# Orinator：游戏角色类，负责创建Memento类，保存游戏进度
class GameCharacter:
    vitality = 0  # 生命力
    attack = 0  # 攻击力
    defense = 0  # 防御力

    def display_state(self):
        print('角色当前状态')
        print('\t生命力：%d' % self.vitality)
        print('\t攻击力：%d' % self.attack)
        print('\t防御力：%d' % self.defense)

    def init_state(self):
        self.vitality = 100
        self.attack = 100
        self.defense = 100

    def fight(self):
        self.vitality = 0
        self.attack = 0
        self.defense = 0

    # 创建Memento对象，保存状态
    def save_state(self):
        return RoleStateMemento(self.vitality, self.attack, self.defense)

    # 根据Memento对象恢复游戏的状态
    def recovery_state(self, memento):
        self.vitality = memento.vitality
        self.attack = memento.attack
        self.defense = memento.defense


# Memento：角色状态存储器
class RoleStateMemento:
    vitality = 0
    attack = 0
    defense = 0

    def __init__(self, vitality, attack, defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense


# Caretaker：角色状态管理者，设置或获取Memento状态存储器
class RoleStateCareTaker:
    memento = None


def client_ui():
    print('----大战前----')
    character = GameCharacter()
    character.init_state()
    character.display_state()

    print('----保存进度----')
    state_admin = RoleStateCareTaker()
    state_admin.memento = character.save_state()

    print('---大战Boss，损耗严重----')
    character.fight()
    character.display_state()

    print('----恢复之前的状态----')
    character.recovery_state(state_admin.memento)
    character.display_state()
    return


if __name__ == '__main__':
    client_ui()
