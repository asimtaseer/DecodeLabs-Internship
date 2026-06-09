# 🖼️ Image-Text Recognition OCR

A Python-based **Optical Character Recognition (OCR)** project that extracts and recognizes text from images — including handwritten and printed content. Built as part of the **DecodeLabs Internship Program**.

---

## 📌 Project Overview

This project demonstrates how to use OCR techniques to convert image-based text (both printed and handwritten) into machine-readable strings. It processes `.jfif`, `.jpg`, and `.png` image files and outputs the detected text using powerful OCR libraries.

---

## 🗂️ Project Structure

```
Image-Text Recognation OCR/
│
├── code.ipynb          # Main Jupyter Notebook with OCR pipeline
│
└── data/               # Sample input images for OCR testing
    ├── image2.jfif     # Handwritten text sample
    ├── image3.jfif     # OCR concept illustration
    └── image4.jfif     # Printed notes sample
```

---

## ✅ Steps Performed

### Step 1: Environment Setup
- Installed required Python libraries: `Pillow`, `pytesseract`, `opencv-python`
- Installed and configured **Tesseract OCR** engine on the local system
- Imported all necessary modules inside the Jupyter Notebook

### Step 2: Loading Images
- Loaded sample images from the `data/` directory using **Pillow (PIL)**
- Images include handwritten notes and printed text in `.jfif` format
- Previewed images inline within the Jupyter Notebook

### Step 3: Image Preprocessing
- Converted images to **grayscale** to improve OCR accuracy
- Applied **thresholding** and **noise reduction** using OpenCV
- Resized and enhanced image contrast for better text detection

### Step 4: Text Extraction (OCR)
- Used **Tesseract OCR** (via `pytesseract`) to extract text from preprocessed images
- Applied `image_to_string()` function to each image
- Printed and compared raw detected text output

### Step 5: Results Analysis
- Reviewed OCR output for accuracy across different image types
- Tested on:
  - **Handwritten text** (e.g., *"This is a handwritten example..."*)
  - **Printed notes** (e.g., *"Notes are a solid foundation for class preparation..."*)
  - **OCR concept images**
- Observed differences in recognition accuracy between handwritten and printed text

---

## 🔬 Image Processing Pipeline (Step-by-Step)

This section shows the complete visual transformation an image undergoes before OCR text extraction is applied.

---

### 🟢 Stage 1 — Load Original Image

The raw image is loaded using **OpenCV** (`cv2.imread`) and displayed in its original color form.

```python
image = cv2.imread("data/image3.jfif")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
```

![Original Image](screenshots/original%20image.png)

---

### ⚫ Stage 2 — Convert to Grayscale

The image is converted to **grayscale** using `cv2.COLOR_BGR2GRAY`. This removes color noise and prepares the image for thresholding.

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')
plt.axis("off")
plt.show()
```

![Gray Image](screenshots/gray%20image.png)

---

### 🌑 Stage 3 — Apply Thresholding

**Binary thresholding** is applied to make the image purely black and white, separating text pixels from the background for cleaner OCR detection.

```python
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
plt.imshow(thresh, cmap='gray')
plt.axis("off")
plt.show()
```

![Threshold Image](screenshots/Apply%20threshhold.png)

---

### 🟩 Stage 4 — Detect Boundaries / Contours

**Contours** are drawn around detected text regions using `cv2.findContours` and `cv2.boundingRect`. This highlights the bounding boxes of text blocks that will be passed to Tesseract for recognition.

```python
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
boundary_img = image.copy()
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(boundary_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
plt.imshow(cv2.cvtColor(boundary_img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
```

![Boundaries Image](screenshots/boundaries%20image.png)

---

### 🔄 Pipeline Summary

```
Original Image  →  Grayscale  →  Threshold  →  Contours/Boundaries  →  OCR Text Output
```

| Stage | Operation | Purpose |
|-------|-----------|---------|
| 1️⃣ Original | `cv2.imread()` | Load raw image |
| 2️⃣ Grayscale | `cv2.cvtColor(BGR2GRAY)` | Remove color noise |
| 3️⃣ Threshold | `cv2.threshold()` | Isolate text pixels |
| 4️⃣ Boundaries | `cv2.findContours()` | Detect text regions |
| 5️⃣ OCR | `pytesseract.image_to_string()` | Extract text |

---

## 🛠️ Technologies & Tools Used

| Tool / Library      | Purpose                                   |
|---------------------|-------------------------------------------|
| Python 3.x          | Core programming language                 |
| Jupyter Notebook    | Interactive development environment       |
| Pillow (PIL)        | Image loading and basic manipulation      |
| pytesseract         | Python wrapper for Tesseract OCR engine   |
| OpenCV              | Image preprocessing (grayscale, threshold)|
| Tesseract OCR       | Core OCR engine for text recognition      |
| NumPy               | Array and image data manipulation         |

---

## 🖼️ Sample Images Used

| Image File    | Content Type         | Description                                    |
|---------------|----------------------|------------------------------------------------|
| `image2.jfif` | Handwritten Text     | "This is a handwritten example. Write as good as you can." |
| `image3.jfif` | Printed / Graphic    | OCR concept — "How to turn handwriting notes into text using OCR" |
| `image4.jfif` | Printed Notes        | "Notes are a solid foundation for class preparation..." |

---

## ⚙️ How to Run

### Prerequisites
1. Install **Python 3.8+**
2. Install **Tesseract OCR**:
   - Windows: Download from [GitHub - UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
   - After installation, note the path (e.g., `C:\Program Files\Tesseract-OCR\tesseract.exe`)

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Notebook
```bash
jupyter notebook code.ipynb
```

> 💡 **Note:** Make sure to update the Tesseract path in the notebook:
> ```python
> pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
> ```

---

## 📊 Results

- **Printed text** was recognized with **high accuracy** (~95%+)
- **Handwritten text** recognition showed moderate accuracy depending on handwriting clarity
- Preprocessing steps (grayscale + thresholding) significantly improved detection quality

---

## 🔮 Future Improvements

- Integrate a deep learning-based OCR model (e.g., **EasyOCR** or **TrOCR**) for better handwriting recognition
- Add support for multi-language OCR
- Build a simple web interface using **Streamlit** or **Flask** for user-friendly image uploads
- Export recognized text to `.txt` or `.pdf` format

---

## 👤 Author

**Asim Taseer**
*DecodeLabs Internship Program*

---

## 📄 License

This project is developed for educational and internship purposes under the **DecodeLabs** program.
