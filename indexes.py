
class indexes:
    '''
    Class for getting DWi, SCSE, t_a, M_ia, M_ic, M_ih, M_ib indexes
    '''
    @staticmethod
    def getDWi( A: float, b: float, SG: float) -> float:
        return 92.56 *SG * (A * b)**( -0.977) 
    
    @staticmethod
    def getSCSE( A:float, b: float) -> float:
        return 52.74 * (A*b)**(-.441)
    
    @staticmethod
    def gett_a(A:float, b:float, SG:float) -> float:
        return 2.6132 * (92.56 *SG * (A * b)**( -0.977) )**(-1)
    
    @staticmethod
    def getM_ia(A:float, b:float) -> float:
        return 390 * (A*b) **(-.813)
    
    @staticmethod
    def getM_ic(A:float, b:float) -> float:
        return 303.5 * (A*b)**(-1)
    
    @staticmethod
    def getM_ih(A:float, b:float) -> float:
        return 577 * (A*b)**(-1)
    
    @staticmethod
    def getM_ib(BWI:float) -> float:
        return BWI * 1.86 - 8.7