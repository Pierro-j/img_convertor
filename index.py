# pip install Pillow
# pip install glop



from PIL import Image  # Python Image Library - Image Processing
import glob


im = Image.open("th.png")  #Png go there
rgb_im = im.convert('RGB')
rgb_im.save('colors.jpg') # result