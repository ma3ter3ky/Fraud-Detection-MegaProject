import random
from faker import Faker

fake = Faker()

class Merchant:
    def __init__(self, merchant_id: int):
        self.merchant_id = merchant_id
        self.country = fake.country_code()
        self.mcc = random.choice([5311, 5812, 5732, 4111, 6011])
        self.risk_score = random.uniform(0, 1)
