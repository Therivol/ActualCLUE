
class Card:
    types = ["ROOM", "CHARACTER", "WEAPON"]
    names = []
    running_id = 0
    
    def __init__(self, name: str, type: int) -> None:
        self.id = self.next_id()
        self.names.append(name)
        self.type = type
        
    def __eq__(self, __value: object) -> bool:
        return self.id == __value.id
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __hash__(self) -> int:
        return self.id
        
    @property
    def name(self) -> str:
        return self.names[self.id]
    
    @property
    def type_name(self) -> str:
        return self.types[self.type]
    
    @classmethod
    def next_id(cls) -> int:
        next = cls.running_id
        cls.running_id += 1
        return next

        