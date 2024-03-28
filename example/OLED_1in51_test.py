#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging    
import time
import traceback
import asyncio
import Display_Screens as DS
from waveshare_OLED import OLED_1in51
from PIL import Image,ImageDraw,ImageFont
logging.basicConfig(level=logging.DEBUG)

async def main():
    try:
        disp = OLED_1in51.OLED_1in51(0)
        logging.info("Disp 1 setup complete")
        disp2 = OLED_1in51.OLED_1in51(1)
        logging.info("Disp 2 setup complete")
        logging.info("Init libraries for BOTH! displays")
        disp.Init()
        
        disp.clear()
        disp2.clear()
        logging.info("Cleared Displays")
#
        #make blank images to draw on
        image1 = Image.new('1', (disp.width, disp.height), "WHITE")
        draw = ImageDraw.Draw(image1)
        image2 = Image.new('1', (disp.width, disp.height), "WHITE")
        draw2 = ImageDraw.Draw(image1)
        
        #draw OBD error Display #1
        await DS.OBDError(draw,disp, 'P1153', 'Cylinder 3 Misfire')
        #draw right arrow Display #2
        await DS.ArrowRight(draw2,disp2, '')
        
        #Clear
        disp.clear()
        disp2.clear()
         
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        OLED_1in51.config.module_exit()
        exit()
    

asyncio.run(main())