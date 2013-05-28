'''
Created on May 22, 2013

@author: fran


This package read the file with the interactions and the file with the preedictions and returns a list of either interactions of predictions
'''
import Data.Interaction;
import Data.Prediction;
from Data.Interaction import Interaction
from Data.Prediction import Prediction




    
def load_predictions(file_predictions):
    
    # Input format 
    # DRUG,TARGETUP,TARGETPDB,DIST_SCORE,ZSCORE,ZSCORE_GLOBAL.
    try:
        list_predictions = list()
        f=open(file_predictions)
        for line in f:
            line.rstrip()
            line = line.replace('\n', '') 
            
            l = line.split(',')
            prediction = Prediction(l[0], l[2], l[1], l[3], l[4], l[5])
            list_predictions.append(prediction)
        return list_predictions
    except Exception:
        print "File " + file_predictions + " not found or bad format \n FORMAT IS:  DRUG,TARGETUP,TARGETPDB,DIST_SCORE,ZSCORE,ZSCORE_GLOBAL "+"\n"
        return 
    
    
    
def load_interactions(file_interactions):
    
    # Input format : 
    # DRUG,DRUG_NAME,GROUP,PDB_ID,KEGG_ID,type_accion,pharmacologial_action,TYPE_RECEPTOR,TARGET_UP,PDBs_TARGET
    #  0     1         2     3     4         5           6                       7           8         9
    try:
        list_interaction = list()
        f=open(file_interactions)
        for line in f:
            line = line.replace('\n', '') 
            line.rstrip()
            l = line.split(',')
            list_pdb = l[9].split('\t')
            interaction = Interaction(l[0], l[2], l[8], list_pdb, l[3], l[5],l[6],l[7])
            list_interaction.append(interaction)
        return list_interaction
    except Exception:
        print "File " + file_interactions + " not found or bad format \n FORMAT IS:  DRUG,TARGETUP,TARGETPDB,DIST_SCORE,ZSCORE,ZSCORE_GLOBAL "+"\n"
        return

def setRanking(lista):
        
        # Sort list_predictions 
        lista.sort()
        old_distance = 0 
        ranking = 0
        for i in range(len(lista)):
            if (lista[i].distance > old_distance ):
                old_distance = lista[i].distance
                ranking=ranking +1
                lista[i].setRanking(ranking)
            else:
                lista[i].setRanking(ranking)
        return lista 
         
         