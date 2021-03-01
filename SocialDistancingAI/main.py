import cv2
import os
import argparse
import queue
import threading
import time
import json
from network_model import model
from aux_functions import *
import configparser
from logger import Logger
from datetime import datetime


class VideoCapture:
  image = None

  def __init__(self, name):
    self.cap = cv2.VideoCapture(name)
    self.q = queue.Queue()
    t = threading.Thread(target=self._reader)
    t.daemon = True
    t.start()

  def __del__(self):
      #releasing camera
      self.cap.release()

  # read frames as soon as they are available, keeping only most recent one
  def _reader(self):
    while True:
      ret, frame = self.cap.read()
      if not ret:
        break
      if not self.q.empty():
        try:
          self.q.get_nowait()   # discard previous (unprocessed) frame
        except queue.Empty:
          pass
      self.q.put(frame)

  def read(self):
    return self.q.get()

class VideoOutput:
# Suppress TF warnings

    def __init__(self):
        
        os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
        self.mouse_pts = []
        self.logger = Logger("logs/")
          # Read config file or parse arguments
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
     
        if self.config['USER']['videopath']: #If the string is not empty (falsy)
            input_video = self.config['USER']['videopath']
        else:
            input_video = self.config['DEFAULT']['videopath']

        if self.config['USER']['log_interval']:
            self.log_interval = self.config['USER']['log_interval']
        else:
            self.log_interval = self.config['DEFAULT']['log_interval']

        # Define a DNN (deepl neural network) model
        self.DNN = model()
        # Get video handle
        if (self.config['USER']['is_video'] == "yes"):
            self.cap = cv2.VideoCapture(input_video)
        else:
            self.cap = VideoCapture(input_video)

        self.height = 720
        self.width = 1280
        self.fps = 20



        self.scale_w = 1.2 / 2
        self.scale_h = 4 / 2

        self.SOLID_BACK_COLOR = (41, 41, 41)
        # Setuo video writer
        #self.fourcc = cv2.VideoWriter_fourcc(*"XVID")
        #self.output_movie = cv2.VideoWriter("Pedestrian_detect.avi", self.fourcc, self.fps, (self.width, self.height))
        #self.bird_movie = cv2.VideoWriter(
        #    "Pedestrian_bird.avi", self.fourcc, self.fps, (int(self.width * self.scale_w), int(self.height * self.scale_h))
        #)

        # Initialize necessary variables
        self.frame_num = 0
        self.total_pedestrians_detected = 0
        self.total_six_feet_violations = 0
        self.delta_six_feet_violations = 0
        self.total_pairs = 0
        self.abs_six_feet_violations = 0
        self.pedestrian_per_sec = 0
        self.sh_index = 1
        self.sc_index = 1

        cv2.namedWindow("image")
        # makes it so that `get_mouse_points` is used to handle mouse events
        cv2.setMouseCallback("image", self.get_mouse_points)
        self.num_mouse_points = 0
        self.first_frame_display = True
        self.mouseX = 0
        self.mouseY = 0
        self.mouse_pts = []
        self.four_points = []


    # gets coordinates from the mouse and adds them to the `mouse_pts` list
    def get_mouse_points(self, event, x, y, flags, param):
        # Used to mark 4 points on the frame zero of the video that will be warped
        # Used to mark 2 points on the frame zero of the video that are 6 feet away
        #global mouseX, mouseY, mouse_pts
        if event == cv2.EVENT_LBUTTONDOWN:
            self.mouseX, self.mouseY = x, y
            cv2.circle(self.image, (x, y), 10, (0, 255, 255), 10)
         
            self.mouse_pts.append((x, y))
            print("Point detected")
            #print(mouse_pts)


  


    # Process each frame, until end of video
    def get_frame(self):
        self.frame_num += 1
        if (self.config['USER']['is_video'] == "yes"):
            ret, frame = self.cap.read()
        else:
            frame = self.cap.read()

        #if not ret:
        #    print("end of the video file...")
        #    break

        frame_h = frame.shape[0]
        frame_w = frame.shape[1]

        if self.frame_num == 1 and self.config['USER']['config_boot'] == "true":
            text_prompt = ["Select Bottom Left", "Select Bottom Right", "Select Top Left", "Select Top Right", "Select two points 1.5m apart", "Select two points 1.5m apart", "Well done!"]
            # Ask user to mark parallel points and two points 6 feet apart. Order bl, br, tr, tl, p1, p2
            while True:
                self.image = frame
                image_with_text = self.image.copy()
                if len(self.mouse_pts) < 7:
                    cv2.putText(image_with_text, text_prompt[len(self.mouse_pts)], (10,250), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2)
                cv2.imshow("image", image_with_text)
                cv2.waitKey(1)
                if len(self.mouse_pts) == 7:
                    print("DESTROYING!!!!!!!!!!!!!!!!!!")
                    cv2.destroyWindow("image")
                    cv2.waitKey(1)
                    break
                self.first_frame_display = False
            self.four_points = self.mouse_pts
            self.config['USER']['3d_points'] = json.dumps(self.four_points)
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)

        
        else:
            self.four_points = json.loads(self.config['USER']['3d_points'])


 
            
        global M, Minv, pts, src, d_thresh, bird_image, pedestrian_detect
        # Get perspective
        M, Minv = get_camera_perspective(frame, self.four_points[0:4])
        pts = src = np.float32(np.array([self.four_points[4:]]))
        warped_pt = cv2.perspectiveTransform(pts, M)[0]
        d_thresh = np.sqrt(
            (warped_pt[0][0] - warped_pt[1][0]) ** 2
            + (warped_pt[0][1] - warped_pt[1][1]) ** 2
        )
        bird_image = np.zeros(
            (int(frame_h * self.scale_h), int(frame_w * self.scale_w), 3), np.uint8
        )

        bird_image[:] = self.SOLID_BACK_COLOR
        pedestrian_detect = frame
        

        print("Processing frame: ", self.frame_num)
        

        # draw polygon of ROI
        pts = np.array(
            [self.four_points[0], self.four_points[1], self.four_points[3], self.four_points[2]], np.int32
        )
        cv2.polylines(frame, [pts], True, (0, 255, 255), thickness=4)

        # Detect person and bounding boxes using DNN
        pedestrian_boxes, num_pedestrians = self.DNN.detect_pedestrians(frame)

        if len(pedestrian_boxes) > 0:
            pedestrian_detect = plot_pedestrian_boxes_on_image(frame, pedestrian_boxes)
            warped_pts, bird_image = plot_points_on_bird_eye_view(
                frame, pedestrian_boxes, M, self.scale_w, self.scale_h
            )
            six_feet_violations, ten_feet_violations, pairs = plot_lines_between_nodes(
                warped_pts, bird_image, d_thresh
            )
            # plot_violation_rectangles(pedestrian_boxes, )
            self.total_pedestrians_detected += num_pedestrians
            self.total_pairs += pairs

            self.total_six_feet_violations += six_feet_violations / self.fps
            self.delta_six_feet_violations += six_feet_violations / self.fps
            self.abs_six_feet_violations += six_feet_violations
            pedestrian_per_sec, sh_index = calculate_stay_at_home_index(
                self.total_pedestrians_detected, self.frame_num, self.fps
            )

            if(self.delta_six_feet_violations >= 1):
                for i in range(int(self.delta_six_feet_violations)):
                    self.logger.write_violation(date = datetime.now().strftime("%d/%m/%Y"), time = datetime.now().strftime("%H:%M:%S"))
                self.delta_six_feet_violations = 0

        last_h = 75
        text = "Violations: " + str(int(self.total_six_feet_violations))
        pedestrian_detect, last_h = put_text(pedestrian_detect, text, text_offset_y=last_h)

        # text = "Stay-at-home Index: " + str(np.round(100 * sh_index, 1)) + "%"
        # pedestrian_detect, last_h = put_text(pedestrian_detect, text, text_offset_y=last_h)

        #if total_pairs != 0:
        #    sc_index = 1 - abs_six_feet_violations / total_pairs

        # text = "Social-distancing Index: " + str(np.round(100 * sc_index, 1)) + "%"
        # pedestrian_detect, last_h = put_text(pedestrian_detect, text, text_offset_y=last_h)

        #cv2.imshow("Street Cam", pedestrian_detect)
        #cv2.waitKey(1)
        # output_movie.write(pedestrian_detect)
        # bird_movie.write(bird_image)


        


        self.logger.write_live_counter(violations= int(self.delta_six_feet_violations) , people = self.total_pedestrians_detected, total_violations = str(int(self.total_six_feet_violations)))
            
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

