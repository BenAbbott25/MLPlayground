import csv
import torch

# load the data
def load_data():
    print("Loading data")
    # empty tensors to store data
    train_data = []
    train_labels = []
    test_data = []
    test_labels = []
    with open('mnist_train.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            for i in range(1, len(row)):
                row[i] = float(row[i])
            train_data.append(row[1:])
            train_labels.append(int(row[0]))

    with open('mnist_test.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            for i in range(1, len(row)):
                row[i] = float(row[i])
            test_data.append(row[1:])
            test_labels.append(int(row[0]))

    # convert to tensors
    train_data = torch.tensor(train_data, dtype=torch.float32)
    train_labels = torch.tensor(train_labels, dtype=torch.int64)
    test_data = torch.tensor(test_data, dtype=torch.float32)
    test_labels = torch.tensor(test_labels, dtype=torch.int64)

    # normalize the data
    train_data = train_data / 255
    test_data = test_data / 255

    print("Data loaded")

    return train_data, train_labels, test_data, test_labels


# train_data, train_labels, test_data, test_labels = load_data()
# print("Data loaded")

