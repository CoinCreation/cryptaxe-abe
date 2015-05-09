from .Sha256Chain import Sha256Chain

class ATOMIC(Sha256Chain):
    def __init__(chain, **kwargs):
        chain.name = 'ATOMIC'
        chain.code3 = 'ATO'
        chain.address_version = '\x17'
        chain.script_addr_vers = '\x0f'
        chain.magic = '\xd8\xe6\xfe\xf5'
        Sha256Chain.__init__(chain, **kwargs)

