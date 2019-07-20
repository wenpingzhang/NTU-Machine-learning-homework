from PIL import Image

lena = Image.open(r"C:\Users\Administrator\Desktop\NTU-Machine-learning-homework\HW0\01-Data\lena.png")
lena_modified = Image.open(r"C:\Users\Administrator\Desktop\NTU-Machine-learning-homework\HW0\01-Data\lena_modified.png")

w, h = lena.size
for j in range(h):
    for i in range(w):
        if lena.getpixel((i, j)) == lena_modified.getpixel((i, j)):
            lena_modified.putpixel((i, j), 255)

lena_modified.show()
lena_modified.save(r"C:\Users\Administrator\Desktop\NTU-Machine-learning-homework\HW0\ans_two.png")
