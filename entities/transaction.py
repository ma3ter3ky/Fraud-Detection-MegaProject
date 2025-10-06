import uuid
import random
from faker import Faker

fake = Faker()


class Transaction:
    def __init__(self, user, merchant, timestamp, is_fraud: bool):
        self.txn_id = str(uuid.uuid4())
        self.event_time = timestamp.isoformat()
        self.account_id = user.user_id
        self.card_id = random.choice(user.cards)
        self.merchant_id = merchant.merchant_id
        self.amount = user.sample_amount()
        self.currency = "USD"
        self.mcc = merchant.mcc
        self.channel = random.choice(["pos", "ecommerce"])
        self.device_id = user.sample_device()
        self.ip_addr = fake.ipv4()
        self.merchant_country = merchant.country
        self.user_country = user.country
        self.auth_method = random.choice(["chip", "3DS", "contactless", "online"])
        self.is_fraud = int(is_fraud)
