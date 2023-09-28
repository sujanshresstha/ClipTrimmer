# ClipTrimmer
This script extracts specified segments from video files based on start and end times provided in a CSV file.

## Dependencies

The script requires the following Python libraries:

- `os`
- `csv`
- `moviepy`

You can install these with pip:
```
pip install moviepy
```

## Usage

1. Place your video files in a directory named `videos` in the same directory as the script.
2. Create a CSV file named `annotation.csv` in the same directory as the script. The CSV file should have the following format:

filename,start_time,end_time
video1.mp4,00:01:00,00:02:00
video2.mp4,00:05:00,00:06:00
…

Each row represents a video file and the start and end times for the segment to extract. The times should be in the format `HH:MM:SS`.

3. Run the script:

```
python main.py
```


The script will create a directory named `output` and place the extracted video segments there. The output files will have the same name as the input files, but with the `.mp4` extension.

## Note

If a row in the CSV file starts with `#`, the script will skip that row.
