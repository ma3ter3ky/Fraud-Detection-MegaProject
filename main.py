from fraud.random_fraud import RandomFraud
from fraud.velocity_fraud import VelocityFraud
from generator.data_generator import DataGenerator


def main():
    generator = DataGenerator(
        n_users=500,
        n_merchants=100,
        n_txns=5000,
        fraud_strategies=[
            RandomFraud(0.02),
            VelocityFraud(window_minutes=1, threshold=4)
        ]
    )
    generator.save_csv("transactions.csv")


if __name__ == "__main__":
    main()
