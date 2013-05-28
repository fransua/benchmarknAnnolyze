'''
Created on May 22, 2013

@author: fran
'''

class Prediction:
     
    def __init__(self,drug,target_up,target_pdb,distance,zscore_local,zscore_global,ranking=-1):
          
        self.drug = drug
        self.target_up = target_up
        self.target_pdb = target_pdb
        self.distance = distance
        self.zscore_local = zscore_local
        self.zscore_global = zscore_global
        self.ranking = -1
        
    def setRanking(self,ranking):
        
        self.ranking=ranking
    
    def __cmp__( self, other ) :
        
        if self.distance < other.distance :
            rst = -1
        elif self.distance > other.distance :
            rst = 1
        else :
            
            if self.zscore_local < other.zscore_local: 
                rst = -1 
            elif self.zscore_local > other.zscore_local:
                rst = 1
            else:
                rst = 0
            

        return rst
    def __str__(self):
     return self.drug +","+ self.target_up +","+ self.target_pdb +","+self.distance +"," + self.zscore_global +"," + self.zscore_local + "\n"
