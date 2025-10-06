class FraudStrategy:
    def apply(self, txn) -> bool:
        raise NotImplementedError
