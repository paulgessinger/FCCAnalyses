import os, sys
import copy
import heppy.framework.config as cfg
import logging

# next 2 lines necessary to deal with reimports from ipython
logging.shutdown()
reload(logging)
logging.basicConfig(level=logging.WARNING)

sys.path.append('/afs/cern.ch/work/h/helsens/public/FCCDicts/')

comp = cfg.Component(
    'example',
     files = ["root://eospublic.cern.ch//eos/fcc/hh/generation/DelphesEvents/fcc_v01/pp_h012j_5f_hmumu/events0.root"]
)

from heppySampleList import *

'''selectedComponents = [
                      pp_h012j_5f_HT_0_100_hmumu,
                      pp_h012j_5f_HT_100_400_hmumu,
                      pp_h012j_5f_HT_400_1000_hmumu,
                      pp_h012j_5f_HT_1000_1900_hmumu,
                      pp_h012j_5f_HT_1900_4400_hmumu,
                      pp_h012j_5f_HT_4400_8500_hmumu,
                      pp_h012j_5f_HT_8500_100000_hmumu,
                      pp_h012j_5f_hmumu,
                      pp_tth01j_5f_HT_0_1100_hmumu,
                      pp_tth01j_5f_HT_1100_2700_hmumu,
                      pp_tth01j_5f_HT_2700_4900_hmumu,
                      pp_tth01j_5f_HT_4900_8100_hmumu,
                      pp_tth01j_5f_HT_8100_100000_hmumu,
                      pp_tth01j_5f_hmumu,
                      pp_vbf_h01j_5f_HT_0_2000_hmumu,
                      pp_vbf_h01j_5f_HT_2000_4000_hmumu,
                      pp_vbf_h01j_5f_HT_4000_7200_hmumu,
                      pp_vbf_h01j_5f_HT_7200_100000_hmumu,
                      pp_vbf_h01j_5f_hmumu,
                      pp_vh012j_5f_HT_0_300_hmumu,
                      pp_vh012j_5f_HT_300_1400_hmumu,
                      pp_vh012j_5f_HT_1400_2900_hmumu,
                      pp_vh012j_5f_HT_2900_5300_hmumu,
                      pp_vh012j_5f_HT_5300_8800_hmumu,
                      pp_vh012j_5f_HT_8800_100000_hmumu,
                      pp_vh012j_5f_hmumu,
                      pp_llv01j_5f_HT_0_800,
                      pp_llv01j_5f_HT_800_2000,
                      pp_llv01j_5f_HT_2000_4000,
                      pp_llv01j_5f_HT_4000_100000,
                      pp_llv01j_5f,
                      pp_ll012j_5f_HT_0_200,
                      pp_ll012j_5f_HT_200_700,
                      pp_ll012j_5f_HT_700_1500,
                      pp_ll012j_5f_HT_1500_2700,
                      pp_ll012j_5f_HT_2700_4200,
                      pp_ll012j_5f_HT_4200_100000,
                      pp_ll012j_5f,
                      pp_v0123j_5f_HT_0_1500,
                      pp_v0123j_5f_HT_1500_2900,
                      pp_v0123j_5f_HT_2900_5100,
                      pp_v0123j_5f_HT_5100_8500,
                      pp_v0123j_5f_HT_8500_100000,
                      pp_v0123j_5f,
                      pp_vv012j_5f_HT_0_300,
                      pp_vv012j_5f_HT_300_1400,
                      pp_vv012j_5f_HT_1400_2900,
                      pp_vv012j_5f_HT_2900_5300,
                      pp_vv012j_5f_HT_5300_8800,
                      pp_vv012j_5f_HT_8800_100000,
                      pp_vv012j_5f,
                      pp_tt012j_5f_HT_0_600,
                      pp_tt012j_5f_HT_600_1200,
                      pp_tt012j_5f_HT_1200_2100,
                      pp_tt012j_5f_HT_2100_3400,
                      pp_tt012j_5f_HT_3400_5300,
                      pp_tt012j_5f_HT_5300_8100,
                      pp_tt012j_5f_HT_8100_100000,
                      pp_tt012j_5f,
                      ]

pp_h012j_5f_HT_0_100_hmumu.splitFactor = 10
pp_h012j_5f_HT_100_400_hmumu.splitFactor = 10
pp_h012j_5f_HT_400_1000_hmumu.splitFactor = 10
pp_h012j_5f_HT_1000_1900_hmumu.splitFactor = 10
pp_h012j_5f_HT_1900_4400_hmumu.splitFactor = 10
pp_h012j_5f_HT_4400_8500_hmumu.splitFactor = 10
pp_h012j_5f_HT_8500_100000_hmumu.splitFactor = 10
pp_h012j_5f_hmumu.splitFactor = 10
pp_tth01j_5f_HT_0_1100_hmumu.splitFactor = 10
pp_tth01j_5f_HT_1100_2700_hmumu.splitFactor = 10
pp_tth01j_5f_HT_2700_4900_hmumu.splitFactor = 10
pp_tth01j_5f_HT_4900_8100_hmumu.splitFactor = 10
pp_tth01j_5f_HT_8100_100000_hmumu.splitFactor = 10
pp_tth01j_5f_hmumu.splitFactor = 10
pp_vbf_h01j_5f_HT_0_2000_hmumu.splitFactor = 10
pp_vbf_h01j_5f_HT_2000_4000_hmumu.splitFactor = 10
pp_vbf_h01j_5f_HT_4000_7200_hmumu.splitFactor = 10
pp_vbf_h01j_5f_HT_7200_100000_hmumu.splitFactor = 10
pp_vbf_h01j_5f_hmumu.splitFactor = 10
pp_vh012j_5f_HT_0_300_hmumu.splitFactor = 10
pp_vh012j_5f_HT_300_1400_hmumu.splitFactor = 10
pp_vh012j_5f_HT_1400_2900_hmumu.splitFactor = 10
pp_vh012j_5f_HT_2900_5300_hmumu.splitFactor = 10
pp_vh012j_5f_HT_5300_8800_hmumu.splitFactor = 10
pp_vh012j_5f_HT_8800_100000_hmumu.splitFactor = 10
pp_vh012j_5f_hmumu.splitFactor = 10
pp_llv01j_5f_HT_0_800.splitFactor = 10
pp_llv01j_5f_HT_800_2000.splitFactor = 10
pp_llv01j_5f_HT_2000_4000.splitFactor = 10
pp_llv01j_5f_HT_4000_100000.splitFactor = 10
pp_llv01j_5f.splitFactor = 10
pp_ll012j_5f_HT_0_200.splitFactor = 10
pp_ll012j_5f_HT_200_700.splitFactor = 10
pp_ll012j_5f_HT_700_1500.splitFactor = 10
pp_ll012j_5f_HT_1500_2700.splitFactor = 10
pp_ll012j_5f_HT_2700_4200.splitFactor = 10
pp_ll012j_5f_HT_4200_100000.splitFactor = 10
pp_ll012j_5f.splitFactor = 10
pp_v0123j_5f_HT_0_1500.splitFactor = 10
pp_v0123j_5f_HT_1500_2900.splitFactor = 10
pp_v0123j_5f_HT_2900_5100.splitFactor = 10
pp_v0123j_5f_HT_5100_8500.splitFactor = 10
pp_v0123j_5f_HT_8500_100000.splitFactor = 10
pp_v0123j_5f.splitFactor = 10
pp_vv012j_5f_HT_0_300.splitFactor = 10
pp_vv012j_5f_HT_300_1400.splitFactor = 10
pp_vv012j_5f_HT_1400_2900.splitFactor = 10
pp_vv012j_5f_HT_2900_5300.splitFactor = 10
pp_vv012j_5f_HT_5300_8800.splitFactor = 10
pp_vv012j_5f_HT_8800_100000.splitFactor = 10
pp_vv012j_5f.splitFactor = 10
pp_tt012j_5f_HT_0_600.splitFactor = 10
pp_tt012j_5f_HT_600_1200.splitFactor = 10
pp_tt012j_5f_HT_1200_2100.splitFactor = 10
pp_tt012j_5f_HT_2100_3400.splitFactor = 10
pp_tt012j_5f_HT_3400_5300.splitFactor = 10
pp_tt012j_5f_HT_5300_8100.splitFactor = 10
pp_tt012j_5f_HT_8100_100000.splitFactor = 10
pp_tt012j_5f.splitFactor = 10
'''
selectedComponents = [comp]


