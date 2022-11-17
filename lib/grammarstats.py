class GrammarStats():
    def __init__(self):
        self.true = 0
        self.false = 0
  
    def check(self, text):
        self.text = text
        if self.text == '':
            raise Exception('Error')
        elif self.text[-1] in '.?!' and self.text[0].upper() == self.text[0]:
            self.true += 1
            return True 
        else:
            self.false += 1
            return False
  
    def percentage_good(self):
        total = self.true + self.false
        return round(self.true * 100 /(total))