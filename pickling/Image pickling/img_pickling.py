import pickle

# Step 1: Read image in binary mode
with open("images.jpg", "rb") as img:
    img_data = img.read()

# Step 2: Pickle the binary data
with open("image.pkl", "wb") as f:
    pickle.dump(img_data, f)

print("Image pickled successfully")
