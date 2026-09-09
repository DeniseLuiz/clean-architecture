

class Email():
    value: str
    
    def __init__(self, value):
        self.value = value
        self.validate()
        
    def validate(self):
        if not self.value or not self.value.strip():
            raise ValueError('This value is required')
        if '.' not in self.value or '@' not in self.valor:
            raise ValueError('Invalid value. You must have the required taxonomy')