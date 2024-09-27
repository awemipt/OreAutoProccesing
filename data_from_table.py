from dataclasses import dataclass
import numpy as np

@dataclass
class ore53:
    
    energy = np.array([0.4,0.25,0.1])
    t10 = np.array([26.89, 17.99, 8.66])


@dataclass
class ore37_5:
    
    energy = np.array([1,0.25,0.1])
    t10 = np.array([38.33, 13.74, 7.22])




@dataclass
class ore26_5:
    
    energy = np.array([2.5,1,0.25])
    t10 = np.array([57.07, 32.28, 10.17])



@dataclass
class ore19:
    
    energy = np.array([2.49,1,0.25])
    t10 = np.array([53.08, 27.46, 7.94])


@dataclass
class ore13_2:
    
    energy = np.array([2.5,1,0.25])
    t10 = np.array([46.01, 20.74, 7.91])

