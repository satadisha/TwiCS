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

whole_level=[[0.8488160291438979, 0.81340923466160653, 0.78598823830222453, 0.75209272376046366, 0.74555984555984556, 0.7573869988819677, 0.75994384651380453], [0.8488160291438979, 0.8141817030705919, 0.78639038117165527, 0.75241571827356668, 0.74395200309657439, 0.75508569597949715, 0.7577037384639449], [0.8488160291438979, 0.81340923466160653, 0.78598823830222453, 0.75209272376046366, 0.74507531865585153, 0.75698993449432816, 0.75955687314713682], [0.8488160291438979, 0.81340923466160653, 0.78598823830222453, 0.75810580204778155, 0.75067230119093353, 0.76157149673930347, 0.76390183286735003], [0.8488160291438979, 0.81340923466160653, 0.78598823830222453, 0.75209272376046366, 0.74555984555984556, 0.7573869988819677, 0.75994384651380453], [0.8488160291438979, 0.8141817030705919, 0.78639038117165527, 0.75241571827356668, 0.74395200309657439, 0.75508569597949715, 0.7577037384639449], [0.8488160291438979, 0.8141817030705919, 0.78639038117165527, 0.75241571827356668, 0.74395200309657439, 0.75508569597949715, 0.7577037384639449], [0.8488160291438979, 0.81340923466160653, 0.78598823830222453, 0.75209272376046366, 0.74507531865585153, 0.75698993449432816, 0.75955687314713682], [0.8520432127759511, 0.81422399468261886, 0.7699066447007139, 0.73440037114358625, 0.72385379252060011, 0.73477268737932244, 0.73857216230097589], [0.8424591738712777, 0.79972752043596729, 0.74544419134396356, 0.70585389453313985, 0.6893654653990714, 0.70508598609586526, 0.70934379457917263], [0.8167748377433849, 0.77598314606741581, 0.71705882352941175, 0.6763309172706824, 0.66318181818181809, 0.6799249530956849, 0.68289112534309238], [0.7881227981882235, 0.74830900676397294, 0.68742514970059876, 0.65572942958101965, 0.64007336084364963, 0.65693153802389537, 0.66112342941611224], [0.7741935483870968, 0.73916184971098264, 0.67919951485748931, 0.63471502590673579, 0.61702632202987906, 0.63721657544957, 0.64229963830192272], [0.7678018575851392, 0.72627336020520328, 0.66004346476249609, 0.62414698162729665, 0.60260115606936426, 0.62452942341985351, 0.62948668467773061], [0.6741071428571428, 0.65047021943573669, 0.5935653315824031, 0.55018171652222525, 0.53615071283095728, 0.56728177482894471, 0.57361839451391683], [0.6632882882882883, 0.63466878222927414, 0.57920956492859521, 0.54779206260480717, 0.530423620025674, 0.5600669736291336, 0.56625279869733358], [0.6499429874572406, 0.61935483870967734, 0.56266846361185985, 0.52158894645941278, 0.50591638180383913, 0.52456896551724141, 0.53068062827225138], [0.6343713956170703, 0.60497350183448839, 0.55015300918055088, 0.51015670342426012, 0.49429859453725805, 0.50872600349040131, 0.51463725074246924], [0.6322657176749703, 0.61221122112211224, 0.55502063273727642, 0.52420991591765731, 0.50518479127891514, 0.51506487794149991, 0.52053036783575712], [0.6322657176749703, 0.61221122112211224, 0.55509641873278248, 0.52353282975014526, 0.50504514073287321, 0.50990752972258913, 0.51330472103004288], [0.6322657176749703, 0.60050041701417844, 0.54216027874564454, 0.50207468879668049, 0.48371335504885993, 0.49315068493150688, 0.49638870650032835]]

tweets_been_processed_list=[500,1000,1500,2000,2500,3000,3200]
whole_level_transposed=list(map(list, zip(*whole_level)))

fig, ax = plt.subplots()
params = {
   'text.usetex': False,
    'legend.fontsize': 3,
   'figure.figsize': [40, 400]
   }

matplotlib.rcParams.update(params)

markers=['s','d','>','*','x','o','D']
Z_scores=[-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]

for idx,level in enumerate(whole_level_transposed):

    f1=level
    ax.plot( Z_scores,f1 ,marker=markers[idx] , label=tweets_been_processed_list[idx],markersize=6,linewidth=1)
    
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
    ax.set_ylim([0.45,0.90])
    ax.set_xlim([-1.1,1.1])
    
    # tick_spacing = 0.1
    # ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    plt.xlabel('Z Score',fontproperties=font_axis)
    plt.ylabel('F1 Score',fontproperties=font_axis)
    plt.grid(True)
    legend=plt.legend(loc="lower left",ncol=1,frameon=False,prop=font_legend,title="# of Input Tweets")
    plt.setp(legend.get_title(),fontsize='15')

    plt.tick_params(axis='both', which='major', labelsize=12)
fig.savefig("z-score-VS-f1-score-Mention.pdf",dpi=1200,bbox_inches='tight')

plt.show()