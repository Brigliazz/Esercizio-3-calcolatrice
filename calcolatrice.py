class operazione


class somma(operazione)
    
    def __Init__(self, *valori):
        super().__init__("somma", *valori)
    
    def esegui(self):
        return sum(self.valori)
    


    
    
        