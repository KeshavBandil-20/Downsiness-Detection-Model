
# 😴 Drowsiness and Yawning Detection Using Mediapipe & OpenCV

### 👨‍💻 Developed by: Keshav Bandil

---

## 📌 Overview

This project implements a real-time drowsiness and yawning detection system using **Mediapipe's FaceMesh**, **OpenCV**, and **NumPy**. It tracks facial landmarks to calculate **Eye Aspect Ratio (EAR)** and **Mouth Aspect Ratio (MAR)**, identifying drowsiness (via eye closure) and yawning (via mouth opening) in live webcam feed.

It's designed as a lightweight, practical safety tool—especially useful for drivers or heavy machinery operators—detecting fatigue before it becomes dangerous.

---

## 🎯 Objectives

- Detect when a person is drowsy based on prolonged eye closure.
- Detect yawning using facial landmarks.
- Display real-time EAR & MAR values with visual alerts.
- Run efficiently on CPU with no need for GPU acceleration.

---

## 🧠 How It Works

1. **Facial Landmark Detection**  
   Uses Mediapipe's `FaceMesh` model to detect 468 facial landmarks in real time.

2. **Eye Aspect Ratio (EAR)**  
   Measures the distance between vertical and horizontal eye landmarks.  
   - If EAR falls below a defined threshold (`0.25`) for more than 20 frames → **DROWSY**.

3. **Mouth Aspect Ratio (MAR)**  
   Measures the openness of the mouth.  
   - If MAR exceeds threshold (`0.7`) for 10 frames → **YAWNING**.

---

## 💻 Tech Stack

| Technology | Description |
|------------|-------------|
| Python | Main programming language |
| OpenCV | Real-time video capture and annotation |
| Mediapipe | FaceMesh model for facial landmark detection |
| NumPy | Vectorized math for landmark calculations |

---

## 📽️ Demo

> Press `Q` to exit the program.

![Demo](https://user-images.githubusercontent.com/your-demo-gif-or-screenshot.gif)

---

## 🧪 Output

- EAR and MAR displayed on screen.
- Alerts shown when thresholds are crossed:
  - 🔴 **DROWSY!** in red text
  - 🔵 **YAWNING!** in blue text

---

## 📦 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/drowsiness-detection
   cd drowsiness-detection
   ```

2. Install dependencies:
   ```bash
   pip install opencv-python mediapipe numpy
   ```

3. Run the script:
   ```bash
   python drowsiness_detector.py
   ```

---

## 📁 File Structure

```
📦 drowsiness-detection/
 ┣ 📜 drowsiness_detector.py
 ┗ 📄 README.md
```

---

## 🚀 Future Enhancements

- Add sound alert using `playsound` or `pyaudio`
- Extend for multi-face detection
- Export detection logs with timestamps
- Deploy on **NVIDIA Jetson Nano** or **Raspberry Pi**

---

## 🧑‍🔬 Author's Note

This project was built to explore **computer vision**, **facial landmark tracking**, and **real-time inference**. It gave me hands-on experience with EAR/MAR calculations and applying mathematical intuition to practical AI safety applications.

If you find this useful or have suggestions, feel free to connect!

---

## 🔗 Connect with Me

- 🔗 GitHub: [github.com/yourusername](https://github.com/yourusername)
- 📫 Email: your.email@example.com
- 💼 LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
