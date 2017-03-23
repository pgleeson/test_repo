'''

Example to create some new LEMS files for running NML2 models

'''

from pyneuroml.lems import generate_lems_file_for_neuroml
import os

if __name__ == '__main__':
    
    
    
    ############################################
    ###  Create the LEMS file with helper method
    
    
    net = 'HippocampalNet'
    net = 'LargeScale_HippocampalNet'
    
    sim_id = 'Sim_%s'%net
    neuroml_file = "%s.net.nml"%net
    target = net
    duration=100
    dt = 0.025
    lems_file_name = 'LEMS_%s.xml'%sim_id
    target_dir = "."
    
    pops_with_morphlogies = ["pop_ngf","pop_bistratified","pop_sca","pop_olm","pop_poolosyn","pop_pvbasket","pop_cck","pop_axoaxonic","pop_ivy"]
    
    generate_lems_file_for_neuroml(sim_id, 
                                   neuroml_file, 
                                   target, 
                                   duration, 
                                   dt, 
                                   lems_file_name,
                                   target_dir,
                                   include_extra_files = [],
                                   gen_plots_for_all_v = False,
                                   plot_all_segments = False,
                                   gen_plots_for_only_populations = pops_with_morphlogies,   #  List of populations, all pops if = []
                                   gen_saves_for_all_v = False,
                                   save_all_segments = False,
                                   gen_saves_for_only_populations = pops_with_morphlogies,  #  List of populations, all pops if = []
                                   gen_saves_for_quantities = {},   #  Dict with file names vs lists of quantity paths
                                   copy_neuroml = True,
                                   seed=None)
