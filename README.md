# 💪 AI Fitness Trainer & Rep Counter

A real-time AI-powered fitness trainer and rep counter using **MediaPipe Pose** and **JavaScript**. This project analyzes your **bicep curls** via webcam and provides **live feedback**, **rep count**, and **pose status**.

---

## 🌐 Live Demo

> Coming soon (or host via GitHub Pages and insert your link here)

---

## 📸 Preview

![AI Fitness Trainer Preview](https://your-demo-image-or-gif-url.com)

---

## 🚀 Features

- 🧠 AI-based body pose tracking with MediaPipe
- 🎥 Real-time webcam feed with overlaid pose landmarks
- 💪 Automatic **bicep curl** rep counting
- 📢 Real-time feedback and exercise stage display
- 🌈 Clean, responsive UI built with TailwindCSS

---

## 🛠️ Tech Stack

- **HTML**, **CSS**, **JavaScript**
- [TailwindCSS](https://tailwindcss.com/)
- [MediaPipe Pose](https://google.github.io/mediapipe/solutions/pose)
- [Camera Utils](https://google.github.io/mediapipe/solutions/camera_utils.html)

---

## 🧠 How It Works

1. **MediaPipe** detects landmarks of the body from the webcam.
2. Calculates the **elbow joint angle** using:
   - `shoulder → elbow → wrist`
3. Logic:
   - If angle > 160° → **"down" position**
   - If angle < 40° and previous state was down → count **1 rep**
4. UI updates the **rep count**, **status**, and **feedback**.

---

