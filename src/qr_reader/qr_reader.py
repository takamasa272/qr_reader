from PIL import ImageGrab
from cv2 import QRCodeDetectorAruco
from numpy import ndarray, array, int64


def main():
    # grab image from clipboard
    clipImg = ImageGrab.grabclipboard()

    if clipImg is None:
        raise TypeError("No image is detected on your clipboard!")

    # decode QR code
    decoded_data = QR_decode(array(clipImg))
    if decoded_data == []:
        raise ValueError("There is no QR code!")

    # output QR code
    for i, content in enumerate(decoded_data):
        print(i, content)


def QR_decode(clipImg: ndarray) -> list:
    qrd = QRCodeDetectorAruco()
    decoded_data = []

    # decode QR
    retval, decoded_info, points, _ = qrd.detectAndDecodeMulti(clipImg)

    if retval:
        points = points.astype(int64)

        for info in decoded_info:
            if info == "":
                continue
            decoded_data.append(info)

    return decoded_data
