import sys
import base64
import requests
import validators
import json

def main(token, image):
    '''
    Google just public their cloud vision platform, which provides functions
    including label detection, landmark detection, facial detection, OCR etc.
    This program shows how to use this platform to get landmark detection result

    User need to pass two arguments, first is api key, which you could get
    from google's cloud platform, second is an image url or an local image name
    '''

    #if passing an url, then get image data from url
    if validators.url(image):
        image_content = requests.get(image)
        if image_content.status_code is not 200:
            print json.dumps(image_content.text)
            return
        image_content = base64.b64encode(image_content.content)
        #otherwise, try to get file from local file
    else:
        with open(image, 'rb') as image:
            image_content = base64.b64encode(image.read())
      
    #send data to google cloud vision and get request
    post_data =\
        '{\
            "requests": [\
                {\
                    "image":{"content": "%s" },\
                    "features": [{"type": "LABEL_DETECTION","maxResults": 2}]\
             }\
         ]\
     }' % image_content

    data = requests.post(\
            'https://vision.googleapis.com/v1/images:annotate?key=%s' % token,\
            data = post_data,\
            headers = {'Content-Type': 'application/json'})
    print json.dumps(data.text)

if __name__ == '__main__':
    if len(sys.argv) is not 3:
        print "Usage: python <program name> <api_key> \
                <image url or local image name>"
        sys.exit(1)
    token = sys.argv[1]
    image = sys.argv[2]
    main(token, image)
