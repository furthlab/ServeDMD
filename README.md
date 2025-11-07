# 🧙‍♂️ ServeDMD: Serve the Dungeon Master’s Device

**ServeDMD** is a Python-based control framework for **closed-loop photolithography on a microscope**.  
It combines real-time **Digital Mirror Device (DMD)** control with **deep learning–based image segmentation**, enabling adaptive pattern projection and precise light-driven microfabrication.

- 🖥️ **Server code** → runs on a **Raspberry Pi** connected to the **DMD hardware**.  `raspberrypi_server.py`
- 💻 **Client code** → runs on a **control workstation** (handling microscope imaging, segmentation, and feedback). `microscope_client.py` 

In short — it’s the **Dungeon Master** for your light patterns.

---

## ✨ Overview

ServeDMD orchestrates a feedback loop between imaging, segmentation, and projection:

1. **Capture** — Acquire an image from the microscope.  
2. **Segment** — Run deep learning segmentation (e.g., with PyTorch or TensorFlow) to identify regions of interest.  
3. **Project** — Generate and send a photolithography pattern to the DMD.  
4. **Evaluate** — Capture a new image and iterate — until the desired pattern is achieved.

This closed-loop control enables **adaptive exposure**, **self-correcting lithography**, and **high-precision optical patterning**.

---

## ⚙️ Features

- 🧠 **Closed-loop control** between imaging, segmentation, and projection.  
- 💡 **Real-time DMD pattern generation** for adaptive photolithography.  
- 🧩 **Modular architecture** — integrate any microscope camera, DMD, or segmentation model.  
- 🤖 **Deep learning segmentation** using PyTorch or TensorFlow backends.  
- 🔬 **Microscope integration** via Ethernet or serial device communication.  
- 🧙 **Dungeon Master mode** — because your photons deserve a commanding presence.

---

## 🧰 Installation

### Requirements
- Python 3.8+
- `opencv-python`
- `numpy`
- `torch` or `tensorflow` (depending on segmentation backend)
- `matplotlib` (for visualization)

Install dependencies:
```bash
pip install -r requirements.txt
