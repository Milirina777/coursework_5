from dataclasses import dataclass

from skills import Skill, FuryPunch, HardShot, KnifePunch, Shot


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(name='Воин', max_health=40.0, max_stamina=10.0, attack=3, stamina=26, armor=3.5, skill=FuryPunch())

ThiefClass = UnitClass(name='Вор', max_health=16.0, max_stamina=8.0, attack=2, stamina=22, armor=1.0, skill=Shot())

ArcherClass = UnitClass(name='Лучник', max_health=20.0, max_stamina=5.0, attack=1.5, stamina=33, armor=1.5, skill=HardShot())

AssassinClass = UnitClass(name='Ассасин', max_health=36.0, max_stamina=9.0, attack=3, stamina=35, armor=2.0, skill=KnifePunch())

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass,
    ArcherClass.name: ArcherClass,
    AssassinClass.name: AssassinClass,
}
