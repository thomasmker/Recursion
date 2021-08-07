class Person():
    def __init__(self) -> None:
        self.nextInLine = None

def get_my_position_in_line(person):
    """Get the position in line"""
    if person.nextInLine is None:
        return 1
    
    return 1 + get_my_position_in_line(person.nextInLine)
    
ana = Person()
joe = Person()
dave = Person()
peter = Person()

ana.nextInLine = joe
joe.nextInLine = dave
dave.nextInLine = peter

print(get_my_position_in_line(ana))



