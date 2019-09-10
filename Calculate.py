import csv
from Triangle import Triangle


class DataResult:
    def __init__(self, file):
        self._file = file
        self.res, self.dates = [], []
        self.tupled_data()
        self.make_res_csv()

    # Yielded to save memory instead of adding each obj to memory(in a list)
    # Create some checks on the file while looping through it
    # Let user know
    def create_triangle_objects(self):
        with open(self._file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            # Skip Headers
            next(csv_reader)
            c = 0
            for data in csv_reader:
                c += 1
                try:
                    if len(data) != 4:
                        print("Your file contains an error on line - ", c + 1, " - ", data)
                        print("Only the first four indexes will be used.")
                        print("\n")
                    # product, origin_year, development_year, incremental_value
                    yield Triangle(data[0], data[1], data[2], data[3])
                except Exception as e:
                    print(e)

    def group_data_splitting(self):
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
        for k, rows in self.group_data_splitting().items():
            for row in rows:
                item = (k, row[0], row[1], row[2])
                data.append(item)

        self.calculate_icremental_value(data)

    def calculate_icremental_value(self, data):
        # Append dates into self.dates for later use
        # Loop through data
        # Check if products match
        # Check if the origin and development year match, if they do append curr incremental val
        # Else check the num of iterations between origin and development year
        # If its one, do the calcs manually,
        # Run self.do_calc_iterations
        # Read last product from data since i am looping through minus 1
        # Do the same cals on the last product and append to res
        for i in data:
            self.dates.append(int(i[1]))
            self.dates.append(int(i[2]))

        for i in range(len(data) - 1):
            if data[i][0] == data[i + 1][0]:
                if data[i][1] == data[i][2]:
                    self.res.append((data[i][0], data[i][3]))
                else:
                    iterations = int(data[i][2]) - int(data[i][1])
                    if iterations == 1:
                        self.res.append((data[i][0], float(data[i][3]) + float(data[i - 1][3])))
                    elif iterations > 1:
                        self.icremental_value_iterations(data, i, iterations)
            else:
                if data[i][1] == data[i][2]:
                    self.res.append((data[i][0], data[i][3]))
                else:
                    self.res.append((data[i][0], float(data[i][3]) + float(data[i - 1][3])))

        if data[-1][1] == data[-1][2]:
            self.res.append((data[-1][0], data[-1][3]))
        elif int(data[-2][1]) + 1 == int(data[-1][2]):
            self.res.append((data[-1][0], float(data[-1][3]) + float(data[-2][3])))
        else:
            inc_val = 0
            for i in range(int(data[-1][2]) - int(data[-1][1]) + 1):
                inc_val += float(data[-1 - i][3])
            self.res.append((data[-1][0], inc_val))

    # Loop through iteration range passed in
    # Get the missing dates
    # Loop through the range for missing dates
    # Check if the missing dates would equal development year
    # If it is, append data
    # Append normal incremetal_vals without missing dates at the end
    def icremental_value_iterations(self, data, i, iter):
        actual_dates = []
        incremental_val = 0
        missing_dates = 0
        for iterations_range in range(iter + 1):
            if data[i][0] == data[i - iterations_range][0]:
                incremental_val += float(data[i - iterations_range][3])
            expected_dates = list(range(int(data[i][1]), int(data[i][2]) + 1))
            actual_dates.append(int(data[i - iterations_range][2]))
            missing_dates = list(set(expected_dates) - set(actual_dates))
        for p in range(len(missing_dates)):
            if missing_dates[p] == int(data[i][2]) - p - 1:
                self.res.append((data[i][0], incremental_val - float(data[i][3])))
        self.res.append((data[i][0], incremental_val))

    # Loop through self.res and put all the revelant data together
    # Get the length of the max value in the dict for later use
    # loop through data and check if the length of value is equal to max value,
    # if it isnt, get the difference between the max val and length of current list
    # and add 0's to the start.
    def format_results(self):
        data = {}
        for i in self.res:
            if i[0] not in data:
                data[i[0]] = [float(i[1])]
            else:
                data[i[0]] += [float(i[1])]

        long_val = max(data, key=lambda x: len(data[x]))

        for key, value in data.items():
            if len(data[key]) != len(data[long_val]):
                for i in range(len(data[long_val]) - len(data[key])):
                    data[key].insert(0, 0)
            print(key, value)
        print("\n")

        return data

    # Make new csv file and add it to the current folder with the result data inside
    # print out that the file is made
    def make_res_csv(self):
        with open("Result_File_" + self._file, 'w', newline='') as my_file:
            wr = csv.writer(my_file, quoting=csv.QUOTE_ALL)
            wr.writerow([min(self.dates), max(self.dates) - min(self.dates) + 1])
            for i, j in self.format_results().items():
                wr.writerow([i, ",".join(str(i) for i in j)])
            print("Result_File_" + self._file, "Created, Check your directory!")
