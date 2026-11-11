
from PIL import Image
import os

def create_magnified_images(ws, x0, y0, xstep, ystep, dx, dy, scale1, scale2, imgSize):
  """
  Creates magnified images of multiple points on a 2D drawing.

  Args:
    ws: The drawing data.
    x0: The starting x-coordinate.
    y0: The starting y-coordinate.
    xstep: The number of steps in the x-direction.
    ystep: The number of steps in the y-direction.
    dx: The step interval in the x-direction.
    dy: The step interval in the y-direction.
    scale1: The first magnification factor.
    scale2: The second magnification factor.
    imgSize: The size of the output image file.
  """

  html_content = """
  <html>
  <head>
    <title>Magnified Images</title>
  </head>
  <body>
    <table>
      <tr>
        <th>X</th>
        <th>Y</th>
        <th>Scale1</th>
        <th>Scale2</th>
      </tr>
  """

  for ix in range(xstep):
    for iy in range(ystep):
      x = x0 + ix * dx
      y = y0 + iy * dy

      # Create image files with different scales
      imgFile1 = f"image_{ix}_{iy}_{scale1}.png"
      imgFile2 = f"image_{ix}_{iy}_{scale2}.png"

      # Assume saveViewImage is a defined function in your environment
      # ws.saveViewImage(imgFile1, imagesize=imgSize, location=(x, y), scale=scale1)
      # ws.saveViewImage(imgFile2, imagesize=imgSize, location=(x, y), scale=scale2)
      ws.saveViewImage(imgFile1, imagesize=imgSize, location=(x, y), scale=scale1)
      ws.saveViewImage(imgFile2, imagesize=imgSize, location=(x, y), scale=scale2)

      # Add image to the HTML
      html_content += f"""
      <tr>
        <td>{x}</td>
        <td>{y}</td>
        <td><img src="{imgFile1}" width="320"></td>
        <td><img src="{imgFile2}" width="320"></td>
      </tr>
      """

  html_content += """
    </table>
  </body>
  </html>
  """

  with open("magnified_images.html", "w") as f:
    f.write(html_content)

x0 = 0
y0 = 0
xstep = 10
ystep = 10
dx = 102.4
dy = 102.4
scale1 = 2
scale2 = 4
imgSize = (1024, 1024) #Example size

class DummyWorkspace:
  def __init__(self, image_path):
    """画像ファイルを読み込むクラス"""
    self.image_path = image_path
    self.img = Image.open(image_path)

  def saveViewImage(self, output_path, imagesize, location, scale=1.0):
    """
    画像の一部を指定サイズ、中心座標、スケールで切り出して保存する関数
        
    Parameters:
    - output_path (str): 保存先のファイルパス (例: 'outFile.png')
    - imagesize (tuple): 出力する画像のサイズ (width, height)
    - location (tuple): 切り出しの中心座標 (x, y) [元画像のピクセル座標基準]
    - scale (float): 拡大・縮小倍率 (1.0 = 等倍, 2.0 = 2倍拡大, 0.5 = 0.5倍縮小)
    """
    out_w, out_h = imagesize
    x, y = location
      
    # スケールを考慮した、元画像から切り出す範囲のサイズを計算
    crop_w = out_w / scale
    crop_h = out_h / scale
        
    # 指定された中心座標 (x, y) を基準に切り出し領域の矩形 (left, upper, right, lower) を計算
    left = x - (crop_w / 2)
    upper = y - (crop_h / 2)
    right = x + (crop_w / 2)
    lower = y + (crop_h / 2)
        
    # 元画像から指定範囲をクロップ
    cropped_img = self.img.crop((left, upper, right, lower))
        
    # 指定された出力サイズ (imagesize) にリサイズ（高品質な LANCZOS フィルターを使用）
    resized_img = cropped_img.resize((out_w, out_h), Image.Resampling.LANCZOS)
        
    # 画像を保存
    resized_img.save(output_path)

ws = DummyWorkspace( "..\img\chipmunk.png" )

create_magnified_images(ws, x0, y0, xstep, ystep, dx, dy, scale1, scale2, imgSize)

# from google.colab import files
# files.download('magnified_images.html')
