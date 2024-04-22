from PIL import Image, ImageEnhance

# Read the image
im = Image.open("sample-image.png")

# Image brightness enhancer
enhancer = ImageEnhance.Contrast(im)

factor = 1 #gives original image
im_output = enhancer.enhance(factor)
im_output.save('original-image.png')

factor = 1.5 #increase contrast
im_output = enhancer.enhance(factor)
im_output.save('more-contrast-image.png')