import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"


def transformToText(path: str, language: str = "eng", show_result_image: bool = False):
    image = cv2.imread(path)
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray_scale, (3, 3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    if show_result_image:
        # Show the result
        cv2.imshow("Transformed text image", thresh)
        cv2.waitKey()

    # Text extraction
    return pytesseract.image_to_string(thresh, lang=language, config="--psm 6")


if __name__ == "__main__":
    text_from_image = transformToText("captcha.png", show_result_image=False)
    print(text_from_image)
