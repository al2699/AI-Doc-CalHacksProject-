import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='e73a2a89267d6264ca3975920d8228a6639ed2e6')


DIFFURL = []
DIFFURL.append('http://essentialhealth.com/wp-content/uploads/2013/02/Rash-from-plants.jpeg')
DIFFURL.append('http://www.pictureofpoisonivy.com/wp-content/uploads/2014/08/poison-ivy-on-arm.jpg')
lengthURLS = len(DIFFURL) + 1
CLASSIFIERDEL = 'PoisonIvyVsFoodPoisoning_1310090243'
PAPERCUTCLASSIFIER = 'PapercutvsNoinury_82046074'
POISONIVYCLASSIFIER = 'PoisonIvyVsFoodPoisoning_1489093693'

POSITIVEX = 'PoisonIvyRashes' + '.zip'
NEGATIVEX = 'FoodPoisoning' + '.zip'
#if json.dumps(visual_recognition.list_classifiers(), indent=2).CSRF_FAILURE_VIEW = ''

def testRecognition():
	i = 0
	print ('The Diffurl elem 0 consists of ' + DIFFURL[0] + ' and elem 1 ' + DIFFURL[1])
	while i <= lengthURLS:
		print(json.dumps(visual_recognition.classify(images_url=DIFFURL[i], threshold=0.1,
    											classifier_ids=[POISONIVYCLASSIFIER, 'default']), indent=2))
		print 'Now printing element ' + str(i) 
		i = i + 1

def createClassifier():
    with open(join(dirname(__file__), POSITIVEX),
    'rb') as poiseonIvyHands, \
      open(join(dirname(__file__), NEGATIVEX),
    'rb') as hivesHands:
      print(json.dumps(visual_recognition.create_classifier('PoisonIvyVsFoodPoisoning', poiseon_positive_examples=poiseonIvyHands, negative_examples=hivesHands), indent=2))

def checkClassifiers():
	print(json.dumps(visual_recognition.list_classifiers(), indent=2))

def deleteClassifier(CLASSIFIERID):
	print(json.dumps(visual_recognition.delete_classifier(classifier_id=CLASSIFIERID), indent=2))

def imageRecognitionBETA():
	i=0
	wResponse = json.dumps(visual_recognition.classify(images_url=DIFFURL[0], threshold=0.1,
    											classifier_ids=[POISONIVYCLASSIFIER, 'default']), indent=2)
	print type(wResponse)
	while i < 900:
		print wResponse[i]
		i = i + 1

#createClassifier()
#print 'Finshed making new classifier!'
#testRecognition()
#deleteClassifier(CLASSIFIERDEL)
#checkClassifiers()
imageRecognitionBETA()
print 'Done with script!'

"""
{
  "url": "https://gateway-a.watsonplatform.net/visual-recognition/api",
  "note": "It may take up to 5 minutes for this key to become active",
  "api_key": "e73a2a89267d6264ca3975920d8228a6639ed2e6"
}"""