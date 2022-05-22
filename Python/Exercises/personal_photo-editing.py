import PIL.Image
import pilgram

im1 = PIL.Image.open("images\\trumpblack3.jpg")
im2 = PIL.Image.open("images\\IMG_2407.jpg")

layer1 = pilgram.css.saturate(im1, amount=1.3)
layer2 = pilgram.css.brightness(layer1, amount=1)


# pilgram.css.blending.multiply(im1, layer1).save("images\\trump.jpg")


print("Editing Done!")
