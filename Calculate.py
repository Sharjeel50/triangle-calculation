import csv
from Triangle import Triangle


class DataResult:
    def __init__(self, file):
        self.res = []
        self._file = file
        self.res = []
        self.tupled_data()

    # Yielded to save memory
    def create_triangle_objects(self):
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
        for objects in self.create_triangle_objects():
            if objects.product not in products:
                products[objects.product] = [
                    [objects.origin_year, objects.development_year, objects.incremental_value]]
            else:
                products[objects.product] += [
                    [objects.origin_year, objects.development_year, objects.incremental_value]]
        return products

    # Tuple all the data up along side the correct vals (origin_date, development_date, incremental_val)
    # Run self.do_calc on the data
    def tupled_data(self):
        data = []
        for k, rows in self.product_splitting().items():
            for row in rows:
                item = (k, row[0], row[1], row[2])
                data.append(item)

        self.do_calc(data)

    def do_calc(self, data):
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
                    self.res.append((data[i][0], data[i][3]))
                else:
                    iterations = int(data[i][2]) - int(data[i][1])
                    if iterations == 1:
                        self.res.append((data[i][0], float(data[i][3]) + float(data[i - 1][3])))
                    elif iterations == 2:
                        self.res.append((data[i][0], float(data[i][3]) + float(data[i - 1][3]) + float(data[i - 2][3])))
                    else:
                        self.do_calc_iterations(data, i, iterations)
            else:
                if data[i][1] == data[i][2]:
                    self.res.append((data[i][0], data[i][3]))
                else:
                    self.res.append((data[i][0], float(data[i][3]) + float(data[i - 1][3])))

        if data[-1][1] == data[-1][2]:
            self.res.append((data[-1][0], data[-1][3]))
        elif int(data[-2][1]) + 1 == int(data[-1][2]):
            self.res.append((data[-1][0], float(data[-1][3]) + float(data[-2][3])))

        print(self.res)

    def do_calc_iterations(self, data, i, iter):
        incremental_val = 0
        actual_dates = []
        missing_dates = 0
        for iterations_range in range(iter):
            incremental_val += float(data[i - iterations_range][3])
            expected_dates = list(range(int(data[i][1]), int(data[i][2]) + 1))
            actual_dates.append(int(data[i - iterations_range][2]))
            missing_dates = list(set(expected_dates) - set(actual_dates))
        for p in range(len(missing_dates)):
            if missing_dates[p] == int(data[i][2]) - p - 1:
                self.res.append((data[i][0], incremental_val - float(data[i][3])))
        self.res.append((data[i][0], incremental_val))

    # Make new csv file and add it to the current folder with the result data inside
    # print out that the file is made
    def make_res_csv(self):
        with open("Result_File_" + self._file, 'w', newline='') as my_file:
            wr = csv.writer(my_file, quoting=csv.QUOTE_ALL)
            wr.writerow(self.res)
            print("Result_File_" + self._file, "Created, Check your directory!")