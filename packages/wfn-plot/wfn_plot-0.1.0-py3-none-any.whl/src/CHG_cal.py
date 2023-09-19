'''
Descripttion: 
version: 
Author: Yang Zhong
Date: 2023-06-28 20:59:09
LastEditors: Yang Zhong
LastEditTime: 2023-06-28 21:16:34
'''

from pymatgen.core.structure import Structure
import numpy as np
from collections import OrderedDict
import numpy as np
import json
from shutil import copyfile
import os
import yaml
import argparse


au2ang = 0.5291772083

def main():
    parser = argparse.ArgumentParser(description='Wavefunction export')
    parser.add_argument('--config', default='wfn_export.yaml', type=str, metavar='N')
    args = parser.parse_args()
    
    with open(args.config, encoding='utf-8') as rstream:
        input = yaml.load(rstream, yaml.SafeLoader)
        
    cif_path = input['cif_path']
    disp = input['disp']
    save_dir = input['save_dir']
    soc_switch = input['soc_switch']
    CHG_abs_u_path = input['CHG_abs_u_path']
    CHG_abs_d_path = input['CHG_abs_d_path']
    
    crystal = Structure.from_file(cif_path)
    
    disp = np.array(disp)*au2ang
    crystal.translate_sites(indices=list(range(len(crystal))), vector = -disp, frac_coords=False)
    
    crystal.to(filename=os.path.join(save_dir, 'charge.vasp'), fmt='poscar')
    
    if soc_switch:
        f_json = open(CHG_abs_u_path)
        orb_data = json.load(f_json, object_pairs_hook=OrderedDict)
        chg_den = orb_data['CHG']
        chg_den_u = np.array(chg_den)
        
        f_json = open(CHG_abs_d_path)
        orb_data = json.load(f_json, object_pairs_hook=OrderedDict)
        chg_den = orb_data['CHG']
        chg_den_d = np.array(chg_den)
        
        chg_den = chg_den_u + chg_den_d
        chg_shape = chg_den.shape
        
        CHG_out = open(os.path.join(save_dir, 'charge.vasp'), mode='a')
        CHG_out.write(f"\n{chg_shape[0]}  {chg_shape[1]}  {chg_shape[2]}\n")
        for l in range(chg_shape[2]):
            for j in range(chg_shape[1]):
                for i in range(chg_shape[0]):
                    CHG_out.write("%f " % (chg_den[i,j,l]))
            CHG_out.write('\n')
        CHG_out.close()
    
    else:
        f_json = open(CHG_abs_u_path)
        orb_data = json.load(f_json, object_pairs_hook=OrderedDict)
        chg_den = orb_data['CHG']
        chg_den = np.array(chg_den)
        chg_shape = chg_den.shape
    
        CHG_out = open(os.path.join(save_dir, 'charge.vasp'), mode='a')
        CHG_out.write(f"\n{chg_shape[0]}  {chg_shape[1]}  {chg_shape[2]}\n")
        for l in range(chg_shape[2]):
            for j in range(chg_shape[1]):
                for i in range(chg_shape[0]):
                    CHG_out.write("%f " % (chg_den[i,j,l]))
            CHG_out.write('\n')
        CHG_out.close()

if __name__ == '__main__':
    main()