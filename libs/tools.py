import cv2

def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)


def mosaic_area(src, x1, y1, x2, y2, ratio=0.1):
    dst = src.copy()
    try:
        dst[y1:y2, x1:x2] = mosaic(dst[y1:y2, x1:x2], ratio)
    except:
        dst[y1:y2, x1:x2] = 0
    return dst

