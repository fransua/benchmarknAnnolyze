'''
Created on May 22, 2013

@author: fran
This script reads the predictions output by nAnnolyze for a set of drugs on a set of PDBS, search the UP of this PDB and after that it print different scores : 

IDEA 1 : BENCHMARKING 

FOR EACH REACHEABLE INTERACTION:
Get the ranking of the ONE? of the PDS. 
 
--> % oF RAKING FOUND IN TOP 1. 
--> % OF RANKING FOUND In TOP 3.
--> % OF RANKING FOUND IN TOP 15. 
'''
import getopt, sys, os
import Utils.utils;
from Utils.utils import load_interactions, load_predictions, setRanking

class benchmarking1:
    
    
    def __init__(self,file_interactions,file_predictions):
        self.list_interactions = load_interactions(file_interactions)
        self.list_predictions = load_predictions(file_predictions)
        self.map_sorted_predictions = self.setRankingMap()
      
    
    def setRankingMap(self):
        # this method return a map where the key is the drug and they value is a SORTED LIST OF PREDICTIONS 
        
        map_pred = {}
        for predi in self.list_predictions:
            if not(predi.drug in map_pred):
                # Non defined
                map_pred[predi.drug] = list()
            map_pred[predi.drug].append(predi)
           
        for drug in map_pred.keys():
            map_pred[drug]=setRanking(map_pred[drug])
        
        return map_pred
    
    
    
    
    
    
       
            
    def getTopPredictions(self,n,lista):
          
        # Return the top N predictions
        list_topN = list()
        for p in lista:
            
            if p.ranking <= n:  
                list_topN.append(p)
        
            else:
                break;
        return list_topN
    
    def getPercetangeInteractionsTopN(self,n):
    # Returns the percentage of interactions found in top N.
    # For each interactions in the query file, adds 1 if found ANY of the PDBs in top N, 0 otherwise
    # Return found / total
    
        total = len(self.list_interactions)
        
        found = 0
        eqv = 0
        for interaction in self.list_interactions:
            list_pdbs = interaction.targets_pdb
            drug = interaction.drug
            if drug in self.map_sorted_predictions:
                list_topN = self.getTopPredictions(n,self.map_sorted_predictions[drug])
                for pdb in list_pdbs:
                    for pre in list_topN:
                        eqv = 0
                        if (pdb == pre.target_pdb[0:4].upper()):
                            found=found+1
                            eqv = 1
                            break
                    
                    if (eqv == 1): # Only search 1 match :?
                        break;
        return ((found / float(total) ) * 100) # Ya veremos como lo imprimimmos
    def getRankingPosition(self):
    # For each query interaction return the raking position where it can be found 
    
        total = len(self.list_interactions)
        list_positions = list()
        #print total
        for i in range(total):
            list_positions.insert(i,-1)
        position = 0
        eqv = 0
        for interaction in self.list_interactions:
            
            list_pdbs = interaction.targets_pdb
            drug = interaction.drug
            if drug in self.map_sorted_predictions:
                list_topN = self.map_sorted_predictions[drug]
                for pdb in list_pdbs:
                    
                    for pre in list_topN:
                        
                        eqv = 0
                        if (pdb == pre.target_pdb[0:4].upper()):
                            list_positions[position]=str(pre.ranking)+" "+pre.drug+" "+pre.target_pdb+" "+pre.distance+" "+pre.zscore_local+" "+pre.zscore_global
                            
                            eqv = 1
                            break
                        
                    if (eqv == 1): # Only search 1 match :?
                        break;
            position= position +1
        return list_positions # Ya veremos como lo imprimimmos
 

def usage():
    
    print """Usage: benchmarking1 [options]
    \t\t--predictions_file file : file with the predictions
    \t\t--interactions_file file : file with the interactions
    \n
         
     """
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "", ["predictions_file=","interactions_file="])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    interactions_file = ""
    predictions_file = ""
    for o, a in opts:
        #print "%s = %s" % (str(o), str(a))
        if o == "--predictions_file":
            predictions_file = a
        elif o == "--interactions_file":
            interactions_file = a
    if(interactions_file == "" or predictions_file == ""):
        usage()
        sys.exit(2)
    bench = benchmarking1(interactions_file,predictions_file)
    print bench.getPercetangeInteractionsTopN(150)
    print bench.getRankingPosition()
    
if __name__ == "__main__":
    main(sys.argv[1:])      