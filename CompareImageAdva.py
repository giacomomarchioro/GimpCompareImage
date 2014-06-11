#!/usr/bin/env python
from gimpfu import *

def CompareImageAdva(img,drw,nc,nr,s,par):
    layers = img.layers 
    img.resize((layers[0].width+s)*nc-s,(layers[0].height+s)*nr-s,0,0)
    count=0
    if par==True:
        count=1
    for j in range(0,nr):
        for i in range(0,nc):
            layers[count].translate((layers[0].width+s)*i,(layers[0].height+s)*j)
            count+=1
            if par==True:
                layer2=layers[0].copy()
                img.add_layer(layer2, 0)
                layer2.translate((layers[0].width+s)*i,(layers[0].height+s)*j)
    if par==True:
        img.remove_layer(layers[0])
            
        
register(
        "",
        "Rescale differents layers and center them in a resize image",
        "Allows to rescale differents layers and center them in a resize image",
        "Giacomo Marchioro",
        "GPL License",
        "2013",
        "<Image>/ComparazioneImmagini/CompareImageAdv",
        "*",
        [
                (PF_INT, "nc", "Number of coulum:", 0),
                (PF_INT, "nr", "Number of row:", 0),
                (PF_INT, "s", "Space between images:", 0),
                 (PF_BOOL,"par","Duplicate first layer over the others:",False)
                
        ],
        [],
        CompareImageAdva)
main()
