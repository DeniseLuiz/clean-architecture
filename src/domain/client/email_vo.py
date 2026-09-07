

class Email():
    value: str
    
    def __init__(self, value):
        self.value = value
        
    def __post_init__(self):
        pass
    
    def validate(self):
        if not self.valor or not self.valor.strip():
            raise ValueError('This value is required')
        if '.' not in self.valor or '@' not in self.valor:
            raise ValueError('Invalid value. You must have the required taxonomy')