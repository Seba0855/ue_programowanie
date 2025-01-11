import cv2
import pytesseract
from enum import Enum

pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"


class Mode(Enum):
    THRESH = 1
    OPENING = 2
    INVERT = 3


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


if __name__ == "__main__":
    captcha = transformToText("captcha.png", language="eng", show_result_image=False)
    print(captcha)
    mazda = transformToText(
        "mazda.png", language="eng", show_result_image=False, mode=Mode.THRESH
    )
    print(mazda)
    mcdonalds = transformToText(
        "mcdonalds.png", language="eng", show_result_image=False
    )
    print(mcdonalds)
    memorial = transformToText("memorial.png", language="eng", show_result_image=False)
    print(memorial)
    us = transformToText("us.png", language="eng", show_result_image=False)
    print(us)
