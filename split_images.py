import os
import sys
 
def split_files(path, factor):
    test_path = os.path.join(path, 'test')
    imagecount = 0
    if not os.path.exists(test_path):
      os.makedirs(test_path)

    for image in os.scandir(path):
        if (os.path.isfile(image.path)):
            imagecount += 1
            if (imagecount % factor) == 0:
                os.rename(image.path, os.path.join(test_path, os.path.basename(image.path)))
                

def main(argv):
    split_files(argv[1], int(argv[2]))
    

if __name__ == "__main__":
    if len(sys.argv) >1:
        main(sys.argv)
    else:
        print ("Usage: python split_files.py PATH FACTOR")
        print ("PATH: path to the folder containing the images.")
        print ("FACTOR: one of each factor images will be moved to test folder.")
