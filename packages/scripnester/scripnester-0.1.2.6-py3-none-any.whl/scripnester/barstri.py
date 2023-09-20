import pandas as pd
import numpy as np
class bars:
	def __init__(self,d,p):
		try:
			ohlc = {
				'Open':'first',
				'High':'max',
				'Low':'min',
				'Close':'last'
				}
				
			self.f = d.resample(p,offset='15min').apply(ohlc
			)
			self.f.dropna()
			
			self.f = self.f[
				self.f.Open.notnull() & 
				self.f.High.notnull() & 
				self.f.Low.notnull() & 
				self.f.Close.notnull()
				]
				
			self.f['avg'] = self.f.iloc[:,1:5].mean(axis=1)
			
			self.f['c'] = self.f.avg.ewm(alpha=0.5,adjust=False).mean()
			self.f['o'] = (
					(
					self.f.Open.shift(1) + self.f.c.shift(1)
					)/2
					).ewm(alpha=0.5,adjust=False).mean()

			#t = np.maximum(self.f.High,self.f.o)
			self.f['h'] = (np.maximum(
					np.maximum(
						self.f.High,
						self.f.o
						),
						self.f.c
						)
						).ewm(alpha=0.5,adjust=False).mean()

			#t = np.minimum(self.f.Low,self.f.o)
			self.f['l'] = (np.minimum(
					np.minimum(
						self.f.Low,
						self.f.o
						),
						self.f.c
						)
						).ewm(alpha=0.5,adjust=False).mean()
			#print(self.f.head(3))
						
		except:
			print('Error in init')	
		pass
	
	def getdf(self):
		return self.f
		pass	
	
	
	def getindex(self):
		return self.f.index
		pass	
		
	def getopen(self):
		return self.f.Open
		pass	
		
	def gethigh(self):
		return self.f.High
		pass	
		
	def getlow(self):
		return self.f.Low
		pass	
		
	def getclose(self):
		return self.f.Close
		pass	

	def getavg(self):
		return self.f.avg
		pass
		
	def getsma(self,N):
		return (self.f.avg.rolling(N).mean()).fillna(0)
		pass
			
	def getema(self,s,N):
		k=2/(1+N)
		return s.ewm(alpha=k,adjust=False).mean()
		pass
	
	def gettma(self,s,N):
		k=2/(1+N)
		e1 = self.getema(s,N)
		e2 = self.getema(e1,N)
		e3 = self.getema(e2,N)
		return (3*e1) - (3*e2) + e3
		pass
	pass
