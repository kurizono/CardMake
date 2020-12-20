from PIL import Image, ImageFont, ImageDraw
import cv2
import numpy as np
 
# 画像に文字を入れる関数
def img_add_msg(img, message):
    img = Image.fromarray(img)                          # cv2(NumPy)型の画像をPIL型に変換
    draw = ImageDraw.Draw(img)                          # 描画用のDraw関数を用意
    draw_text_width, draw_text_height = draw.textsize(message, font=font)

    # テキストを描画（位置、文章、フォント、文字色（BGR+α）を指定）
    draw.text(((img.width - draw_text_width)/2, (img.height - draw_text_height)/2), message, font=font, fill=(0, 0, 255, 0))
    img = np.array(img)                                 # PIL型の画像をcv2(NumPy)型に変換
    return img                                          # 文字入りの画像をリターン

font_path = './Font/Molot/Molot.otf'                    # フォントファイルへのパス
font_size = 200                                         # フォントサイズ
font = ImageFont.truetype(font_path, font_size) 

for num in range (101):
    img = cv2.imread('./input/patter.jpg')              # カラー画像読み込み
    message = str(num)                                  # 画像に入れる文章
    img = img_add_msg(img, message)                     # 画像に文字を入れる関数を実行
    cv2.imwrite('./output/'+ message +'.jpg', img)


# 画像を表示させる
#cv2.imshow('title', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
