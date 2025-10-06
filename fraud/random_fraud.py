import random
from .base import FraudStrategy

class RandomFraud(FraudStrategy):
    def __init__(self, fraud_rate: float):
        self.fraud_rate = fraud_rate

    def apply(self, txn) -> bool:
        return random.random() < self.fraud_rate
