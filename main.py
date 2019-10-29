'''
SLIDESHOW USING OPENCV-PYTHON

It is a simple commandline based python script to make a slideshow instantly with blur effect and background
music with next, previous and pause feature.

Features-
    1. Background Music Enabled
    2. Slideshow has the following buttons-
        (1) 'a' - Previous Image
        (2) 's' - Pause the Slideshow
        (3) 'd' - Next Image
        (4) 'q' - Exit the Slideshow
    3. Adding images and background music is as simple as copy-paste in the respective directories

Note-
    1. Images must be placed at 'Images' folder
    2. Background Music file must be placed at 'Background_Music' folder

'''

import os
import sys
import cv2
from playsound import playsound

def slideshow():
    '''
    It is used to make the slideshow of the Images with next, previous, pause and exit button.
    '''

    image_names = os.listdir('Images/') # making a list of image names
    no_of_images = len(image_names)  # calculating number of images
    image_id = 0     # initially we are starting from 0th image (1st image)

    while image_id < no_of_images:  # iterating until we get at the end of the images list
        backward, forward = False, False   # they acts like a flag to store whether we are moving to next or previous image

        img = cv2.imread('Images/' + image_names[image_id]) # reading an image as per the index value

        height = 600   # height of our resized image      
        dim = (int((height/img.shape[0])*img.shape[1]), height) # manipulating width by maintaining constant ratio

        img = cv2.resize(img,dim)  # rsizing our image
        
        '''
        To add blur effect
        '''
        key, pause_key = None, None  # to store the key entered by user while slideshow
        for blur_amount in range(16,1,-2):  # getting blur values for our blur effect
            cv2.imshow('Slideshow', cv2.blur(img, (blur_amount,blur_amount) ) ) # showing blurred image
            key = cv2.waitKey(50)     # taking a key from the user with 50 ms delay
                        
            if key == ord('q'): # If 'q' pressed (EXIT)
                sys.exit(0)
            
            elif key == ord('s'): # If 's' pressed (PAUSE)
                pause_key = cv2.waitKey() 
                if pause_key == ord('q'): # If 'q' pressed (User wants to quit when slideshow is paused)
                    sys.exit(0)
                elif pause_key == ord('s'): # if user wants to resume the slideshow
                    continue
                elif pause_key == ord('a') or pause_key == ord('d'): # if user wants to go to next or previous image
                    break
        if pause_key == ord('a') and image_id != 0: # If 'a' pressed (Previous Image)
            image_id -= 1    # decrementing image_id to get previous image id
            continue
        elif pause_key == ord('d'):  # If 'd' pressed (Next Image)
            image_id += 1   # incrementing image_id to get next image id
            continue

        cv2.imshow('Slideshow', img)  # displaying clear image

        key = cv2.waitKey(1000)   # taking key from user with 1000 ms delay
        
        if key == ord('q'):  # If 'q' pressed (User wants to quit when slideshow is displaying clear image)
            sys.exit(0)
        elif key == ord('s'):  # If 's' pressed (User wants to pause when slideshow is displaying clear image)
            pause_key = cv2.waitKey()
            if pause_key == ord('q'):   # If 'q' pressed (User wants to quit when slideshow is paused)
                sys.exit(0)
            elif key == ord('a') or key == ord('d'): # if user wants to go to next or previous image
                    break
        if key == ord('a') and image_id != 0: # If 'a' pressed (Previous Image)
            image_id -= 1    # decrementing image_id to get previous image id
            continue
        elif key == ord('d'):  # If 'd' pressed (Next Image)
            image_id += 1   # incrementing image_id to get next image id
            continue
            
        image_id += 1 # If no keys are pressed, then image_id incremented for next image
    cv2.destroyAllWindows() # when work id done, closing windows

def main():

    # Music files must be placed at Birthday_Music directory.
    playsound('Background_Music/' +os.listdir('Background_Music/')[0], 0)
    
    print(''' 
                                -------------------
                                |    SLIDESHOW    |
                                -------------------
    
    ~~~~~~~~~~~~~~
    || Hot Keys ||
    ~~~~~~~~~~~~~~
    1.  'a' for previous picture
    2.  'd' for next picture
    3.  's' to pause the slideshow
    4.  'q' to exit the slideshow
    ''')

    slideshow()

if __name__ == "__main__":
    main()
