from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from unit import BaseUnit


class Skill(ABC):
    """
    Базовый класс умения
    """
    user = None
    target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def skill_effect(self) -> str:
        pass

    def _is_stamina_enough(self):
        return self.user.stamina > self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        """Проверяет, достаточно ли выносливости у игрока для применения умения (для вызова скилла используется use)
        """
        self.user = user
        self.target = target
        if self._is_stamina_enough:
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости"


class FuryPunch(Skill):
    name = "Яростный удар"
    stamina = 6
    damage = 12

    def skill_effect(self) -> str:
        """Логика использования скилла: уменьшение выносливости у игрока, применяющего умение, и уменьшение здоровья
        цели"""
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)

        return f"{self.user.name} использует навык {self.name} и наносит {self.damage} урона противнику. "


class HardShot(Skill):
    name = "Сильный выстрел"
    stamina = 5
    damage = 15

    def skill_effect(self) -> str:
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)

        return f"{self.user.name} использует навык {self.name} и наносит {self.damage} урона противнику. "

class Shot(Skill):
    name = "Обычный удар"
    stamina = 2
    damage = 4

    def skill_effect(self) -> str:
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)

        return f"{self.user.name} использует навык {self.name} и наносит {self.damage} урона противнику. "

class KnifePunch(Skill):
    name = "Удар скрытым оружием"
    stamina = 10
    damage = 25

    def skill_effect(self) -> str:
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)

        return f"{self.user.name} использует навык {self.name} и наносит {self.damage} урона противнику. "