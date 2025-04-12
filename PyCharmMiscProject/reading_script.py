import numpy as np
import pandas as pd


def generate_series():
    np.random.seed(242)
    data = np.random.normal(size=120)
    data = data ** 3
    data_series = pd.Series(data, index=[i * 3 for i in range(len(data))])
    count_positive = (data_series > 0).sum()
    print(f"Количество значений серии больше нуля: {count_positive}")


def read_data():
    tr_types = pd.read_csv('data/tr_types.csv', sep=',')
    transactions = pd.read_csv('data/transactions.csv', sep=',', nrows=1000000)

    print("Содержимое датафрейма tr_types:")
    print(tr_types.head())

    print("Содержимое датафрейма transactions:")
    print(transactions.head())

    return transactions


def transaction_frequency(transactions):
    transaction_counts = transactions['tr_type'].value_counts()
    top_5 = transaction_counts.head(5)
    print("Топ-5 транзакций по частоте встречаемости:")
    print(top_5)

    check_transactions = [
        "Выдача наличных в АТМ Сбербанк России",
        "Комиссия за обслуживание ссудного счета",
        "Покупка. ТУ Россия."
    ]

    for tr in check_transactions:
        if tr in top_5.index:
            print(f"'{tr}' попала в топ-5 транзакций.")
        else:
            print(f"'{tr}' не попала в топ-5 транзакций.")


if __name__ == "__main__":
    generate_series()
    transactions = read_data()
    transaction_frequency(transactions)
