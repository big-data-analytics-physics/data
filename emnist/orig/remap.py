import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#
# Read in all of the other digits
#dfTest = pd.read_csv('emnist-letters-test.csv',header=None)
dfTest = pd.read_csv('emnist-letters-train.csv',header=None)
print(dfTest.head(5))

#dfA = dfAll[dfAll['digit']==digitSignal]
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','z']

counter = 0
for letter in characters:
	print("letter",letter)
	counter += 1
	dfTemp = dfTest[dfTest[0]==counter]
	dfNew = []
	for index, row in dfTemp.iterrows():
        # "row" is a series - the first 784 elecments being the pixel values, the last is th elabel
#		print(type(row))
		img = row[1:785]      # grab the pixel info
		img = img.values.reshape(28,28)
		img = np.swapaxes(img,0,1)
		img = img.reshape(1,784)
		dfNew.append(img.tolist()[0])
#		print(type(img))
#		plt.imshow(img)
#		plt.show()
#	print("dfNew ",dfNew)
	dfNew = pd.DataFrame(dfNew)
	name = 'emnist_letter_'+letter+'.csv'
	dfNew.to_csv(name,index=False,header=False )
