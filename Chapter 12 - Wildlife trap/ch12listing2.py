# search for userMotionCodeHere. There will be 2 results, edit the second so you are passing filename to the function
userMotionCodeHere(filename)

# make sure you include filename as a parameter in the function
def userMotionCodeHere(filename):
    # we need to create an instance of the Google Vision API
    client = storage.Client()
    # instantiates a client
    client = vision.ImageAnnotatorClient()

    # loads the image into memory
    with io.open(filename, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # performs label detection on the image file
    response = client.label_detection(image=image)
    # pass the response into a variable
    labels = response.label_annotations
    
    # we have our labels, now create a string to add to the tweet message
    # for debugging - let’s see what Google thinks is in the image
    print('Labels:')
    # add labels to our tweet text
    tweetText = "Labels: "
    animalInPic = False
    for label in labels:
        print(label.description)
        tweetText = tweetText + " " + label.description
        # edit this line to change the animal you want to detect
        if "bird" in tweetText: animalInPic = true

    # set up Tweepy
    # consumer keys and access tokens, used for authorisation  
    consumer_key = ‘XXX’  
    consumer_secret = ‘XXX’  
    access_token = ‘XXX’  
    access_token_secret = ‘XXX’

    # authorisation process, using the keys and tokens  
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
    auth.set_access_token(access_token, access_token_secret)  
      
    # creation of the actual interface, using authentication  
    api = tweepy.API(auth)  

    # send the tweet with photo and message 
    photo_path = filename
    # only send tweet if it contains a desired animal
    if animalInPic:
        api.update_with_media(photo_path, status=tweetText)
    
    return