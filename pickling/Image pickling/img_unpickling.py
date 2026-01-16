import pickle

# Step 1: Load pickled image data
with open("image.pkl", "rb") as f:
    img_data = pickle.load(f)

# Step 2: Write bytes back to image file
with open("restored.jpg", "wb") as img:
    img.write(img_data)

print("Image unpickled successfully")
