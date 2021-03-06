#python examples/FCCee/flavour/generic-analysis/finalSel.py

from config.common_defaults import deffccdicts
import sys, os
import ROOT

###Input directory where the files produced at the pre-selection level are
#baseDir  = "outputs/FCCee/flavour/generic-analysis/"
baseDir  = "/eos/experiment/fcc/ee/tmp/flatntuples/Z_Zbb_Bc2TauNu/"

###Link to the dictonary that contains all the cross section informations etc...
#procDict = os.path.join(os.getenv('FCCDICTSDIR', deffccdicts), '') + "FCCee_procDict_fcc_tmp_v02.json"
#procDict ='https://fcc-physics-events.web.cern.ch/fcc-physics-events/sharedFiles/FCCee_procDict_fcc_v02.json'
procDict = {
    "p8_ee_Zbb_ecm91": {"numberOfEvents": 19830000, "sumOfWeights": 19830000, "crossSection":6645.46, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "p8_ee_Zbb_ecm91_EvtGen_Bc2TauNuTAUHADNU": {"numberOfEvents": 14789, "sumOfWeights": 14789, "crossSection": 6645.46*7.9e-5*0.0236*0.098, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "p8_ee_Zcc_ecm91": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 5215.46, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "p8_ee_Zuds_ecm91": {"numberOfEvents": 1000000, "sumOfWeights": 1000000, "crossSection": 18616.5, "kfactor": 1.0, "matchingEfficiency": 1.0}
}

process_list=['p8_ee_Zbb_ecm91_EvtGen_Bc2TauNuTAUHADNU','p8_ee_Zbb_ecm91','p8_ee_Zcc_ecm91','p8_ee_Zuds_ecm91']

define_list={
    "EVT_Ediff":"EVT_thrutshemis_emax-EVT_thrutshemis_emin",
    
    "EVT_Echarged_max":"if (EVT_thrutshemis0_echarged>EVT_thrutshemis1_echarged) return EVT_thrutshemis0_echarged; else return EVT_thrutshemis1_echarged;",
    "EVT_Echarged_min":"if (EVT_thrutshemis0_echarged>EVT_thrutshemis1_echarged) return EVT_thrutshemis1_echarged; else return EVT_thrutshemis0_echarged;",
    "EVT_Eneutral_max":"if (EVT_thrutshemis0_eneutral>EVT_thrutshemis1_eneutral) return EVT_thrutshemis0_eneutral; else return EVT_thrutshemis1_eneutral;",
    "EVT_Eneutral_min":"if (EVT_thrutshemis0_eneutral>EVT_thrutshemis1_eneutral) return EVT_thrutshemis1_eneutral; else return EVT_thrutshemis0_eneutral;",

    "EVT_Ncharged_max":"if (EVT_thrutshemis0_ncharged>EVT_thrutshemis1_ncharged) return EVT_thrutshemis0_ncharged; else return EVT_thrutshemis1_ncharged;",
    "EVT_Ncharged_min":"if (EVT_thrutshemis0_ncharged>EVT_thrutshemis1_ncharged) return EVT_thrutshemis1_ncharged; else return EVT_thrutshemis0_ncharged;",
    "EVT_Nneutral_max":"if (EVT_thrutshemis0_nneutral>EVT_thrutshemis1_nneutral) return EVT_thrutshemis0_nneutral; else return EVT_thrutshemis1_nneutral;",
    "EVT_Nneutral_min":"if (EVT_thrutshemis0_nneutral>EVT_thrutshemis1_nneutral) return EVT_thrutshemis1_nneutral; else return EVT_thrutshemis0_nneutral;",

}

###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cut_list = {"sel0":"RP_p.size()>0",
            "sel1":"EVT_thrutshemis_emax<48. && EVT_thrutshemis_emin<35. && EVT_Ediff>10.",
            "sel2":"EVT_thrutshemis_emax<45. && EVT_thrutshemis_emin<25. && EVT_Ediff>15. && EVT_Echarged_min<20. && EVT_Nneutral_min<7. && EVT_Nneutral_min<5",
            "sel3":"EVT_thrutshemis_emin<10.",
            }

###Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
variables = {

    "EVT_thrust_val":{"name":"EVT_thrust_val","title":"Event Thrust","bin":100,"xmin":0.4,"xmax":1.},
    "EVT_thrusthemis_emax":{"name":"EVT_thrutshemis_emax","title":"Hemisphere energy (max) [GeV]","bin":120,"xmin":0.,"xmax":60},
    "EVT_thrusthemis_emin":{"name":"EVT_thrutshemis_emin","title":"Hemisphere energy (min) [GeV]","bin":120,"xmin":0.,"xmax":60},
    "EVT_Ediff":{"name":"EVT_Ediff","title":"Hemisphere energy difference [GeV]","bin":120,"xmin":0.,"xmax":60},
    "EVT_Echarged_max":{"name":"EVT_Echarged_max","title":"Hemisphere charged energy (max) [GeV]","bin":120,"xmin":0.,"xmax":60},
    "EVT_Echarged_min":{"name":"EVT_Echarged_min","title":"Hemisphere charged energy (min) [GeV]","bin":120,"xmin":0.,"xmax":60},
    "EVT_Eneutral_max":{"name":"EVT_Eneutral_max","title":"Hemisphere neutral energy (max) [GeV]","bin":120,"xmin":0.,"xmax":60},
    "EVT_Eneutral_min":{"name":"EVT_Eneutral_min","title":"Hemisphere neutral energy (min) [GeV]","bin":120,"xmin":0.,"xmax":60},
    "EVT_Ncharged_max":{"name":"EVT_Ncharged_max","title":"Hemisphere charged multiplicity (max)","bin":25,"xmin":0.,"xmax":25},
    "EVT_Ncharged_min":{"name":"EVT_Ncharged_min","title":"Hemisphere charged multiplicity (min)","bin":25,"xmin":0.,"xmax":25},
    "EVT_Nneutral_max":{"name":"EVT_Nneutral_max","title":"Hemisphere neutral multiplicity (max)","bin":25,"xmin":0.,"xmax":25},
    "EVT_Nneutral_min":{"name":"EVT_Nneutral_min","title":"Hemisphere neutral multiplicity (min)","bin":25,"xmin":0.,"xmax":25}
}

###Number of CPUs to use
NUM_CPUS = 4

###This part is standard to all analyses
import config.runDataFrameFinal as rdf
#myana=rdf.runDataFrameFinal(baseDir,procDict,process_list,cut_list,variables)
myana=rdf.runDataFrameFinal(baseDir,procDict,process_list,cut_list,variables,defines=define_list)
myana.run(ncpu=NUM_CPUS, doTree=False)
