from deepface.basemodels import Facenet
model = Facenet.loadModel()
target_size = (160, 160)
embedding_size = 128
from deepface.commons import functions
