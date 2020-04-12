import cv2
import os, sys
import time
import shutil


def ppdt():
    root_path = '/home/trigen/practice'
    files_folder = os.path.join(root_path, 'files')
    archives = os.path.join(root_path, 'archives')

    files = set(os.listdir(files_folder))
    move_file = ''

    while True:

        if not files:
            os.system('spd-say "Files folder is empty"')
            break

        os.system('spd-say "Enter "y" to continue and "n" to cancel"')
        to_start = input(f'Enter "y" to continue and "n" to cancel\n')
        if to_start != 'y':
            break
        
        move_file = os.path.join(files_folder, files.pop())
        os.system('spd-say "Write down action, mood, no. of characters etc."')

        # read img
        img = cv2.imread(move_file)
        os.system('spd-say "Image will open in 5 seconds and will be opened for 1 minute"')
        time.sleep(5)

        # open img
        cv2.imshow('PPDT', img)
        # Keep open
        cv2.waitKey(60000)
        cv2.destroyAllWindows()

        os.system('spd-say "You have got 1 minute to create a story in your mind"')
        time.sleep(60)

        os.system('spd-say "Start"')
        time.sleep(240)
        os.system('spd-say "Stop Stop Stop Stop"')

        shutil.move(move_file, archives)
        print('file moved to archives')

    os.system('spd-say "Bye-Bye"')

if __name__ == '__main__':
    ppdt()
