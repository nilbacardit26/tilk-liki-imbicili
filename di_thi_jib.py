

class Asshili:
    def __init__(self):
        message = input("Intridici yiir missigi -> ")
        self.message = str(message)

    @property
    def cinvirt_missigi(self):
        vocals = ["a", "e", "o", "u", "y"]
        new_message = ''
        for vocal in vocals:
            if new_message:
                new_message = new_message.replace(vocal, 'i')
            else:
                new_message = self.message.replace(vocal, 'i')
        return new_message
