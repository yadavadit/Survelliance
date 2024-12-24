# Surveillance App
A lightweight, efficient surveillance application capable of detecting known and unknown faces, as well as objects such as weapons and people. It intelligently excludes objects or known faces displayed on screens like phones and laptops, making it highly versatile for various surveillance scenarios.

## Key Features
Face Detection: Identifies known and unknown faces with high accuracy.
Object Detection: Detects objects, including weapons and individuals, not limited to faces.
Smart Exclusion: Automatically excludes faces or objects displayed on device screens (e.g., phones, laptops).
Video Frame Integration: Easily integrates to process frames from videos with its lightweight model.

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Add images of known people to the known_faces folder.
3. Start the application:
```bash
streamlit run app.py
```

## Standalone scripts
### To Process an Image with the provided python scripts
1. Update the file name in the main function of process.py.
2. Run the script:
```bash
python recognizor.py
```

### To Recognize Faces in an Image
1. Update the file name in the main function of recognizor.py.
2. Run the script:
```bash
python recognizor.py
```

### To Detect Objects in an Image
Update the file name in the main function of detector.py.
Run the script:
```bash
python detector.py
```
