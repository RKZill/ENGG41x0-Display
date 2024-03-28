#Here lies Ryan Kelsey's artwork


import sys
import os
import time
import logging  
from PIL import Image,ImageDraw,ImageFont
logging.basicConfig(level=logging.DEBUG)
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
    
import asyncio #async calls so each display can be called seperate

font05 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
font1 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
font2 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
font3 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 39)
    
async def outline(draw):
    draw.line([(0,0),(127,0)], fill = 0)
    draw.line([(0,0),(0,63)], fill = 0)
    draw.line([(0,63),(127,63)], fill = 0)
    draw.line([(127,0),(127,63)], fill = 0)

async def leftTurn(draw, disp, distance):
    disp.clear()
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    #outline(draw)
    draw.line([(20,40),(100,40)], fill = 0) #thick line
    draw.polygon([(20,60),(20,20),(2,40)], fill=0) #head of triangle
    logging.info ("***Turn LEFT")
    draw.text((1,0), 'Turn Left '+distance, font = font1, fill = 0)
    image1 = image1.rotate(180) 
    disp.ShowImage(disp.getbuffer(image1))
    time.sleep(5)
    
async def rightTurn(draw, disp, distance):
    disp.clear()
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    #outline(draw)
    draw.line([(0,40),(100,40)], fill = 0) #thick line
    draw.polygon([(100,60),(100,20),(120,40)], fill=0) #head of triangle
    logging.info ("***Turn Right")
    draw.text((2,0), 'Turn Right '+distance, font = font1, fill = 0)
    image1 = image1.rotate(180) 
    disp.ShowImage(disp.getbuffer(image1))
    time.sleep(5)
    
async def goStraight(draw, disp, distance):
    disp.clear()
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    #outline(draw)
    draw.line([(60,30),(60,63)], fill = 0) #thick line
    draw.polygon([(40,40),(80,40),(60,20)], fill=0) #head of triangle
    logging.info ("***Turn LEFT")
    draw.text((1,0), 'Go Straight '+distance, font = font05, fill = 0)
    image1 = image1.rotate(180) 
    disp.ShowImage(disp.getbuffer(image1))
    time.sleep(5)
    
async def OBDError(draw, disp, errorCode, errorDesc):
    disp.clear()
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    
    logging.info ("***OBDERROR")
    draw.text((10,10), errorCode, font = font1, fill = 0)
    draw.text((10,40), errorDesc, font = font05, fill = 0)
    image1 = image1.rotate(180) 
    disp.ShowImage(disp.getbuffer(image1))
    time.sleep(0.01)
    
async def Speed(draw, disp, speed,unit):
    disp.clear()
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    
    logging.info ("***OBDERROR")
    draw.text((10,10), speed, font = font3, fill = 0)
    draw.text((70,20), unit, font = font2, fill = 0)

    image1 = image1.rotate(180) 
    disp.ShowImage(disp.getbuffer(image1))
    time.sleep(5)
    
async def Dist(draw, disp, num,unit):
    disp.clear()
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    
    logging.info ("***OBDERROR")
    draw.text((10,10), num, font = font3, fill = 0)
    draw.text((90,20), unit, font = font2, fill = 0)

    image1 = image1.rotate(180) 
    disp.ShowImage(disp.getbuffer(image1))
    time.sleep(5)
    
async def ArrowRight(draw, disp, direction):
    disp.clear()
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    logging.info ("***rightarrow")
    draw.line([(20,40),(20,20)], fill = 0) #thick line
    draw.line([(100,40),(20,40)], fill = 0) #thick line
    draw.line([(100,20),(20,20)], fill = 0) #thick line
    draw.line([(100,20),(100,0)], fill = 0) #thick line
    draw.line([(100,40),(100,60)], fill = 0) #thick line
    
    draw.line([(100,60),(123,30)], fill = 0) #thick line
    draw.line([(100,00),(123,30)], fill = 0) #thick line
    image1 = image1.rotate(180) 
    disp.ShowImage(disp.getbuffer(image1))
    time.sleep(5)
    
        
async def TEMP(draw, disp, direction):
    disp.clear()
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    logging.info ("***rightarrow")
    draw.line([(20,40),(20,20)], fill = 0) #thick line
    draw.line([(100,40),(20,40)], fill = 0) #thick line
    draw.line([(100,20),(20,20)], fill = 0) #thick line
    draw.line([(100,20),(100,0)], fill = 0) #thick line
    draw.line([(100,40),(100,60)], fill = 0) #thick line
    
    draw.line([(100,60),(123,30)], fill = 0) #thick line
    draw.line([(100,00),(123,30)], fill = 0) #thick line
    image1 = image1.rotate(180) 
    disp.ShowImage(disp.getbuffer(image1))
    time.sleep(1)
