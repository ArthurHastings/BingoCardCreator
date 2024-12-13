import tkinter as tk
from tkinter import messagebox
from func import *
from PIL import Image, ImageTk
class Bingo:
    def __init__(self, root) -> None:
        self.root = root
        self.n = 0
        self.m = 0

        self.setup()

    def setup(self):
        self.setWindowSize(600, 800)
        self.frame = tk.Frame(self.root, width=300, height=200)
        # self.frame.pack_propagate(False)
        self.frame.pack()
        
        self.title = tk.Label(self.root, text="Bingo Card Creator", font=("Helvetica", 20))
        self.title.pack(pady=50)

        self.input = tk.Label(self.root, text = "Input bingo card size! (ex: 'n m')")
        self.input.pack(pady=20)

        self.dimensions_bingo_card = tk.Entry(self.root)
        self.dimensions_bingo_card.pack()

        self.start_button = tk.Button(self.root, text="Submit!", command=self.start)
        self.start_button.pack()

    def start(self):
        self.setWindowSize(600, 800)
        self.bingo_size = list(self.dimensions_bingo_card.get().split(" "))
        for i in range(len(self.bingo_size)):
            self.bingo_size[i] = int(self.bingo_size[i])

        self.n, self.m = tuple(self.bingo_size)

        if self.n * self.m > len(images_list):
            messagebox.showerror(message="The bingo card is too big!", title="Error!")
            root.quit()

        self.title.pack_forget()
        self.input.pack_forget()
        self.dimensions_bingo_card.pack_forget()
        self.start_button.pack_forget()

        self.bingo_matrix = randomizeMatrix(self.n, self.m, images_list)
        # print(type(self.bingo_matrix[0][0]))
        self.generate_button = tk.Button(self.root, text="Generate!", command=self.display_image_matrix)
        self.generate_button.pack()

    def setWindowSize(self, window_width, window_height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        center_x = int((screen_width - window_width) / 2)
        center_y = int((screen_height - window_height) / 2)

        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    def display_image_matrix(self):
        self.setWindowSize(600, 800)
        self.generate_button.pack_forget()
        root.geometry()
        if self.n == self.m == 5:
            self.bingo_title = tk.Label(self.root, text="Daniel Bingo!\nDeluxe Edition", font=("Helvetica", 30), foreground="red")
            self.bingo_title.pack(pady=30)
        else:
            self.bingo_title = tk.Label(self.root, text="Daniel Bingo!", font=("Helvetica", 30))
            self.bingo_title.pack(pady=30)

        self.matrix_frame = tk.Frame(self.root, pady=50)
        self.matrix_frame.pack()

        self.images = []
        for i in range(self.n):
            for j in range(self.m):
                self.img = Image.open(self.bingo_matrix[i][j])
                self.img = self.img.resize((100, 100))
                self.photo = ImageTk.PhotoImage(self.img)
                self.images.append(self.photo)

                self.label = tk.Label(self.matrix_frame, image=self.photo, border="2", background="black")
                self.label.grid(row=i, column=j, padx=0, pady=0)
            


if __name__ == "__main__":
    root = tk.Tk()
    app = Bingo(root)
    root.mainloop()