import pandas as pd

tr_types_data = {
    'id': [1, 2, 3],
    'type_name': [
        'Выдача наличных в АТМ Сбербанк России',
        'Комиссия за обслуживание ссудного счета',
        'Покупка. ТУ Россия.'
    ]
}

transactions_data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8],
    'tr_type': [
        'Выдача наличных в АТМ Сбербанк России',
        'Комиссия за обслуживание ссудного счета',
        'Покупка. ТУ Россия.',
        'Покупка. ТУ Россия.',
        'Выдача наличных в АТМ Сбербанк России',
        'Комиссия за обслуживание ссудного счета',
        'Покупка. ТУ Россия.',
        'Покупка. ТУ Россия.'
    ]
}

if __name__ == "__main__":
    tr_types_df = pd.DataFrame(tr_types_data)
    tr_types_df.to_csv('data/tr_types.csv', index=False, encoding='utf-8')
    transactions_df = pd.DataFrame(transactions_data)
    transactions_df.to_csv('data/transactions.csv', index=False, encoding='utf-8')
