import numpy as np

# parameter Settings
Ndim=16 # the optimal dimension for isometric representation is 16
n0=Ndim*6
ZERO=np.zeros((Ndim,Ndim))
II=np.eye(Ndim)
M0=np.concatenate((np.concatenate((ZERO,ZERO, II),axis=1),np.concatenate((II, ZERO, ZERO),axis=1),np.concatenate((ZERO,II, ZERO),axis=1)))
# Construct 6-th order cyclic group
ZERO45=np.zeros((Ndim*3,Ndim*3))
# M6 is the determined omega matrix
M6=np.concatenate((np.concatenate((ZERO45,M0),axis=1),np.concatenate((M0, ZERO45),axis=1)))

bl62={'A':[4,-1,-2,-2,0,-1,-1,0,-2,-1,-1,-1,-1,-2,-1,1,0,-3,-2,0],
      'R':[-1,4,0,-2,-3,1,0,-2,0,-3,-2,2,-1,-3,-2,-1,-1,-3,-2,-3],
      'N':[-2,0,4,1,-3,0,0,0,1,-3,-3,0,-2,-3,-2,1,0,-4,-2,-3],
      'D':[-2,-2,1,4,-3,0,2,-1,-1,-3,-4,-1,-3,-3,-1,0,-1,-4,-3,-3],
      'C':[0,-3,-3,-3,4,-3,-4,-3,-3,-1,-1,-3,-1,-2,-3,-1,-1,-2,-2,-1],
      'Q':[-1,1,0,0,-3,4,2,-2,0,-3,-2,1,0,-3,-1,0,-1,-2,-1,-2],
      'E':[-1,0,0,2,-4,2,4,-2,0,-3,-3,1,-2,-3,-1,0,-1,-3,-2,-2],
      'G':[0,-2,0,-1,-3,-2,-2,4,-2,-4,-4,-2,-3,-3,-2,0,-2,-2,-3,-3],
      'H':[-2,0,1,-1,-3,0,0,-2,4,-3,-3,-1,-2,-1,-2,-1,-2,-2,2,-3],
      'I':[-1,-3,-3,-3,-1,-3,-3,-4,-3,4,2,-3,1,0,-3,-2,-1,-3,-1,3],
      'L':[-1,-2,-3,-4,-1,-2,-3,-4,-3,2,4,-2,2,0,-3,-2,-1,-2,-1,1],
      'K':[-1,2,0,-1,-3,1,1,-2,-1,-3,-2,4,-1,-3,-1,0,-1,-3,-2,-2],
      'M':[-1,-1,-2,-3,-1,0,-2,-3,-2,1,2,-1,4,0,-2,-1,-1,-1,-1,1],
      'F':[-2,-3,-3,-3,-2,-3,-3,-3,-1,0,0,-3,0,4,-4,-2,-2,1,3,-1],
      'P':[-1,-2,-2,-1,-3,-1,-1,-2,-2,-3,-3,-1,-2,-4,4,-1,-1,-4,-3,-2],
      'S':[1,-1,1,0,-1,0,0,0,-1,-2,-2,0,-1,-2,-1,4,1,-3,-2,-2],
      'T':[0,-1,0,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1,-2,-1,1,4,-2,-2,0],
      'W':[-3,-3,-4,-4,-2,-2,-3,-2,-2,-3,-2,-3,-1,1,-4,-3,-2,4,2,-3],
      'Y':[-2,-2,-2,-3,-2,-1,-2,-3,2,-1,-1,-2,-1,3,-3,-2,-2,2,4,-1],
      'V':[0,-3,-3,-3,-1,-2,-2,-3,-3,3,1,-2,1,-1,-2,-2,0,-3,-1,4]}

