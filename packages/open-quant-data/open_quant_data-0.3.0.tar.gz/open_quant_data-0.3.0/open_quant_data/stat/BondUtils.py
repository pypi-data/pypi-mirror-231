import pandas as pd


class BondUtils:
    @staticmethod
    def add_double_index(dataset: pd.DataFrame, price_col: str = "price",
                         transform_ratio: str = "transform_ratio") -> pd.DataFrame:
        dataset['index'] = dataset[price_col] + dataset[transform_ratio]
        return dataset
