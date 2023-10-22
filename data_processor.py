import pandas as pd


class DataProcessor:
    def __init__(self):
        self.columns = ['Код и наименование закупки', 'Заказчик', 'Лоты', 'Ценовые предложения',
                        'Сумма, планируемая для закупки, тенге', 'Способ', 'Статус', 'Начало/окончание приема заявок',
                        'Поставщик', 'Дата подписи']

    def process_data(self, data):
        df = pd.DataFrame(data, columns=self.columns)
        return df
