# Surveillance App
A lightweight, efficient surveillance application capable of detecting known and unknown faces, as well as objects such as weapons and people. It intelligently excludes objects or known faces displayed on screens like phones and laptops, making it highly versatile for various surveillance scenarios.

## Key Features
* *Face Recognition*: Identifies known and unknown faces with from Face database.
* *Person Detection*: Detects individuals, not limited to faces, Yolo v10 model.
* *Weapon Detection*: Detects weapons, Yolo v8 model fine-tuned on weapons dataset.
* *Smart Exclusion*: Automatically excludes faces or objects displayed on device screens (e.g., phones, laptops).
* *Video Frame Integration*: Easily integrates to process frames from videos with its lightweight model.

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Add images of known people to the known_faces folder.

3. Start webcam and process frames
```bash
python video.py
```

4. Start a streamlit application (UI for processing images):
```bash
streamlit run app.py
```

## Standalone scripts
### To Process an Image with the provided python scripts
1. Update the file name in the main function of process.py.
2. Run the script:
```bash
python process.py
```

### To Recognize Faces in an Image
1. Update the file name in the main function of recognizor.py.
2. Run the script:
```bash
python recognizor.py
```

### To Detect Person and other common objects in an Image
Update the file name in the main function of detector.py.
Run the script:
```bash
python detector.py
```

### To Detect Weapons in an Image
Update the file name in the main function of detector.py.
Run the script:
```bash
python weapon_detector.py
```

## Next Steps
### Generate Logs & Detect Anomalies
* Generate logs of detected persons, objects, activities, and store it in a DB.
* Use ML models to identify irregular patterns or anomalies.

### LLMs - Multimodal
* Utilize LLMs to monitor logs, in scenarios with limited data.
* Use multimodal LLMs (text, vision, audio) to inspect frames flagged as critical.
* Generate transcriptions of video/audio for operational insights.
