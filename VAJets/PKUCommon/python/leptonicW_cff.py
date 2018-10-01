import FWCore.ParameterSet.Config as cms

Wtomunu = cms.EDProducer("CandViewShallowCloneCombiner",
                         decay = cms.string("goodMuons slimmedMETs"),
                         #checkCharge = cms.bool(False),
                         cut = cms.string("")
                         )

Wtoenu = cms.EDProducer("CandViewCombiner",
                        decay = cms.string("goodElectrons slimmedMETs"),
                        #checkCharge = cms.bool(False),
                        cut = cms.string("")
                        )
'''
Wtomunu = cms.EDProducer("PKUWLepProducer",
                         leptons=cms.InputTag("goodMuons"),
                         MET=cms.InputTag("slimmedMETs"),
                         cut=cms.string("")
                         )


Wtoenu = cms.EDProducer("PKUWLepProducer",
                        leptons=cms.InputTag("goodElectrons"),
                        MET=cms.InputTag("slimmedMETs"),
                        cut=cms.string("")
                        )
'''
leptonicV = cms.EDProducer("CandViewMerger",
                           src=cms.VInputTag("Wtoenu", "Wtomunu"),
                           cut=cms.string("")
                           )

leptonicVSequence = cms.Sequence(Wtomunu + Wtoenu + leptonicV)
