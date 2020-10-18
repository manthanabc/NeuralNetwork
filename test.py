'''
music to play : https://open.spotify.com/track/5vp1oau7i7lF9WExMWyZDl?si=-gLV4MlmTCiCIR7SmwX9ow

	*	* 		-neuralW1

	*	*		-neuralW2

*	*	*	*	-neuralW3

	*	*		-neuralW4
	
	*			-out(neuralW5)

to read = http://neuralnetworksanddeeplearning.com/chap1.html
to watch = https://www.youtube.com/watch?v=QJoa0JYaX1I

		  [5]    
	[5,6,5] * [3] = [53] = [(5x5)+(6x3)+(5x2)]
		  [2]	 


		     [y1]    
	[x1,x2,x3] * [y2] = [(x1.y1)+(x2.y2)+(x3.y3)] 
		     [y3]	 

ERROR CALCULATION 
#######################################################################		
#								      #
#	  weights       errors 		  	errors 		      #
#   (of this layer)    (next layer)	 (of this layer)	      #
#								      #
#								      #
#	[w1]   			   	[(w11.e1)+(w12.e2)+(w13.e3)]  #
#	[w2] x [e1 , e2, e3]	=	[(w21.e1)+(w22.e2)+(w23.e3)]  #
#	[w3]   				[(w31.e1)+(w33.e2)+(w33.e3)]  #
#								      #
#######################################################################

FEED FORWARD
###############################################################################		
#									      #
#	  weights        		  		value 		      #
#     (of this layer)    (this  layer)	  	 (for next  layer)	      #
#									      #
#									      #
#	[w11,w12,w13]   	[v1]	     [(v1.w11)+(v2.w21)+(v3.w31)]     #
#	[w21,w22,w23] x 	[v2]	=    [(v1.w12)+(v2.w22)+(v3.w32)]     #
#	[w31,w32,w33]   	[v3]	     [(v1.w13)+(v2.w23)+(v3.w33)]     #
#									      #
#	[w11,w21,w31]							      #
#	[w12,w22,w32]							      #
#	[w13,w23,w33]							      #
###############################################################################


		0.4

         0.2  	0.3 		0.562
 1.0 					out
	 0.6 	0.45999999	0.974

		0.54

[[0.4], [0.3], [0.45999999999999996], [0.54]], [[0.562], [0.974]], []]

'''

def oneDmultiply(arr1,arr2,i):
	net_sum=0
	for j in range(len(arr1)):
		net_sum += arr1[j] * arr2[j][i]
	return net_sum

def multiplys_by_num(num,arr):
	out=arr
	for i in arr:
		out.append(i*num)
	return num

def multiply_by_num(num,arr):
	out=arr
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			out[i][j]=arr[i][j]*num
	return out


def multiply(arr1,arr2):

	if not len(arr1[0]) == len(arr2):
		print("\n\n\n\n\ 444444 000004 4444")
		sys.exit(1)

	# making a matrix with rows equal to arr1 and coloms equal to arr2 
	out=[[j for j in range(len(arr2[0])) ] for i in range(len(arr1))]


	for i in range(len(out)):
		for j in range(len(out[i])):
			out[i][j]=oneDmultiply( arr1[i] , arr2 , j)
	return out


def sum_error(arr):
	print("this .-",arr,"-")
	out=[i for i in range(len(arr))]
	for i in range(len(arr)):
		sume=0
		for j in range(len(arr[i])):
			sume+=arr[i][j]
		out[i]=sume
	return out


def transpose(array):	
	if type(array[0]) == type(0.5):
			print("ok fdoinf somrthiomn else")
			arr=[[array[i]] for i in range(len(array))]
			return arr
	out=[[i for i in range(len(array))] for j in range(len(array[0]))]
	for i in range(len(array)):
		for a in range(len(array[i])):
			out[a][i]=array[i][a]
	#print(out)
	return out
 
def feed_forward(network,inp):
	value=[[] for i in range(len(network)+1)]

	value[0]=inp
	print(value[0][0],network[0])
	value[1]=multiply_by_num(value[0][0],network[0])

	for layerno in range(2,len(network)+1):
		print("\nnetwork -",network)
		print("\nweights used -",network[layerno-1])
		print("\nvlaue -",value)
		print("\n multi =",transpose(network[layerno-1]),' and ',transpose(value[layerno-1]),"\n")
		if layerno < 3:
			value[layerno]=multiply(transpose(network[layerno-1]),transpose(value[layerno-1]))
		else:		
			value[layerno]=multiply(transpose(network[layerno-1]),value[layerno-1])
		print("\n",value)



neuralW1=[[0.2,0.6]]
neuralW2=[[0.2,0.6,0.5,0.3],[0.6,0.3,0.6,0.8]]
neuralW3=[[0.2,0.6],[0.4,0.5],[0.2,0.8],[0.5,0.4]]
neuralW4=[[0.2],[0.6]]

network=[neuralW1,neuralW2,neuralW3,neuralW4]

def main():
	feed_forward(network,[1.0])

if __name__=="__main__":
	main()
