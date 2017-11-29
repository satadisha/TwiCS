

import SatadishaModule_final_trie as phase1
import phase2_Trie as phase2
import datetime
from threading import Thread
import random
import math
from queue  import Queue
import pandas as pd 
import warnings
import numpy as np
import time
import trie as trie
import pickle
import matplotlib.pyplot as plt
import copy
import SVM as svm
import matplotlib.ticker as ticker
import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style
import matplotlib
from matplotlib import rc
import matplotlib.font_manager as fm

fontPath = "/usr/share/fonts/truetype/abyssinica/AbyssinicaSIL-R.ttf"
font_axis = fm.FontProperties(fname=fontPath, size=24)

fontPath = "/usr/share/fonts/truetype/abyssinica/AbyssinicaSIL-R.ttf"
font_legend = fm.FontProperties(fname=fontPath, size=13)

whole_level=[[0.633720930232558, 0.58774373259052926, 0.59113300492610832, 0.58018018018018025, 0.57688723205964576, 0.57878787878787874, 0.57290589451913143], [0.6297376093294461, 0.58659217877094971, 0.58823529411764697, 0.57682926829268288, 0.57438794726930309, 0.57986373959121873, 0.57592339261285896], [0.6297376093294461, 0.58741258741258739, 0.58872305140961867, 0.57718120805369122, 0.57331447430457338, 0.57962264150943399, 0.57676630434782616], [0.6297376093294461, 0.58741258741258739, 0.58872305140961867, 0.57718120805369122, 0.57331447430457338, 0.57908644771611928, 0.57630590645271429], [0.633720930232558, 0.58774373259052926, 0.58997534921939188, 0.57916917519566524, 0.57608189855746861, 0.57886792452830182, 0.57309140705237938], [0.6297376093294461, 0.58741258741258739, 0.58872305140961867, 0.57718120805369122, 0.57331447430457338, 0.57908644771611928, 0.57630590645271429], [0.6297376093294461, 0.58659217877094971, 0.59008264462809912, 0.58009708737864085, 0.57599999999999996, 0.58010630220197434, 0.57496561210453923], [0.6297376093294461, 0.58659217877094971, 0.58823529411764697, 0.57682926829268288, 0.57438794726930309, 0.57986373959121873, 0.57586206896551728], [0.4463519313304721, 0.42588726513569936, 0.40251572327044022, 0.41035120147874304, 0.42467718794835013, 0.42030696576151128, 0.43591130340724715], [0.3253588516746412, 0.3248259860788863, 0.29503546099290778, 0.29926238145416229, 0.31492168178070895, 0.322972972972973, 0.34615384615384615], [0.1693121693121693, 0.22772277227722773, 0.21257485029940118, 0.22197558268590456, 0.24697754749568226, 0.26460239268121044, 0.28811369509043927], [0.1497326203208556, 0.19143576826196473, 0.16666666666666666, 0.1763341067285383, 0.19907834101382485, 0.21477532368621474, 0.23897581792318634], [0.11956521739130435, 0.17346938775510204, 0.15576323987538943, 0.15981198589894241, 0.17860465116279073, 0.1941896024464832, 0.22001419446415896], [0.10928961748633878, 0.14987080103359171, 0.13440000000000002, 0.14077669902912621, 0.1562198649951784, 0.16916996047430832, 0.19117647058823531], [0.08839779005524862, 0.12073490813648295, 0.11631663974151858, 0.11793611793611793, 0.1364522417153996, 0.15163607342378291, 0.16880180859080635], [0.07777777777777778, 0.10582010582010581, 0.10406504065040649, 0.11138613861386139, 0.12289395441030726, 0.13736713000817663, 0.15926493108728942], [0.06703910614525138, 0.095744680851063829, 0.094771241830065356, 0.097622027534418024, 0.10989010989010987, 0.12171052631578944, 0.14285714285714288], [0.056179775280898875, 0.080428954423592491, 0.085385878489326758, 0.088050314465408813, 0.1004016064257028, 0.10927152317880794, 0.12116443745082613], [0.04519774011299435, 0.075268817204301078, 0.079077429983525543, 0.08322824716267338, 0.092741935483870969, 0.099833610648918478, 0.11075949367088608], [0.04519774011299435, 0.075268817204301078, 0.076666666666666661, 0.070038910505836577, 0.077324973876698011, 0.080000000000000002, 0.089256198347107421], [0.04519774011299435, 0.062992125984251982, 0.069291338582677178, 0.079041916167664664, 0.087040618955512586, 0.091787439613526575, 0.10422960725075528]]

tweets_been_processed_list=[500,1000,1500,2000,2500,3000,3200]
whole_level_transposed=list(map(list, zip(*whole_level)))

fig, ax = plt.subplots()
params = {
   'text.usetex': False,
    'legend.fontsize': 3,
   'figure.figsize': [40, 400]
   }

matplotlib.rcParams.update(params)

markers=['x','d','>','s','*','o','D']
Z_scores=[-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]

for idx,level in enumerate(whole_level_transposed):

    f1=level
    ax.plot( Z_scores,f1 ,marker=markers[idx] , label=tweets_been_processed_list[idx],markersize=7,linewidth=1)
    
    major_ticks = np.arange(-1.0, 1.2, 0.2)                                              
    minor_ticks = np.arange(-1.0, 1.2, 0.1)                                               

    ax.set_xticks(major_ticks)                                                       
    ax.set_xticks(minor_ticks, minor=True)                                           
    # ax.set_yticks(major_ticks)                                                       
    # ax.set_yticks(minor_ticks, minor=True)                                           

    # and a corresponding grid                                                       

    ax.grid(which='both')                                                            

    # or if you want differnet settings for the grids:                               
    ax.grid(which='minor', alpha=0.2)                                                
    ax.grid(which='major', alpha=0.5)     
    ax.set_ylim([0,0.70])
    ax.set_xlim([-1.1,1.1])
    # tick_spacing = 0.1
    # ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    plt.xlabel('Z Score',fontproperties=font_axis)
    plt.ylabel('F1 Score',fontproperties=font_axis)
    plt.grid(True)
    legend=plt.legend(loc="lower left",ncol=1,frameon=False,prop=font_legend,title="# of Input Tweets")
    plt.setp(legend.get_title(),fontsize='15')


    plt.tick_params(axis='both', which='major', labelsize=12)
fig.savefig("z-score-VS-f1-score-Entity.pdf",dpi=1200,bbox_inches='tight')

plt.show()