X=np.array([[-0.31230882, -0.53572156, -0.01949946, -0.12211268, -0.70947917,
        -0.42211092,  0.02783931,  0.02637933, -0.41760305,  0.21809875,
         0.53532768,  0.04833016,  0.07877711,  0.50464914, -0.26972087,
        -0.52416842],
       [ 0.29672002,  0.29005364,  0.18176298, -0.05103382, -0.34686519,
         0.58024228, -0.49282931,  0.62304281, -0.09575202,  0.30115555,
         0.09913529,  0.1577466 , -0.94391939, -0.10505925,  0.05482389,
         0.38409897],
       [-0.42212537,  0.12225749,  0.16279646,  0.60099009,  0.19734216,
         0.42819919, -0.33562418,  0.17036334,  0.4234109 ,  0.46681561,
        -0.50347222, -0.37936876,  0.1494825 ,  0.32176759,  0.28584684,
         0.68469861],
       [ 0.18599294, -0.44017825, -0.4476952 ,  0.34340976,  0.44603553,
         0.40974629, -0.60045935, -0.09056728,  0.22147919, -0.33029418,
         0.55635594, -0.54149972,  0.05459062,  0.57334159, -0.06227118,
         0.65299872],
       [-0.19010428,  0.64418792, -0.85286762,  0.21380295,  0.37639516,
        -0.67753593,  0.38751609,  0.55746524,  0.01443766,  0.1776535 ,
         0.62853954, -0.15048523,  0.55100206, -0.21426656,  0.3644061 ,
        -0.0018255 ],
       [ 0.7350723 ,  0.10111267,  0.55640019, -0.18226966,  0.51658102,
        -0.19321508, -0.46599027, -0.02989911,  0.4036196 , -0.11978213,
        -0.29837524, -0.30232765, -0.36738065, -0.1379793 ,  0.04362871,
         0.33553714],
       [ 0.41134047,  0.13512443,  0.62492322, -0.10120261, -0.03093491,
         0.23751917, -0.68338694,  0.05124762,  0.41533821,  0.46669353,
         0.31467277, -0.02427587,  0.15361135,  0.70595112, -0.27952632,
         0.32408931],
       [-0.33041265, -0.43860065, -0.5509376 , -0.04380843, -0.35160935,
         0.25134855,  0.53409314,  0.54850824,  0.59490287,  0.32669345,
        -0.45355268, -0.56317041, -0.55416297,  0.18117841, -0.71600849,
        -0.08989825],
       [-0.40366849,  0.10978974,  0.0280101 , -0.46667987, -0.45607028,
         0.54114052, -0.77552923, -0.10720425,  0.55252091, -0.34397153,
        -0.59813694,  0.15567728,  0.03071009, -0.02176143,  0.34442719,
         0.14681541],
       [ 0.19280422,  0.35777863,  0.06139255,  0.20081699, -0.30546596,
        -0.56901549, -0.15290953, -0.31181573, -0.74523217,  0.22296016,
        -0.39143832, -0.16474685,  0.58064427, -0.77386654,  0.19713107,
        -0.49477418],
       [-0.16133903,  0.22112761, -0.53162136,  0.34764073, -0.08522381,
        -0.2510216 ,  0.04699411, -0.25702389, -0.8739765 , -0.24171728,
        -0.24370533,  0.42193635,  0.41056913, -0.60378211, -0.65756832,
         0.0845203 ],
       [-0.34792144,  0.18450939,  0.77038332,  0.63868511, -0.06221681,
         0.11930421,  0.04895523, -0.22463059, -0.03268844, -0.58941354,
         0.11640045,  0.32384901, -0.42952779,  0.58119471,  0.07288662,
         0.26669673],
       [ 0.01834555, -0.16367754,  0.34900298,  0.45087949,  0.47073855,
        -0.37377404,  0.0606911 ,  0.2455703 , -0.55182937, -0.20261009,
         0.28325423, -0.04741146,  0.30565238, -0.62090653,  0.17528413,
        -0.60434975],
       [-0.55464981,  0.50918784, -0.21371646, -0.63996967, -0.37656862,
         0.27852662,  0.3287838 , -0.56800869,  0.23260763, -0.20653106,
         0.63261439, -0.22666691,  0.00726302, -0.60125196,  0.07139961,
        -0.35086639],
       [ 0.94039731, -0.25999326,  0.43922549, -0.485738  , -0.20492235,
        -0.26005626,  0.68776626,  0.57826888, -0.05973995, -0.1193658 ,
        -0.12102433, -0.22091354,  0.43427913,  0.71447886,  0.32745991,
         0.03466398],
       [-0.13194625, -0.12262688,  0.18029209,  0.16555524,  0.39594125,
        -0.58110665,  0.16161717,  0.0839783 ,  0.0911945 ,  0.34546976,
        -0.29415349,  0.29891936, -0.60834721,  0.5943593 , -0.29473819,
         0.4864154 ],
       [ 0.40850093, -0.4638894 , -0.39732987, -0.01972861,  0.51189582,
         0.10176704,  0.37528519, -0.41479418, -0.1932531 ,  0.54732221,
        -0.11876511,  0.32843973, -0.259283  ,  0.59500132,  0.35168375,
        -0.21733727],
       [-0.50627723, -0.1973602 , -0.02339884, -0.66846048,  0.62696606,
         0.60049717,  0.69143364, -0.48053591,  0.17812208, -0.58481821,
        -0.23551415, -0.06229112,  0.20993116, -0.72485884,  0.34375662,
        -0.23539168],
       [-0.51388312, -0.2788953 ,  0.00859533, -0.5247195 , -0.18021544,
         0.28372911,  0.10791359,  0.13033494,  0.34294013, -0.70310089,
        -0.13245433,  0.48661081,  0.08451644, -0.69990992,  0.0408274 ,
        -0.47204888],
       [ 0.68546275,  0.22581365, -0.32571833,  0.34394298, -0.43232367,
        -0.5041842 ,  0.04784017, -0.53067936, -0.50049908,  0.36874221,
         0.22429186,  0.4616482 ,  0.11159174, -0.26827959, -0.39372848,
        -0.40987423]])

