class Item:
    
    def __init__(self, weight: float):
        self.weight = weight

class Player:
    inventory = []

    def __init__(self, *args: list[Item]):
        # print(*args)
        if args and all([True if isinstance(item, Item) else False for item in args[0]]):
            self.inventory.extend(*args)

        else: raise TypeError('Not all the given objects are Item class instances')

    def add_item(self, item: Item):
        if isinstance(item, Item):
            self.inventory.append(item)
        else: raise TypeError()

    def find_heaviest_item(self): # Главная функция здесь :)
        # return max([item.weight for item in self.inventory])
        if self.inventory:
            max_value = self.inventory[0].weight
            for elem in self.inventory:
                if elem.weight > max_value: max_value = elem.weight
            return max_value
    
player = Player([Item(5), Item(7)])
player.add_item(Item(weight=2))
# player.add_item('cheater')

print(player.find_heaviest_item())
# Создаем два класса: для игрока и для предмета. метод max находит наибольшее значение в списке