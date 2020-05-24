import cv2
#
# def get_position(event, x, y, flags, param):  # definiowanie parametrów
#     if event== cv2.EVENT_LBUTTONDBLCLK:         # polecenie
#         print(f"x={x}, y={y}")                  # wyprintowanie pozycji
#
#
# def draw_circle(event, x, y, flags, param):  # definiowanie parametrów
#     if event== cv2.EVENT_LBUTTONDBLCLK:         # polecenie
#         cv2.circle(
#             image=image,
#             center=(x,y),
#             color=(0,255,0),
#             thickness=2,
#             radius=50,
#
#         )                 # wyprintowanie pozycj
#
#
# image = cv2.imread(r"D:\Programy\pyCharm\compiuter-vision-course1\01_basics\assets\tesla.jpg")
#
# cv2.namedWindow("image")
# cv2.setMouseCallback("image", draw_circle)
#
# while True:
#     cv2.imshow("image", image)
#     if cv2.waitKey(1) == 27:
#         break

def get_position(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(f'x={x}, y={y}')


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(
            img=img,
            center=(x, y),
            radius=50,
            color=(0, 255, 0),
            thickness= 2
        )


img = cv2.imread(r'D:\Programy\pyCharm\compiuter-vision-course1\01_basics\assets\tesla.jpg')

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) == 27:
        break
