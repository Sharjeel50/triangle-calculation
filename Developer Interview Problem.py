import csv
from Triangle import Triangle


class DataResult:
    def __init__(self, file):
        self._file = file
        self.tupled_data()

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

        # Loop through yielded data
        # Keep key as product and values as the rest and return
        for objects in self.triangle_product_creation():
            if objects.product not in products:
                products[objects.product] = [
                    [objects.origin_year, objects.development_year, objects.incremental_value]]
            else:
                products[objects.product] += [
                    [objects.origin_year, objects.development_year, objects.incremental_value]]
        return products

    def tupled_data(self):
        data = []
        for k, rows in self.product_splitting().items():
            for row in rows:
                item = (k, row[0], row[1], row[2])
                data.append(item)

        self.do_calc(data)

    def do_calc(self, data):
        res = []

        # Loop through data
        # Check if products match
        # Check if the origin and development year match, if they do append
        # Else check the num of iterations between origin and development year
        # If its one or two, do the calcs manually,
        # Else create a for loop between iterations and add all vals to incremental_val
        # Append it to res
        # Read last product from data since i am looping through minus 1
        # Do the same cals on the last product and append to res
        for i in range(len(data) - 1):
            if data[i][0] == data[i + 1][0]:
                if data[i][1] == data[i][2]:
                    res.append((data[i][0], data[i][3]))
                else:
                    iterations = int(data[i][2]) - int(data[i][1])
                    if iterations == 1:
                        res.append((data[i][0], float(data[i][3]) + float(data[i - 1][3])))
                    elif iterations == 2:
                        res.append((data[i][0], float(data[i][3]) + float(data[i - 1][3]) + float(data[i - 2][3])))
                    else:
                        incremental_val = 0
                        for iterations_range in range(iterations):
                            incremental_val += float(data[i - iterations_range][3])
                        if data[i][2] != int(data[i - 1][2]) - 1:
                            res.append((data[i][0], incremental_val - float(data[i][3])))
                        res.append((data[i][0], incremental_val))
            else:
                if data[i][1] == data[i][2]:
                    res.append((data[i][0], data[i][3]))
                else:
                    res.append((data[i][0], float(data[i][3]) + float(data[i - 1][3])))

        if data[-1][1] == data[-1][2]:
            res.append((data[-1][0], data[-1][3]))
        elif int(data[-2][1]) + 1 == int(data[-1][2]):
            res.append((data[-1][0], float(data[-1][3]) + float(data[-2][3])))

        print(res)

        return res

    # Make new csv file and add it to the current folder with the result data inside
    # print out that the file is made
    def make_res_csv(self):
        with open("results_" + self._file, 'w', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow()


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
