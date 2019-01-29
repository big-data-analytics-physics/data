import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#
# Read in all of the other digits
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','z']
characters = ['a','b']

counter = 0
for letter in characters:
	print("letter",letter)
	dfTemp = pd.read_csv('emnist_letter_'+letter+'.csv',header=None)
	print(dfTemp.head(3))
	img = dfTemp.iloc[0]
	img = img.values.reshape(28,28)
	print(type(img))
	plt.imshow(img)
	plt.show()
