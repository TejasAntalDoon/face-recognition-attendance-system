# Face Recognition Attendance System

A real-time face recognition attendance system built with Python that automatically marks attendance when recognized faces are detected through a webcam feed.

## Features

- **Real-time Face Recognition**: Uses webcam to detect and recognize faces in real-time
- **Automatic Attendance Marking**: Automatically logs attendance with timestamps
- **Duplicate Prevention**: Prevents multiple entries within a configurable time interval
- **User-friendly GUI**: Clean interface with live video feed and attendance log
- **CSV Export**: Save attendance records to CSV file
- **Multiple Face Support**: Can recognize and track multiple individuals

## Screenshots

![System Interface](screenshots/interface.png)
*Main interface showing live video feed and attendance log*

## Requirements

- Python 3.7+
- Jupyter Notebook or JupyterLab
- Webcam/Camera
- Windows/Linux/MacOS

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/TejasAntalDoon/face-recognition-attendance-system.git
   cd face-recognition-attendance-system
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install additional dependencies**
   
   For Windows:
   ```bash
   pip install cmake
   pip install dlib
   ```
   
   For Linux/Ubuntu:
   ```bash
   sudo apt-get install cmake
   sudo apt-get install python3-dev
   pip install dlib
   ```
   
   For MacOS:
   ```bash
   brew install cmake
   pip install dlib
   ```

4. **Install Jupyter Notebook** (if not already installed)
   ```bash
   pip install jupyter notebook
   ```
   
   Or for JupyterLab:
   ```bash
   pip install jupyterlab
   ```

## Dataset Setup

1. **Create the dataset folder structure**
   ```
   dataset/
   ├── person1_name/
   │   ├── image1.jpg
   │   ├── image2.jpg
   │   └── ...
   ├── person2_name/
   │   ├── image1.jpg
   │   ├── image2.jpg
   │   └── ...
   └── ...
   ```

2. **Add face images**
   - Create a folder for each person using their name
   - Add 3-5 clear face images per person
   - Ensure images are well-lit and face is clearly visible
   - Supported formats: JPG, PNG, JPEG

## Usage

### Running in Jupyter Notebook

1. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```
   
   Or for JupyterLab:
   ```bash
   jupyter lab
   ```

2. **Open the notebook file**
   - Navigate to the project directory
   - Open `attendance_system.ipynb` in Jupyter

3. **Run all cells** or execute cells individually

### Running as Python Script

1. **Run the application**
   ```bash
   python attendance_system.py
   ```

### Using the system
   - Click "Start Webcam" to begin face recognition
   - The system will automatically detect and recognize faces
   - Attendance will be marked when a known face is detected
   - View real-time attendance log in the right panel
   - Click "Save Attendance" to export data to CSV

3. **Configuration**
   - Modify `TIME_INTERVAL` variable to change the minimum time between attendance marks for the same person
   - Adjust face recognition tolerance by changing the threshold value (default: 0.5)

## File Structure

```
face-recognition-attendance/
├── attendance_system.py      # Main application file
├── attendance_system.ipynb   # Jupyter notebook version
├── dataset/                  # Face images dataset
│   └── [person_folders]/
├── screenshots/              # Interface screenshots
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── LICENSE                  # License file
└── .gitignore              # Git ignore file
```

## Configuration Options

You can modify these variables in `attendance_system.py`:

- `TIME_INTERVAL`: Minimum minutes between attendance marks (default: 1)
- Face recognition tolerance: Adjust the threshold value (default: 0.5)
- Window size: Modify geometry in `root.geometry("900x600")`

## Troubleshooting

### Common Issues

1. **"No module named 'face_recognition'"**
   - Install: `pip install face_recognition`

2. **"Error processing image"**
   - Ensure image files are valid and readable
   - Check file permissions

3. **Webcam not working**
   - Check camera permissions
   - Try different camera index: `cv2.VideoCapture(1)` instead of `cv2.VideoCapture(0)`
   - In Jupyter: Restart the kernel if camera access issues persist

4. **Jupyter Notebook specific issues**
   - If GUI doesn't appear: Make sure you're using `%matplotlib inline` or `%matplotlib widget`
   - Kernel crashes: Restart the kernel and run cells again
   - Camera permission in Jupyter: Allow camera access in browser settings

5. **Poor recognition accuracy**
   - Add more training images per person
   - Ensure good lighting conditions
   - Adjust recognition tolerance

### Performance Tips

- Use well-lit images for training
- Maintain consistent lighting during recognition
- Keep the dataset organized with clear folder names
- For Jupyter users: Close the webcam properly using the stop button to avoid camera lock issues
- Restart the application after adding new faces
- In Jupyter: Use "Restart & Run All" when making changes to the code

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [face_recognition](https://github.com/ageitgey/face_recognition) library by Adam Geitgey
- [OpenCV](https://opencv.org/) for computer vision capabilities
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for GUI framework

## Contact

Tejasvi Singh Antal - tejas1379antal@gmail.com

Project Link: [https://github.com/TejasAntalDoon/face-recognition-attendance-system](https://github.com/TejasAntalDoon/face-recognition-attendance-system)

---

⭐ Star this repository if you found it helpful!
