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



ERROR CALCULATION {BACK PROPAGATIOn}

w11     w(weight)1(first neuron)1(first weight coming out of neuron i.e weight of wire from first neuron of this layer to first neuron of next layer)
#######################################################################		
#								      				  						  #
#	  weights             errors 		  	       errors 		              #
#   (of this layer)    (next layer)	            (of this layer)	       		  #
#								                            		  		  #
#								     						    			  #
#	[w11,w12,w13]   			   			[(w11.e1)+(w12.e2)+(w13.e3)]      #
#	[w21,w22,w23]   x  [e1 , e2, e3]	=	[(w21.e1)+(w22.e2)+(w23.e3)]      #
#	[w31,w32,w33]   						[(w31.e1)+(w33.e2)+(w33.e3)]      #
#														              
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
1.0									out
	0.6 	0.45999999	0.974

		0.54

[[0.4], [0.3], [0.45999999999999996], [0.54]], [[0.562], [0.974]], []]



network=[[weigths],[biases]]

network[0]=[[weigths of layer 1],[weigths of layer 2],[weights of layer 3],[weights of layer 4]..]
network[0][0]=[[weigths coming out of first neuron],[weights coming out of second neuron]...]

network[1]=[[bias of first layer],[bias of second layer]..]
network[1][0]=[bias of first neuron,bias of second neuron,bias of third neuron]

'''
import random,math

class NeuralNetwork():

	def matrixadd(self,arr1,arr2):
		out=arr1
		if len(arr1) != len(arr2):
			print("wronge inpout for matrix add")
			exit()

		if type(arr1[0]) == type(0.5):
			for i in range(len(arr1)):
				out[i]=arr1[i]+arr2[i]
		else:
			for i in range(len(arr1)):
				for j in range(len(arr1[i])):
					out[i][j]=arr1[i][j] + arr2[i][j]

		return out

	def oneDmultiply(self,arr1,arr2,i):
		net_sum=0
		for j in range(len(arr1)):
			net_sum += arr1[j] * arr2[j][i]
		return net_sum

	def multiplys_by_num(self,num,arr):
		out=arr
		for i in arr:
			out.append(i*num)
		return num

	def multiply_by_num(self,num,arr):
		out=arr
		for i in range(len(arr)):
			for j in range(len(arr[i])):
				out[i][j]=arr[i][j]*num
		return out


	def multiply(self,arr1,arr2):

		if not len(arr1[0]) == len(arr2):
			print("\n\n\n\n invalid multiply matrises")
			sys.exit(1)

		# making a matrix with rows equal to arr1 and coloms equal to arr2 
		out=[[j for j in range(len(arr2[0])) ] for i in range(len(arr1))]


		for i in range(len(out)):
			for j in range(len(out[i])):
				out[i][j]=self.oneDmultiply( arr1[i] , arr2 , j)
		return out


	def sum_error(self,arr):
		print("this .-",arr,"-")
		out=[i for i in range(len(arr))]
		for i in range(len(arr)):
			sume=0
			for j in range(len(arr[i])):
				sume+=arr[i][j]
			out[i]=sume
		return out


	def activaton(self,x):
		return 1/(1+math.exp(-x));


	def transpose(self,array):	
		if type(array[0]) == type(0.5):
				#print("doing a single dimentional transpose")
				arr=[[array[i]] for i in range(len(array))]
				return arr
		out=[[i for i in range(len(array))] for j in range(len(array[0]))]
		for i in range(len(array)):
			for a in range(len(array[i])):
				out[a][i]=array[i][a]
		#print(out)
		return out
	 
	def back_propagate(self):
		
		network=self.network[0]
		oriex=self.expected[:]
		#print(oriex)
		expt=self.matrixadd(self.expected,self.multiply_by_num(-1,self.feed_forward()))
		error=[[] for i in range(len(network[0])+1)]
		error[-1]=expt

		#to create the output layer but without any weights in them
		network.append([[] for i in range(len(network[-1][0]))])

		for layerno in range(len(network)-1):
			Rlayerno=len(network)-2-layerno
			print("at layer-",Rlayerno,"-")
			f

		return Eweights
		

	def feed_forward(self):
		network=self.network
		inp=self.inp
		value=[[] for i in range(len(network[0])+1)]

		value[0]=inp
		for layerno in range(1,len(network[0])+1):	
			value[layerno]=self.matrixadd(self.multiply(self.transpose(network[0][layerno-1]),value[layerno-1]),self.transpose(network[1][layerno-1]))
			for i in range(len(value[layerno])):
				value[layerno][i][0]=self.activaton(value[layerno][i][0])
		
		#print(f'value is- -{value}--\n\n')
		return value[-1]

	'''
	at least thisweights work
	neuralW1=[[0.2,0.6]]
	neuralW2=[[0.2,0.6,0.5,0.3],[0.6,0.3,0.6,0.8]]
	neuralW3=[[0.2,0.6],[0.4,0.5],[0.2,0.8],[0.5,0.4]]
	neuralW4=[[0.2],[0.6]]
	'''
	def __init__(self,arr):

		self.inp=[[0.9],[0.1],[0.8]]
		self.expected=[[0.6],[0.5],[0.3]]
		
		neuralW1=[[0.9,0.2,0.1],[0.3,0.8,0.5],[0.4,0.2,0.6]]
		neuralW2=[[0.3,0.6,0.8],[0.7,0.5,0.1],[0.5,0.2,0.9]]

		bias1=[0.0,0.0,0.0]
		bias2=[0.0,0.0,0.0]
		bias3=[0.0,0.0,0.0]

		self.network=[[neuralW1,neuralW2],[bias1,bias2,bias1]]

		#uncomment to randomly initianlize the network randomly

		#self.network=[[[[random.random() for i in range(arr[i+1])] for j in range(arr[i])] for i in range(len(arr)-1)],[[random.random() for j in range(arr[i])] for i in range(1,len(arr))]]
		#print(self.network)


a=NeuralNetwork([3,3,3])
print(a.back_propagate())