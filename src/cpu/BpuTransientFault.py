from m5.params import *
from m5.SimObject import SimObject

class BpuTransientFault(SimObject):
    type = 'BpuTransientFault'
    cxx_header = "cpu/bpu_transient_fault.hh"
    tick = Param.UInt64(0, "Inject fault at this tick")
    faultLabel = Param.String(None, "Injected fault label")
    faultField = Param.UInt32(0, "BTB field where to inject the fault")
    faultEntry = Param.UInt32(0, "BTB entry where to inject the fault")
    faultBitPosition = Param.UInt32(0,
        "BTB entry's bit position where to inject the fault")
    faultStuckBit = Param.UInt32(0, "BTB value changes to faultStuckBit")
    faultEnd = Param.Bool(False,"Is true when the fault has to be removed")
    bpu = Param.BranchPredictor(NULL, "BPredUnit")
