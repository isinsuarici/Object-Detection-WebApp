# Object Detection WebApp using Ultralytics and Streamlit
## Introduction 
This is a simple web application that uses YOLOv8 to detect objects in images and videos. The application is built using Streamlit and Ultralytics. The model is trained on the [Traffic and Road Dataset](https://universe.roboflow.com/usmanchaudhry622-gmail-com/traffic-and-road-signs/browse?queryText=class%3A%22Turn+right+ahead%22&pageSize=50&startingIndex=0&browseQuery=true).
## Link to the app
[Object Detection WebApp](https://trafficsignsdetection.streamlit.app/)
## Installation
1. Clone the repository
```bash
git clone
```
2. Create a virtual environment
```bash
conda create -n <env_name> python=3.9 -y
```
3. Go to the virtual environment
```bash
conda activate <env_name>
```
4. Install requirements to the virtual environment
```bash
pip install -r requirements.txt
```
5. Run the app
```bash
streamlit run main.py
```

