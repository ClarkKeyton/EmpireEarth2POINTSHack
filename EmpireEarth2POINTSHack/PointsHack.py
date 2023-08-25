from pymem import Pymem
from pymem.ptypes import RemotePointer

pm = Pymem("EE2X.exe")

def getPointerAddress(base, offsets):
    remote_pointer = RemotePointer(pm.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset
def Main():
    game_module_addr = pm.base_address
    valueoffs = getPointerAddress(game_module_addr + 0x0094D824, offsets=[0xD4])
    pm.write_int(valueoffs, 500000)
    value = pm.read_int(valueoffs)
    print(value)
if __name__ == "__main__":
    Main()