def EncodingCDR3(s, M, n0):

    bl62np = {}
    vkk = list(bl62.keys())
    for ii in range(20):
        kk = vkk[ii]
        bl62np[kk] = np.array(list(X[ii,]) + [0] * Ndim * 5)

    sL = list(s)
    x = np.array([0] * n0)
    for ii in range(len(sL)):
        x = np.dot(M, (x + bl62np[sL[ii]]))
    return x

def CollapseUnique(LD, VD, ID, SD):
    kks = LD.keys()
    LDu = {}
    VDu = {}
    IDu = {}
    SDu = {}
    for kk in kks:
        vvL = list(LD[kk])
        if len(VD) > 0:
            vvV = list(VD[kk])
        else:
            vvV = ['TRBV2-1*01'] * len(vvL)
        vvI = list(ID[kk])
        vvS = list(SD[kk])
        zz = zip(vvL, vvS, vvV, vvI)
        zzs = sorted(zz, key=lambda x: (x[1], x[2]))
        nz = len(zzs)
        pointer_pre = 0
        pointer_cur = 1
        s_pre = zzs[pointer_pre][1]
        v_pre = zzs[pointer_pre][2]
        uS = [s_pre]
        uV = [v_pre]
        uI = [[zzs[pointer_pre][3]]]
        while pointer_cur < nz:
            s_cur = zzs[pointer_cur][1]
            v_cur = zzs[pointer_cur][2]
            if s_cur == s_pre and v_cur == v_pre:
                uI[len(uI) - 1].append(zzs[pointer_cur][3])
                pointer_cur += 1
                continue
            else:
                uS.append(s_cur)
                uV.append(v_cur)
                uI.append([zzs[pointer_cur][3]])
                s_pre = s_cur
                v_pre = v_cur
                pointer_pre = pointer_cur
                pointer_cur += 1
        uL = [x for x in range(len(uS))]
        LDu[kk] = uL
        SDu[kk] = uS
        if len(VD) > 0:
            VDu[kk] = uV
        IDu[kk] = uI
    return LDu, VDu, IDu, SDu

def EncodeRepertoire(data, ST=3, verbose=True):
    # No V gene version
    # Encode CDR3 sequences into 96 dimensional space
    vectors = []

    if data.empty:
        print("There is no data")
    else:
        seqs = []
        count = 0
        if verbose:
            print('Creating CDR3 list')
        for index, value in data.items():
            cdr3 = value
            if '*' in cdr3:
                continue
            if '_' in cdr3:
                continue
            flag = True
            for i in list(cdr3):
                if i not in ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']:
                    flag = False
                if flag == False:
                    break
            if flag == True:
                seqs.append(value)
                count += 1

        if verbose:
            print('Performing CDR3 encoding')

        for seq in seqs:
            if len(seq) >= ST + 7:
                dM = np.array([EncodingCDR3(seq[ST:-2], M6, n0)])
                dM = dM.astype("float32")
                vectors.append(dM)
            else:
                print("The length of this sequence < ST + 7 !")
                continue

    return vectors
