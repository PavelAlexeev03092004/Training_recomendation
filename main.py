from predict_training import predict_training
from parsing_youtube_video import get_1st_video

import time
start = time.time()
nametraining = predict_training([150], 2, 1, 2, 7, 2, 108, 3, 4, 1, 3, 2)
trainingnamevideo = []
names = [nt[1] for nt in nametraining]
videotraining = get_1st_video(names)
print([(name, video) for name, video in zip(names, videotraining)])
end = time.time()
print (end-start)