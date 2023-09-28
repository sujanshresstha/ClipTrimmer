import os
import csv
from moviepy.video.io.VideoFileClip import VideoFileClip


base_dir = r'videos'
output_dir = r'output'


def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s


with open('annotation.csv', 'r') as sample:
    csv1 = csv.reader(sample, delimiter=',')
    next(csv1, None)  # skip the headers
    for eachline in csv1:
        if eachline[0].startswith('#'):
            print("================SKIPPED==================")
            continue
        file_name = str(eachline[0])
        input_video_path = os.path.join(base_dir, file_name)
        output_video_path = os.path.join(output_dir, file_name[:-4]+ ".mp4")
        print(output_video_path)
        start, end = map(get_sec, eachline[1:3])


        # Load video and extract subclip
        clip = VideoFileClip(input_video_path).subclip(start, end)
       
        # Write the output video file
        clip.write_videofile(output_video_path, codec='libx264')