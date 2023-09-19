from data_wrappers_interface import DataWrapperInterface
# create a CreditScoringWrapper class


class CreditScoringWrapper(DataWrapperInterface):
    @staticmethod
    def _exported_features(): return ["age", "income", "loan_amount",
                                      "loan_duration", "number_of_dependents"]

    @staticmethod
    def _config_keys(): return ["url", "username", "password"]

    def __init__(self, config) -> None:
        self.config = config

    def request(self, input: str) -> list:
        # use self.config to fetch the data from the Data Source
        return {"feature_a": "value_a", "feature_b": "value_b"}
