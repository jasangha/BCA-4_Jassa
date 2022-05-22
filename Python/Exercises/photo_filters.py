import PIL.Image
import pilgram

im1 = PIL.Image.open("images\\trumpblack3.jpg")
im2 = PIL.Image.open("images\\IMG_2407.jpg")

# pilgram.css.saturate(im1, amount=1.3).save("images\\saturate.jpg")
# pilgram.css.brightness(im1, amount=1).save("images\\brightness.jpg")
# pilgram.css.grayscale(im1, amount=.5).save("images\\grayscale.jpg")
# pilgram.css.hue_rotate(im1).save("images\\hue_rotate.jpg")
# pilgram.css.sepia(im1, amount=1).save("images\\sepia.jpg")


pilgram.lofi(im1).save("images\\lofi.jpg")
pilgram.inkwell(im1).save("images\\inkwell.jpg")
pilgram.kelvin(im1).save("images\\kelvin.jpg")
pilgram._1977(im1).save("images\\1977.jpg")
pilgram.xpro2(im1).save("images\\xpro2.jpg")
pilgram.willow(im1).save("images\\willow.jpg")
pilgram.walden(im1).save("images\\walden.jpg")
pilgram.valencia(im1).save("images\\valecia")
pilgram.aden(im1).save("images\\aden.jpg")
pilgram.brannan(im1).save("images\\brannan.jpg")


# pilgram.css.blending.color(im1, im2).save("images\\color.jpg")
# pilgram.css.blending.darken(im1, im2).save("images\\darken.jpg")
# pilgram.css.blending.lighten(im1, im2).save("images\\lighten.jpg")
# pilgram.css.blending.difference(im1, im2).save("images\\difference.jpg")
# pilgram.css.blending.multiply(im1, im2).save("images\\multiply.jpg")


print("Editing Done!")
