'''
Created on May 22, 2013

@author: fran
'''

class Interaction:
    
    
    def __init__(self,drug,group,target_up,targets_pdb,drug_pdb,type_acction,pharmacological_action,type_receptor):
          
        self.drug = drug
        self.group = group
        self.target_up = target_up
        self.targets_pdb = targets_pdb
        self.drug_pdb = drug_pdb
        self.type_acction = type_acction
        self.pharmacological_action = pharmacological_action
        self.type_receptor = type_receptor
    
    