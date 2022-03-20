from abc import ABC, abstractmethod


class WareHouse:
    __storage = []

    def put(self, device):
        self.__storage.append(device)

    def get(self, count = None, **kwargs):
        res_list = []
        for el in self.__storage:
            for k, v in kwargs.items():
                if getattr(el, k) != v:
                    break
            else:
                res_list.append(el)
                if count:
                    count -= 1
                    if not count:
                        break
        for el in res_list:
            self.__storage.remove(el)
        return res_list

    def __len__(self):
        return len(self.__storage)

    def get_report(self):
        pres = {}
        for el in self.__storage:
            ce = pres.get(el.device_type) or 0
            ce += 1
            pres[el.device_type] = ce
        return "На складе находится {}".format(str(pres).strip('{}'))


class OfficeEquipment(ABC):
    serial_number: int
    model: str
    manufacturer: str
    cost: int

    def __init__(self, manufacturer, model, serial_number, cost):
        self.manufacturer = manufacturer
        self.model = model
        if not type(serial_number) is int:
            raise ValueError('Unsupported type for serial number')
        self.serial_number = serial_number
        if not type(cost) is int:
            raise ValueError('Unsupported type for cost')
        self.cost = cost

    @property
    @abstractmethod
    def device_type(self):
        pass


class Printer(OfficeEquipment):
    __serial = 0

    def __init__(self, manufacturer, model, speed, cost=0):
        Printer.__serial += 1
        super().__init__(manufacturer, model, Printer.__serial, cost)
        self.speed = speed

    @property
    def device_type(self):
        return 'Printer'


class Scanner(OfficeEquipment):
    __serial = 0

    def __init__(self, manufacturer, model, size, cost=0):
        Scanner.__serial += 1
        super().__init__(manufacturer, model, Scanner.__serial, cost)
        self.size = size

    @property
    def device_type(self):
        return 'Scanner'


class Copier(OfficeEquipment):
    __serial = 0

    def __init__(self, manufacturer, model, speed, size, resolution, cost):
        Copier.__serial += 1
        super().__init__(manufacturer, model, Copier.__serial, cost)
        self.speed = speed
        self.size = size
        self.resolution = resolution

    @property
    def device_type(self):
        return 'Xerox'


if __name__ == '__main__':

    wh = WareHouse()
    p1 = Printer('Samsung', 'ml100', 120, 1200)
    p2 = Printer('Brother', 'br100', 120, 1000)
    s1 = Scanner('Hp', 'iScan', 'A4', 500)
    s2 = Scanner('Brother', 'Superscan', 'A3', 1500)
    c1 = Copier('Canon', 'imageRunner', 100, 'A4', 1200, 2500)
    c2 = Copier('Xerox', 'Workcentr', 100, 'A4', 2400, 2500)

    wh.put(p1)
    wh.put(p2)
    wh.put(s1)
    wh.put(s2)
    wh.put(c1)
    wh.put(c2)
    print('на складе', len(wh), 'шт')
    print(wh.get_report())

    wh.get(device_type='Scanner', size='A4')
    wh.get(device_type='Printer', cost=1200)
    print('на складе', len(wh), 'шт')
    print(wh.get_report())
