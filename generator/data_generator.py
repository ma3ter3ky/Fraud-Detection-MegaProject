import random
from datetime import datetime, timedelta
import pandas as pd
from ..entities.user import User
from ..entities.merchant import Merchant
from ..entities.transaction import Transaction


class DataGenerator:
    def __init__(self, n_users=1000, n_merchants=200, n_txns=10000, fraud_strategies=None):
        self.n_users = n_users
        self.n_merchants = n_merchants
        self.n_txns = n_txns
        self.users = [User(i) for i in range(n_users)]
        self.merchants = [Merchant(i) for i in range(n_merchants)]
        self.fraud_strategies = fraud_strategies or []

    def _is_fraudulent(self, txn):
        for strategy in self.fraud_strategies:
            if strategy.apply(txn):
                return True
        return False

    def generate(self):
        print(f"Generating {self.n_txns} transactions...")
        data = []
        start_time = datetime.utcnow()

        for i in range(self.n_txns):
            user = random.choice(self.users)
            merchant = random.choice(self.merchants)
            timestamp = start_time + timedelta(seconds=i * random.uniform(0.1, 2.0))
            txn = Transaction(user, merchant, timestamp, False)
            txn.is_fraud = int(self._is_fraudulent(txn))
            data.append(vars(txn))

        df = pd.DataFrame(data)
        return df

    def save_csv(self, filename="transactions.csv"):
        df = self.generate()
        df.to_csv(filename, index=False)
        print(f"✅ Saved {len(df)} transactions to {filename}")
