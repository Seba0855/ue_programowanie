import cv2
import pytesseract
from enum import Enum

pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"


class Mode(Enum):
    THRESH = 1
    OPENING = 2
    INVERT = 3


def prepareImage(path):
    image = cv2.imread(path)
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray_scale, (3, 3), 0)
    return cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


def transformToText(
    path: str,
    language=None,
    show_result_image: bool = False,
    mode: Mode = Mode.THRESH,
    psm: int = 6,
):
    image = cv2.imread(path)
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray_scale, (3, 3), 0)
    output = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    if mode is Mode.OPENING:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        output = cv2.morphologyEx(output, cv2.MORPH_OPEN, kernel, iterations=1)
    elif mode is Mode.INVERT:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        opening = cv2.morphologyEx(output, cv2.MORPH_OPEN, kernel, iterations=1)
        output = 255 - opening

    if show_result_image:
        # Show the result
        cv2.imshow("Transformed text image (output)", output)
        cv2.waitKey()
        cv2.destroyAllWindows()

    # Text extraction
    return pytesseract.image_to_string(output, lang=language, config=f"--psm {psm}")


def preprocessing(img):
    # converted_img = cv2.medianBlur(img, 3)
    # converted_img = cv2.threshold(cv2.GaussianBlur(img, (5, 5),0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # converted_img = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    converted_img = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # converted_img = cv2.adaptiveThreshold(cv2.GaussianBlur(img,(5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # converted_img = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # converted_img = cv2.adaptiveThreshold(cv2.medianBlur(img,3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    return converted_img


if __name__ == "__main__":
    # captcha = transformToText("captcha.png", language="eng", show_result_image=True)
    # print(captcha)
    captcha_img = prepareImage("captcha.png")
    preprocessed_captcha = preprocessing(captcha_img)
    cv2.imshow("Captcha", captcha_img)
    cv2.waitKey()
    cv2.imshow("Captcha preprocessed", preprocessed_captcha)
    cv2.waitKey()