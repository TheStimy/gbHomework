class Warehouse:
    def __init__(self):
        self.warehouse_equip = {}

    def stored_equipment(self, equipment):
        if equipment.type not in self.warehouse_equip:
            self.warehouse_equip[equipment.type] = {}
            self.warehouse_equip[equipment.type]['Parameters: ' + str(equipment)] =\
                'Number of units: ' + str(equipment.units)
        if equipment.name not in self.warehouse_equip[equipment.type]:
            self.warehouse_equip[equipment.type]['Parameters: ' + str(equipment)] =\
                'Number of units: ' + str(equipment.units)


class OfficeEquipment:
    def __init__(self, name, year, color, units):
        self.type = self.__class__.__name__
        self.name = name
        self.year = year
        self.color = color
        self.units = units
        self.__units = units

    @property
    def units(self):
        try:
            return self.__units
        except AttributeError as err:
            print(err)

    @units.setter
    def units(self, units):
        try:
            self.__count = int(units)
        except ValueError as err:
            print(err)


class Printer(OfficeEquipment):
    def __init__(self, name, year, color, units, printing_speed):
        super().__init__(name, year, color, units)
        self.printing_speed = printing_speed

    def __repr__(self):
        return f'{self.name}, {self.color}, {self.year}, {self.printing_speed}'


class Scanner(OfficeEquipment):
    def __init__(self, name, year, color, units, scanning_quality):
        super().__init__(name, year, color, units)
        self.scanning_quality = scanning_quality

    def __repr__(self):
        return f'{self.name}, {self.color}, {self.year}, {self.scanning_quality}'


class Xerox(OfficeEquipment):
    def __init__(self, name, year, color, units, copying_speed):
        super().__init__(name, year, color, units)
        self.copying_speed = copying_speed

    def __repr__(self):
        return f'{self.name}, {self.color}, {self.year}, {self.copying_speed}'


equipments = Warehouse()
printer = Printer('HP', 2019, 'Black', 3, 8)
equipments.stored_equipment(printer)
scanner = Scanner('Fujitsu', 2021, 'Black', 1, 10)
equipments.stored_equipment(scanner)
xerox = Xerox('Epson', 2005, 'White', 5, 3)
equipments.stored_equipment(xerox)

print(equipments.warehouse_equip)
