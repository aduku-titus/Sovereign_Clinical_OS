import easyocr
import cv2  # THE ENGINE
import numpy as np


class SovereignVision:
    def __init__(self):
        # gpu=False for rural resilience
        self.reader = easyocr.Reader(["en"], gpu=False)

    def preprocess_image(self, image_path):
        """
        Logic: The 'Nursing Prep' for the AI's eyes.
        We make the image Grayscale and clear.
        """
        # 1. Load the image via OpenCV
        img = cv2.imread(image_path)

        # 2. Convert to Grayscale (removes distracting colors)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 3. Apply Thresholding (makes the numbers 'Pop' against the background)
        # This turns the image into pure black and white
        _, processed_img = cv2.threshold(
            gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        return processed_img

    def scan_environment(self, image_path):
        # Step 1: Pre-process (Clean the lens)
        # In a professional workflow, we clean the image before reading
        processed_image = self.preprocess_image(image_path)

        # Step 2: Read Text from the PROCESSED image
        results = self.reader.readtext(processed_image)

        raw_data = {"numbers": [], "keywords": []}

        for bbox, text, prob in results:
            clean = text.upper().strip()
            try:
                # Logic: If it looks like a number, treat it as clinical data
                raw_data["numbers"].append(float(clean))
            except ValueError:
                # Logic: If it's text, treat it as clinical context
                keys = [
                    "SYS",
                    "DIA",
                    "BP",
                    "MMOL",
                    "SPO2",
                    "TEMP",
                    "RR",
                    "HR",
                    "ML",
                    "MMSE",
                    "BM",
                    "DAYS",
                ]
                if any(k in clean for k in keys):
                    raw_data["keywords"].append(clean)

        return raw_data
