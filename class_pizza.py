from constants import receipts_data


class Pizza:
    '''main class for pizza objects'''
    receipts = receipts_data

    def __init__(self, name: str, size: str):
        '''create instance'''
        self.name = name
        self.size = size
        self.receipt = self.receipts[name]

    def __eq__(self, other):
        '''check two pizzas equality'''
        return self.name == other.name and self.size == other.size

    def dict(self):
        '''show self receipt as a dict'''
        receipt_dict = {self.name: self.receipt}
        print(f'{receipt_dict}')
