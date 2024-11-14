from PIL import Image
from PIL import ImageOps
import pickle
dBlocknums = Image.open("D block numbers.png")
dBlock = ImageOps.grayscale(dBlocknums)
dBlockpx = dBlock.load()
#boolean for if a certain black pixel has a vertical line of black pixels below it (making the side of a square)
isBlacklineDown = False
#boolean for if a certain black pixel has a horizontal line of black pixels beside it (making the side of a square)
isBlacklineAcross = False
#list of x vals where there are vertical lines
vertLineXvals = []
#list of y vals where there are horizontal lines
horizLineYvals = []
#list to track what row and col is equivalent to what image for final uploading
fileNames = []
for pixelY in range(0, dBlock.size[1]):
    #hardcoded pixelX value where the first black line is
    pixelX = 260
    isBlacklineAcross = True
    if dBlockpx[pixelX,pixelY] < 125:
        for i in range(100):
            # if there is a black pixel, this is not a vertical border spot
            if dBlockpx[pixelX + i,pixelY] > 125:
                isBlacklineAcross = False
                break
        if isBlacklineAcross:
            horizLineYvals.append(pixelY)
for pixelX in range(0, dBlock.size[0]):
    isBlacklineDown = True
    #where the first vertical black line is
    pixelY = horizLineYvals[0]
    if dBlockpx[pixelX,pixelY] < 125:
        for i in range(100):
            #if there is a white pixel, this is not a vertical border spot
            if dBlockpx[pixelX, pixelY+i] > 125:
                isBlacklineDown = False
                break
        if isBlacklineDown:
            vertLineXvals.append(pixelX)
#array of all the number images with rough crop
numbers = []
for i in range(len(vertLineXvals)-1):
    # print(vertLineXvals[i])
    for j in range(len(horizLineYvals)-1):
        # print(horizLineYvals[j])
        #+1 and -1 to manually cut out black borders
        number = dBlock.crop([vertLineXvals[i] + 1, horizLineYvals[j] + 1, vertLineXvals[i + 1] - 1, horizLineYvals[j + 1] - 1])
        # number.show()
        numbers.append(number)
        #add file names to a list with same indexes as numbers

        if i < 11:
            fileNames.append("page 0, row " + str(j) + " col " + str(i))
        else:
            fileNames.append("page 1, row " + str(j) + " col " + str(i-11))
# for number in numbers:
#     number.show()
#list of number images with final crop
numbersClose = []
num = 0
for i in range(7):
    del numbers[70]
    del fileNames[70]
for number in numbers:
    # initialize values for constraints on final number images
    upperY = number.size[1]
    lowerY = 0
    leftX = number.size[0]
    rightX = 0
    number_px = number.load()
    for x in range(number.size[0]):
        for y in range(number.size[1]):
            if number_px[x, y] < 100:
                if y < upperY:
                    upperY = y
                if x < leftX:
                    leftX = x
                if x > rightX:
                    rightX = x
                if y > lowerY:
                    lowerY = y
    newnumberRoughIm = number.crop([leftX, upperY, rightX, lowerY])
    newnumber20x20Im = ImageOps.contain(newnumberRoughIm, (20, 20))
    newnumberImWborder = ImageOps.expand(newnumber20x20Im, 20, 255)
    numbersClose.append(newnumberImWborder)
#var for calculating index
index = 0
numbersFinal = []
for number in numbersClose:
    # number.show()
    #find center of mass
    xSum = 0
    ySum = 0
    nPx = 0
    number_px = number.load()
    for i in range(number.size[0]):
        for j in range(number.size[1]):
            if number_px[i,j] < 100:
                xSum += i
                ySum += j
                nPx += 1
    centerOfMassX = xSum/nPx
    centerOfMassY = ySum/nPx
    numberWithCenterofMass = number.crop([centerOfMassX - 14, centerOfMassY - 14, centerOfMassX + 14, centerOfMassY + 14])
    finalImage = ImageOps.invert(numberWithCenterofMass)
    # finalImage.show()
    numbersFinal.append(finalImage)
#add to digits
for i in range(len(numbersFinal)):
    numbersFinal[i].save(f"Digits/{fileNames[i]}.png")

# for finalnumber in finalnumbers:
#     finalnumber.show()



