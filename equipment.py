from dataclasses import dataclass
from typing import List, Optional
from random import uniform

import marshmallow
import marshmallow_dataclass

import json


@dataclass
class Armor:
    """Описание экземпляра брони"""
    id: int
    name: str
    defence: float
    stamina_per_turn: float

@dataclass
class Weapon:
    """Описание экземпляра оружия"""
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        """Расчёт урона"""
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class EquipmentData:
    """Содержит 2 списка - с оружием и с броней"""
    weapons: List[Weapon]
    armors: List[Armor]


class Equipment:
    """Класс представляет собой интерфейс для взаимодействия с классом BaseUnit"""

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name: str) -> Weapon:
        """Возвращает объект оружия по имени"""
        for weapon in self.equipment.weapons:
            if weapon.name == weapon_name:
                return weapon
        raise ValueError

    def get_armor(self, armor_name: str) -> Armor:
        """Возвращает объект брони по имени"""
        for armor in self.equipment.armors:
            if armor.name == armor_name:
                return armor
        raise ValueError

    def get_weapons_names(self) -> list:
        """Возвращает список с названиями оружия"""
        weapons = self.equipment.weapons
        weapons = [weapon.name for weapon in weapons]
        return weapons

    def get_armors_names(self) -> list[str]:
        """Возвращает список с названиями брони"""
        armors = self.equipment.armors
        armors = [armor.name for armor in armors]
        return armors

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        """Метод загружает json в EquipmentData"""
        with open("./data/equipment.json", encoding="utf-8") as equipment_file:
            data = json.load(equipment_file)
            equipment_file.close()
            equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)

            try:
                return equipment_schema().load(data)
            except marshmallow.exceptions.ValidationError:
                raise ValueError

