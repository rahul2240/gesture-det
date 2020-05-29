import os
from flask import Flask

app = Flask(__name__)


def image_to_array(data):

  d = data['data']

  outputs = {}

  if 'url' in d:
    image = url_to_image(d['url'])

  try:
    if len(image.shape)==2:
      image = cv2.merge((image,image,image))
  except:
      print('image in 2d but cant convert ot 3d')

  try:
    trans_mask = image[:,:,3] == 0
    image[trans_mask] = [255, 255, 255, 255]
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
  except:
    ans = 0

  try:
    if image.shape[0] > 100 or image.shape[1] > 100:


      image = cv2.resize(image,(512,512),interpolation=cv2.INTER_CUBIC)

      image = image.astype('float32')/255.0

      image = np.expand_dims(image, axis=0)



      ans = np.argmax(model.predict(image))
    else:
      ans = 0
  except:
    ans = 0


def video_to_image(filen):

    try:
        hdr = {
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Connection': 'keep-alive'}

        f1 = './app/data/abc.png'
        req = urllib.request.Request(filen, headers=hdr)
        req = urllib.request.urlopen(req, timeout=5)

        f = open(f1, 'wb')
        f.write(req.read())
        f.close()

        image = cv2.imread('./app/data/abc.png', cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image,(224, 224))
        os.remove('./app/data/abc.png')
    except:
        image = None

    return image


@app.route("/")
def main(): 
    video_to_image = None
    #video_to_image(received.JS.data)
    return ""

@app.route('/api')
def hello():
    image_to_array = None
    #image_to_array(response.JS.stream)
    return ""

if __name__ == "__main__":
    print("API pointed to hitAPI")
    app.run(host="0.0.0.0", port=8080)