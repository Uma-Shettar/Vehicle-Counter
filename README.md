# Vehicle Counter

A Python project that detects, tracks, and counts vehicles in video footage using **YOLOv8** for object detection and the **SORT** (Simple Online and Realtime Tracking) algorithm for multi-object tracking.

## Features

- Real-time vehicle detection using YOLOv8 (nano, small, and large weights included)
- Multi-object tracking with SORT to avoid double-counting vehicles across frames
- Vehicle counting as objects cross a defined line/region in the video
- Works on pre-recorded video files (see the `Video` folder)

## Project Structure

```
Vehicle-Counter/
├── Video/           # Input video(s) used for detection and counting
├── main.py          # Main application entry point (detection + counting logic)
├── rq.txt           # Python dependencies (requirements)
├── yolov8n.pt        # YOLOv8 nano weights (fastest, least accurate)
├── yolov8s.pt        # YOLOv8 small weights (balanced speed/accuracy)
├── yolov8l.pt        # YOLOv8 large weights (most accurate, slowest)
└── README.md
```

> **Note:** `sort.py` is not included in this repo. It's licensed under GPL-3.0 by its original author, so you'll need to download it separately — see the setup step below.

## Requirements

- Python 3.8+
- Dependencies listed in `rq.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Uma-Shettar/Vehicle-Counter.git
   cd Vehicle-Counter
   ```

2. Install the required dependencies:
   ```bash
   pip install -r rq.txt
   ```

3. Download `sort.py` from the original [abewley/sort](https://github.com/abewley/sort) repository and place it in the root of this project:
   ```bash
   curl -o sort.py https://raw.githubusercontent.com/abewley/sort/master/sort.py
   ```
   (`sort.py` is licensed under GPL-3.0 by its author, Alex Bewley, and is not redistributed in this repo — see [Acknowledgments](#acknowledgments) below.)

## Usage

1. Place your input video inside the `Video` folder (or update the video path in `main.py` to point to your own file).
2. Choose which YOLOv8 weight file to use (`yolov8n.pt`, `yolov8s.pt`, or `yolov8l.pt`) depending on your speed/accuracy needs, and set it in `main.py`.
3. Run the script:
   ```bash
   python main.py
   ```
4. The script will process the video, detect vehicles, track them frame-to-frame with SORT, and display a running count of vehicles as they cross the counting line.

## Demo

<!-- Add your demo video/GIF here, e.g.: -->
<!-- ![Vehicle Counter Demo](path/to/demo.gif) -->

_A short clip of the tracker detecting, tracking, and counting vehicles in real time._

## How It Works

1. **Detection** – YOLOv8 scans each video frame and identifies vehicles (cars, trucks, buses, etc.).
2. **Tracking** – The SORT algorithm assigns a consistent ID to each detected vehicle across frames, so the same vehicle isn't counted multiple times.
3. **Counting** – When a tracked vehicle crosses a predefined line or region in the frame, the counter increments.

## Notes

- Larger YOLOv8 weights (`yolov8l.pt`) give better accuracy but run slower; smaller weights (`yolov8n.pt`) run faster but may miss some detections.
- Update the video source path and counting line coordinates in `main.py` to match your own footage.

## Acknowledgments

- [SORT (Simple Online and Realtime Tracking)](https://github.com/abewley/sort) by Alex Bewley — this project uses `sort.py` from the original repository (not redistributed here, see installation step 3 above).
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) for object detection.

## License

`sort.py`, used by this project, is licensed under **GPL-3.0** by its original author. If you plan to distribute this project with `sort.py` included, keep that in mind when choosing a license for your own code.
