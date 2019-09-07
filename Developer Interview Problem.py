import csv
from Triangle import Triangle


class DataResult:
    def __init__(self, file):
        self._file = file
        self.test()

    def triangle_product_creation(self):
        with open(self._file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            # Skip Headers
            next(csv_reader)
            for data in csv_reader:
                # product, origin_year, development_year, incremental_value
                yield Triangle(data[0], data[1], data[2], data[3])

    def product_splitting(self):
        products = {}
        for objects in self.triangle_product_creation():
            if objects.product not in products:
                products[objects.product] = [
                    [objects.origin_year, objects.development_year, objects.incremental_value]]
            else:
                products[objects.product] += [
                    [objects.origin_year, objects.development_year, objects.incremental_value]]
        return products


    def test(self):
        for k, v in self.product_splitting().items():
            print(self.product_splitting()[k])



def main():
    print("\n")
    print("Enter 'Exit' to close program")
    file = input("Enter file name: ") + ".csv".lower()
    print("\n")
    if file == "exit.csv" or file == "Exit.csv":
        exit()
    else:
        try:
            DataResult(file)
            main()
        except Exception as e:
            print(e, "\n")
            print(" - Try Again - ")
            main()


if __name__ == "__main__":
    main()
