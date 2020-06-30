-Em "Pre-Logic Script Code" digite:


def LookUp(eInic, eFim, nInic, nFim):
    eFimInic = eFim - eInic
    nFimInic = nFim - nInic
    rumo = abs(math.degrees(math.atan(abs(eFimInic / nFimInic))))

    if (eFimInic>0 and nFimInic>0):
        azimute = abs(rumo)
    elif (eFimInic>0 and nFimInic<0):
        azimute = abs(rumo - 180)
    elif (eFimInic<0 and nFimInic<0):
        azimute = abs(rumo + 180)
    elif (eFimInic<0 and nFimInic>0):
        azimute = abs(rumo - 360)
    
    return azimute 

-No campo abaixo "Nome do campo=" digite apenas:
LookUp(!eInic!, !eFim!, !nInic!, !nFim!)

abs(math.degrees(math.atan(abs(( !eFim! - !eInic! ) / ( !nFim! - !nInic! )))))