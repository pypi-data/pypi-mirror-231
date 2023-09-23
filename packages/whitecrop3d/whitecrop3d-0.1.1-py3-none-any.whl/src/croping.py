from PIL import Image
from PIL import ImageOps
import glob


filePaths = glob.glob("png" + "/*.png") #search for all png images in the folder
destFilePaths = glob.glob("." + "/*.png") #search for all png images in the folder

for i, filePath in enumerate(filePaths):
    image=Image.open(filePath)

    image.load()
    imageSize = image.size

    # remove alpha channel
    invert_im = image.convert("RGB") 

    # invert image (so that white is 0)
    invert_im = ImageOps.invert(invert_im)
    imageBox = invert_im.getbbox()

    a= imageBox[0]-20
    b= imageBox[1]-20
    c= imageBox[2]+20
    d= imageBox[3]+20

    cropped=image.crop((a,b,c,d))

    # SCALING
    # Calculate the scaling factor
    scale_factor = min(1024/cropped.width, 768/cropped.height)

    # Resize the image
    cropped = cropped.resize((int(cropped.width * scale_factor), int(cropped.height * scale_factor)))

    # PASTE TO BACKGROUNG
    background = Image.new('RGB', (1024, 768), (255, 255, 255))

    offset = ((background.width - cropped.width) // 2, (background.height - cropped.height) // 2)
    background.paste(cropped, offset)


    print(filePath, "Size:", imageSize, "New Size:", imageBox)
    background.save('cropped/cropped_'+str(i)+'.png')








