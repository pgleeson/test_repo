import neuroml

from pyneuroml import pynml
import random

nml_file = "HippocampalNet.net.nml"
nml_doc = pynml.read_neuroml2_file(nml_file)

width =1500
depth = 500

h_so = 100
h_sp = 100
h_lm = 200


for pop in nml_doc.networks[0].populations:
    
    print("Handling population %s with %s cells"%(pop.id,len(pop.instances)))
    for instance in pop.instances:
        loc = instance.location
        old = str(loc) 
        loc.x = width*random.random()
        loc.y = (h_so+h_sp+h_lm)*random.random()
        if pop.id == 'pop_poolosyn':
            loc.y = h_so + h_sp*random.random()
        loc.z = depth*random.random()
        print("    Changed %s to %s"%(old,loc))
        
        
net_file = 'Mod_%s'%(nml_file)
neuroml.writers.NeuroMLWriter.write(nml_doc, net_file)

print("Written network to: %s"%(net_file))
        