#from heppy.analyzers.fcc.Reader import Reader
#for fcc_v02
from heppy.FCChhAnalyses.analyzers.Reader import Reader

source = cfg.Analyzer(
    Reader,

    weights = 'mcEventWeights',

    gen_particles = 'skimmedGenParticles',
    
    muons = 'muons',
    muonITags = 'muonITags',
    muonsToMC = 'muonsToMC',

    jets = 'jets',
    bTags = 'bTags',
 
    photons = 'photons',
    
    pfphotons = 'pfphotons',
    pfcharged = 'pfcharged',
    pfneutrals = 'pfneutrals',

    met = 'met',

)

from ROOT import gSystem
gSystem.Load("libdatamodelDict")
from EventStore import EventStore as Events


#############################
##   Reco Level Analysis   ##
#############################


'''
####### ADVANCED ANALYSIS (double check workflow) ######################)

# select fsr photon candidates
from heppy.analyzers.Selector import Selector
sel_photons = cfg.Analyzer(
    Selector,
    'sel_photons',
    output = 'sel_photons',
    input_objects = 'photons',
    filter_func = lambda ptc: ptc.pt()>2
)

# produce particle collection to be used for fsr photon isolation
from heppy.analyzers.Merger import Merger
iso_candidates = cfg.Analyzer(
      Merger,
      instance_label = 'iso_candidates', 
      inputs = ['pfphotons','pfcharged','pfneutrals'],
      output = 'iso_candidates'
)
# compute fsr photon isolation w/r other particles in the event.
from heppy.analyzers.IsolationAnalyzer import IsolationAnalyzer
from heppy.particles.isolation import EtaPhiCircle

iso_photons = cfg.Analyzer(
    IsolationAnalyzer,
    candidates = 'photons',
    particles = 'iso_candidates',
    iso_area = EtaPhiCircle(0.3)
)

# select isolated photons
sel_iso_photons = cfg.Analyzer(
    Selector,
    'sel_iso_photons',
    output = 'sel_iso_photons',
    input_objects = 'sel_photons',
    filter_func = lambda ptc : ptc.iso.sumpt/ptc.pt()<1.0
)

# remove fsr photons from particle-flow photon collections
from heppy.analyzers.Subtractor import Subtractor
pfphotons_nofsr = cfg.Analyzer(
      Subtractor,
      instance_label = 'pfphotons_nofsr', 
      inputA = 'pfphotons',
      inputB = 'sel_iso_photons',
      output = 'pfphotons_nofsr'
)

# produce particle collection to be used for lepton isolation
iso_candidates_nofsr = cfg.Analyzer(
      Merger,
      instance_label = 'iso_candidates_nofsr', 
      inputs = ['pfphotons_nofsr','pfcharged','pfneutrals'],
      output = 'iso_candidates_nofsr'
)

# select muons with pT > 10
from heppy.analyzers.Selector import Selector
sel_muons = cfg.Analyzer(
    Selector,
    'sel_muons',
    output = 'sel_muons',
    input_objects = 'muons',
    filter_func = lambda ptc: ptc.pt()>10
)

# compute muon isolation 
iso_muons = cfg.Analyzer(
    IsolationAnalyzer,
    candidates = 'sel_muons',
    particles = 'iso_candidates_nofsr',
    iso_area = EtaPhiCircle(0.4)
)

# "dress" muons with fsr photons
from heppy.analyzers.LeptonFsrDresser import LeptonFsrDresser
dressed_muons = cfg.Analyzer(
    LeptonFsrDresser,
    output = 'dressed_muons',
    particles = 'sel_iso_photons',
    leptons = 'sel_iso_muons',
    area = EtaPhiCircle(0.3)
)
'''

