'''

Example to create some new LEMS files for running NML2 models

'''

from pyneuroml.lems import LEMSSimulation
from pyneuroml.lems import generate_lems_file_for_neuroml
import os

if __name__ == '__main__':
    
    
    
    ############################################
    ###  Create the LEMS file with helper method
    
    
    net = 'MiniScale_HippocampalNet'
    
    sim_id = 'Sim_%s'%net
    neuroml_file = "%s.net.nml"%net
    target = net
    duration=1000
    dt = 0.025
    lems_file_name = 'LEMS_%s.xml'%sim_id
    target_dir = "."
    
    generate_lems_file_for_neuroml(sim_id, 
                                   neuroml_file, 
                                   target, 
                                   duration, 
                                   dt, 
                                   lems_file_name,
                                   target_dir,
                                   include_extra_files = [],
                                   gen_plots_for_all_v = True,
                                   plot_all_segments = False,
                                   gen_plots_for_quantities = {},   #  Dict with displays vs lists of quantity paths
                                   gen_plots_for_only_populations = [],   #  List of populations, all pops if = []
                                   gen_saves_for_all_v = True,
                                   save_all_segments = False,
                                   gen_saves_for_only_populations = [],  #  List of populations, all pops if = []
                                   gen_saves_for_quantities = {},   #  Dict with file names vs lists of quantity paths
                                   gen_spike_saves_for_all_somas = True,
                                   copy_neuroml = True,
                                   seed=None)
