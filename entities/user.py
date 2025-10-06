import uuid
import random
import numpy as np
from faker import Faker

fake = Faker()


class User:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.country = fake.country_code()
        self.avg_amount = np.random.lognormal(mean=3, sigma=0.5)
        self.active_hours = random.sample(range(24), 8)
        self.cards = [str(uuid.uuid4()) for _ in range(random.randint(1, 2))]
        self.device_pool = [str(uuid.uuid4()) for _ in range(random.randint(1, 3))]

    def sample_amount(self):
        return round(float(np.random.lognormal(np.log(self.avg_amount), 0.6)), 2)

    def sample_device(self):
        return random.choice(self.device_pool)
