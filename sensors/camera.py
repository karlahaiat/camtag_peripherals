import picamera
import os
import time

debug = False
debu= True

print("before initializing cameras")
# Initialize cameras
# Orientation is determined by looking at module with ports facing down
left_camera= picamera.PiCamera(camera_num=0,stereo_mode='none',stereo_decimate=False)
right_camera= picamera.PiCamera(camera_num=1,stereo_mode='none',stereo_decimate=False, led_pin=3)

def count_files_in_dir(path):
    path, dirs, files = next(os.walk(path))
    file_count = len(files)

    if (debu):
        print("current file count: %d" %(file_count))
        
    return int(file_count)

def record():
    
    path_front = "/home/pi/newtest/tag_data/front/"
    path_back  = "/home/pi/newtest/tag_data/back/"
    
    if not os.path.exists(path_front):
	os.makedirs(path_front)
    if not os.path.exists(path_back):
	os.makedirs(path_back)
    file_count_front = count_files_in_dir(path_front)
    file_count_back = count_files_in_dir(path_back)
    
    if (file_count_front != file_count_back):
        raise ValueError('file count in the camera dirs are NOT equal! Make sure they have the same number of files in each dir.')
    
    file_count = file_count_front
    
    for i in range(file_count + 1, 1000): #
        # get timestamp for file name
        timer = time.time()
        left_camera.start_recording(path_front + '%d-%d.h264' %(i,timer))
        right_camera.start_recording(path_back + '%d-%d.h264' %(i,timer))
        

        if (debug):
            time.sleep(5) # record for 5 seconds
            count_files_in_dir(path_front)
            count_files_in_dir(path_back)
        else:
            time.sleep(3600) #record for 1 hour
            
        left_camera.stop_recording() #stop recording so file is saved, and loop again to record another 10 minutes. The loop can run up to 1000 times unless it is paused
        right_camera.stop_recording()
        

def main():
    
    if (debug):
        # make sure the cameras are working
        #left_camera.start_preview(fullscreen=False, window=(100,20,1280,480))
        #right_camera.start_preview(fullscreen=False, window=(100,20,1280,480))
        # make sure debugging state is CLEAR
        print("In DEBUG MODE! - will only record for 5 seconds")
        time.sleep(2)
    
    record()
    
    
if __name__== "__main__":

    main()
    
