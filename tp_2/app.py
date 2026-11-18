import cv2

image = cv2.imread("hiba.jpg")

if image is None:
    print("image introuvable")

else:
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("originale", image)
    cv2.imshow("niveau de gris", gris)
    cv2.waitKey(0)


    cv2.destroyAllWindows()