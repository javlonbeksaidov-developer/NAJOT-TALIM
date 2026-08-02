class Transport:
    def __init__(self, name, tezlik, yoqilgi_hajmi, odam_soni, gildirak_soni):
        self.name = name
        self.tezlik = tezlik
        self.yoqilgi_hajmi = yoqilgi_hajmi
        self.odam_soni = odam_soni
        self.gildirak_soni = gildirak_soni

    def __str__(self):
        return f"Transport name: {self.name}"

    def info(self):
        return f"Name: {self.name}, tezlik: {self.tezlik}km/soat. Yoqilg'i hajmi {self.yoqilgi_hajmi}l. Odam son {self.odam_soni}ta sig'adi. G'ildirak soni {self.gildirak_soni}ta."

    def harakat_qilish(self):
        pass


class Car(Transport):
    def __init__(self, name, tezlik, yoqilgi_hajmi, odam_soni, gildirak_soni):
        super().__init__(name, tezlik, yoqilgi_hajmi, odam_soni, gildirak_soni)

    def harakat_qilish(self):
        return f"{self.name} yurdi."


class Bicycle(Transport):
    def __init__(self, name, tezlik, yoqilgi_hajmi, odam_soni, gildirak_soni):
        super().__init__(name, tezlik, yoqilgi_hajmi, odam_soni, gildirak_soni)

    def harakat_qilish(self):
        return f"{self.name} yurdi."


class Bus(Transport):
    def __init__(self, name, tezlik, yoqilgi_hajmi, odam_soni, gildirak_soni):
        super().__init__(name, tezlik, yoqilgi_hajmi, odam_soni, gildirak_soni)

    def harakat_qilish(self):
        return f"{self.name} yurdi."


def main():
    car = Car(name="car", tezlik=180, yoqilgi_hajmi=10, odam_soni=5, gildirak_soni=4)
    bicycle = Bicycle(name="bicycle", tezlik=15, yoqilgi_hajmi=0, odam_soni=1, gildirak_soni=2)
    bus = Bus(name="bus", tezlik=150, yoqilgi_hajmi=30, odam_soni=24, gildirak_soni=8)

    print(car)
    print(bicycle)
    print(bus)

    print(car.info())
    print(bicycle.info())
    print(bus.info())

    print(car.harakat_qilish())
    print(bicycle.harakat_qilish())
    print(bus.harakat_qilish())


if __name__ == "__main__":
    main()