######################## SIMPLE ANALYSIS #####################

# select muons with pT > 10
from heppy.analyzers.Selector import Selector
sel_muons = cfg.Analyzer(
    Selector,
    'sel_muons',
    output = 'sel_muons',
    input_objects = 'muons',
    filter_func = lambda ptc: ptc.pt()>15
)

# select isolated muons
dressed_muons = cfg.Analyzer(
    Selector,
    'dressed_muons',
    output = 'dressed_muons',
    input_objects = 'sel_muons',
    filter_func = lambda ptc: ptc.iso.sumpt/ptc.pt()<0.4
)

###############################################################


# select jet above 30 GeV
jets_30 = cfg.Analyzer(
    Selector,
    'jets_30',
    output = 'jets_30',
    input_objects = 'jets',
    filter_func = lambda jet: jet.pt()>30.
)
from heppy.analyzers.Matcher import Matcher
match_muon_jets = cfg.Analyzer(
    Matcher,
    'muon_jets',
    delta_r = 0.2,
    match_particles = 'dressed_muons',
    particles = 'jets_30'
)

jets_nomuon = cfg.Analyzer(
    Selector,
    'jets_nomuon',
    output = 'jets_nomuon',
    input_objects = 'jets_30',
    filter_func = lambda jet: jet.match is None
)

