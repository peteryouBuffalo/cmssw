import FWCore.ParameterSet.Config as cms

#------------------------------------------------
#AlCaReco filtering for HCAL HO:
#------------------------------------------------
from Calibration.HcalAlCaRecoProducers.alcahomuon_cfi import *
import HLTrigger.HLTfilters.hltHighLevel_cfi

#
#here we specify triggers for two different menues
#this is possible since throw=False
#

ALCARECOHcalCalHOHLT = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone(
#   HLTPaths = ['HLT_IsoMu3',   #for 8E29
#               'HLT_IsoMu9'],  #for 1E30
   eventSetupPathsKey='HcalCalHO',
   throw = False #dont throw except on unknown path name
) 

# Short-term workaround to preserve the "run for every event" while removing the use of convertToUnscheduled()
# To be reverted in a subsequent PR
seqALCARECOHcalCalHOTask = cms.Task(hoCalibProducer)
seqALCARECOHcalCalHO = cms.Sequence(ALCARECOHcalCalHOHLT, seqALCARECOHcalCalHOTask)



