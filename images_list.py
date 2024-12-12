import os

images_path = f"{os.path.dirname(os.path.abspath(__file__))}/BingoImages"
images_list = [os.path.join(images_path, f) for f in os.listdir(images_path) if f.endswith((".png", ".jpg"))]