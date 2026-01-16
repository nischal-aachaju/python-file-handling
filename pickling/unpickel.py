# import pickle

# f = open("data.pkl", "rb")   # rb = read binary
# data = pickle.load(f)
# f.close()

# print(data)

import pickle

lst = [1, 2, 3]
data = pickle.dumps(lst)
print(data)

