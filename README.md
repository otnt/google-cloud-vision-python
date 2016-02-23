# google-cloud-vision-python
Show how to use Google's most recent Cloud Vision Platform in python.

## What is Google Cloud Vision
Checkout this [post](http://techcrunch.com/2016/02/18/google-opens-its-cloud-vision-api-to-all-developers/) by TechCrunch.

  > Google’s technology do basic things like extracting text from images, but its real power is in actually recognizing the objects in an image. This is the same technology that powers the image search in Google Photos and it can recognize anything from flowers, food and animals to local landmarks. Google says it has trained the algorithm to recognize “thousands” of different objects.
  > 
  > Image classification is probably the most interesting feature in the API, but the service can also flag inappropriate content, for example, so if you want to keep your photo-centric app PG-rated, the Cloud Vision API can help you there, too. And if you only want to see happy people in your images, the Vision API also features sentiment analysis.
  
Example test:

![Google Cloud Vision](https://tctechcrunch2011.files.wordpress.com/2016/02/cloud-vision-api-2.png)

## How to use this code

It is fairly easy.

1.First, install `requests` and `validators`.

[Requests](https://github.com/kennethreitz/requests/) is used to send `GET` and `POST` requests.

[Validators](https://github.com/kvesteri/validators/blob/master/docs/index.rst) is used to check input argument.

<br>

2.Then, run python code with first argument as your api key, and second argument as an image url or a local image name.

Example:

`python google_vision_label_detection.py <api key> https://sp.yimg.com/ib/th?id=OIP.M5c58c8b0219cd0515509976224af0b16H0&pid=15.1`

![Test Image](https://sp.yimg.com/ib/th?id=OIP.M5c58c8b0219cd0515509976224af0b16H0&pid=15.1)


Response:

```JSON
{
   "responses":[
      {
         "labelAnnotations":[
            {
               "mid":"/m/05h0n",
               "description":"nature",
               "score":0.99686354
            },
            {
               "mid":"/m/06nmjv",
               "description":"dirt road",
               "score":0.97034037
            }
         ]
      }
   ]
}
```
