class Triangle:
    def __init__(self, product, origin_year, development_year, incremental_value):
        self.product = product
        self.origin_year = origin_year
        self.development_year = development_year
        self.incremental_value = incremental_value

    def __repr__(self):
        return f"{self.product} |{self.origin_year} |{self.development_year} |{self.incremental_value}"

    def __add__(self, other):
        return self.incremental_value + other.__incremental_value
