# Vehicle Counter

A Python project that detects, tracks, and counts vehicles in video footage using **YOLOv8** for object detection and the **SORT** (Simple Online and Realtime Tracking) algorithm for multi-object tracking.

## Features

- Real-time vehicle detection using **YOLOv8** (`yolov8s.pt`)
- Detects and counts **cars, motorcycles, buses, trucks, and bicycles**
- Multi-object tracking with **SORT** to avoid double-counting vehicles across frames
- Counts vehicles as they cross a defined horizontal line in the video
- Visual overlay with bounding boxes, class labels, confidence scores, and a live running total (via `cvzone`)

## Project Structure

```
Vehicle-Counter/
├── Video/           # Input video(s) used for detection and counting
├── main.py          # Main application entry point (detection + counting logic)
├── sort.py          # SORT tracking algorithm (by Alex Bewley, GPL-3.0 — see LICENSE)
├── rq.txt           # Python dependencies (requirements)
├── yolov8n.pt        # YOLOv8 nano weights (fastest, least accurate)
├── yolov8s.pt        # YOLOv8 small weights (balanced speed/accuracy)
├── yolov8l.pt        # YOLOv8 large weights (most accurate, slowest)
└── README.md
```

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

## Usage

1. Place your input video inside the `Video` folder and update the path in `main.py` (currently set to `Video/vid_3.mp4`).
2. Run the script:
   ```bash
   python main.py
   ```
3. A window will open showing the video with:
   - Bounding boxes and labels around detected vehicles
   - A red counting line across the frame
   - A live "Total Vehicles" count in the top-left corner
4. Press `q` to quit.

## Demo

<!-- Add your demo video/GIF here, e.g.: -->
<!-- ![Vehicle Counter Demo](path/to/demo.gif) -->

_A short clip of the tracker detecting, tracking, and counting vehicles in real time._

## How It Works

1. **Detection** – YOLOv8 (`yolov8l.pt`) scans each video frame and detects objects. Only detections with confidence > 0.4 and belonging to the classes `motorcycle`, `car`, `truck`, `bus`, or `bicycle` are kept.
2. **Tracking** – Filtered detections are passed to a SORT tracker (`max_age=25`, `min_hits=3`, `iou_threshold=0.3`), which assigns a consistent ID to each vehicle across frames so it isn't counted more than once.
3. **Counting** – For each tracked vehicle, the center point of its bounding box is checked against a fixed horizontal line (`(200, 300)` to `(900, 300)`). When a vehicle's center crosses through the line's zone for the first time, its ID is added to the count and its bounding box is highlighted.
4. **Display** – The live video feed shows bounding boxes, class + confidence labels, the counting line, and a running "Total Vehicles" counter.

## Notes

- `main.py` uses `yolov8l.pt` by default. The `yolov8n.pt` and `yolov8s.pt` weights are also included in the repo if you want to swap for faster (nano) or more accurate (small) detection.
- The counting line coordinates (`(200, 300)` to `(900, 300)`) and confidence threshold (`0.4`) are hardcoded in `main.py` — adjust them to fit your own video's resolution and layout.

## Acknowledgments

- [SORT (Simple Online and Realtime Tracking)](https://github.com/abewley/sort) by Alex Bewley — `sort.py` in this repo is used directly from this project, unmodified, with its original license header intact.
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) for object detection.
- [cvzone](https://github.com/cvzone/cvzone) for simplified OpenCV drawing utilities (bounding boxes, text overlays).

## License

This project includes `sort.py`, which is licensed under **GPL-3.0** by its original author, Alex Bewley. Because GPL-licensed code is included, this repository as a whole is distributed under the **GPL-3.0 License** — see the [`LICENSE`](LICENSE) file for the full text.
