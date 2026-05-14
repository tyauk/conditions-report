from PIL import Image, ImageDraw

#CREATE 500X300 PIXEL IMAGE WITH A BLUE BACKGROUND
img = Image.new('RGB', (500, 300), color='skyblue')

#INITIALIZE DRAWING CONTEXT
draw = ImageDraw.Draw(img)

#DRAW A YELLOW CIRCLE (SUN)
draw.ellipse((350, 50, 450, 150), fill='green', outline='orange')

#SAVE THE IMAGE
img.save('my_image.png')

#DISPLAY THE IMAGE
img.show()