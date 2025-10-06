from datetime import datetime, timedelta
from .base import FraudStrategy

class VelocityFraud(FraudStrategy):
    """If too many transactions from same user in short time, mark as fraud."""
    def __init__(self, window_minutes=1, threshold=5):
        self.window = timedelta(minutes=window_minutes)
        self.threshold = threshold
        self.user_history = {}

    def apply(self, txn) -> bool:
        user_id = txn.account_id
        now = datetime.fromisoformat(txn.event_time)
        history = self.user_history.get(user_id, [])
        history = [t for t in history if now - t < self.window]
        history.append(now)
        self.user_history[user_id] = history
        return len(history) > self.threshold