# select lights with pT > 30 GeV and relIso < 0.4
selected_lights = cfg.Analyzer(
    Selector,
    'selected_lights',
    output = 'selected_lights',
    input_objects = 'jets_nomuon',
    filter_func = lambda ptc: ptc.pt()>30 and ptc.tags['bf'] == 0
)

# select b's with pT > 30 GeV
selected_bs = cfg.Analyzer(
    Selector,
    'selected_bs',
    output = 'selected_bs',
    input_objects = 'jets_nomuon',
    filter_func = lambda ptc: ptc.pt()>30 and ptc.tags['bf'] > 0
)

# create H boson candidates with bs
from heppy.analyzers.LeptonicHiggsBuilder import LeptonicHiggsBuilder
higgses = cfg.Analyzer(
      LeptonicHiggsBuilder,
      output = 'higgses',
      leptons = 'dressed_muons',
      pdgid = 25
)

# apply event selection. Defined in "analyzers/examples/hmumu/selection.py"
from heppy.FCChhAnalyses.hmumu.selection import Selection
selection = cfg.Analyzer(
    Selection,
    instance_label='cuts'
)

# store interesting quantities into flat ROOT tree
from heppy.FCChhAnalyses.hmumu.TreeProducer import TreeProducer
reco_tree = cfg.Analyzer(
    TreeProducer,
    higgses = 'higgses',
)

# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
    source,
    sel_muons,
    dressed_muons,
    jets_30,
    match_muon_jets,
    jets_nomuon,
    selected_lights,
    selected_bs,
    higgses,
    selection,
    reco_tree,
    ] )

config = cfg.Config(
    components = selectedComponents,
    sequence = sequence,
    services = [],
    events_class = Events
)

if __name__ == '__main__':
    import sys
    from heppy.framework.looper import Looper

    def next():
        loop.process(loop.iEvent+1)

    loop = Looper( 'looper', config,
                   nEvents=100,
                   nPrint=0,
                   timeReport=True)
    loop.process(6)
    print loop.event
