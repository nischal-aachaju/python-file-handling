import pickle

lst = ["ram", "shyam", "hari"]

f = open("data.pkl", "wb")   # wb = write binary
pickle.dump(lst, f)
f.close()

print("Data Pickled Successfully")
