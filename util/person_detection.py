import cv2
from numpy import ndarray


def count_people(original_img: ndarray, grayscale_img: ndarray, debug_mode: bool = False) -> int:
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    rects, weights = hog.detectMultiScale(grayscale_img, winStride=(2, 2), padding=(10, 10), scale=1.02)

    certain_counter = 0

    for i, (x, y, w, h) in enumerate(rects):
        if weights[i] > 0.7:
            certain_counter += 1
            if debug_mode: cv2.rectangle(original_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            continue

    if debug_mode:
        cv2.imshow('HOG detection', original_img)
        cv2.waitKey(0)

    return certain_counter


def resize_image(image: ndarray) -> ndarray:
    if image.shape[1] < 400:  # if image width < 400
        (height, width) = image.shape[:2]
        ratio = width / float(height)  # find the width to height ratio
        return cv2.resize(image, (400, int(height * ratio)))  # resize the image according to the width to height ratio
    else:
        return image


def person_detection(path: str, debug_mode: bool = False):
    image = cv2.imread(path)
    image = resize_image(image)
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return count_people(original_img=image, grayscale_img=img_gray, debug_mode=debug_mode)


if __name__ == "__main__":
    people = person_detection("images.jpg", debug_mode=True)
    print("found people: ", people)