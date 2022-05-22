import cv2
import qrcode

img = qrcode.make("https://www.youtube.com/watch?v=ZhnJ1bkIWWk")
img.save("bitcoin.jpg")
img = qrcode.make("Baby yoda ate 20 biscuits today")
img.save("yoda.jpg")


d = cv2.QRCodeDetector()
# d.detectAndDecode(cv2.imread("yoda.jpg"))
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("yoda.jpg"))
print(val)
        
    #              QR CODE MAKER AND DECODER /