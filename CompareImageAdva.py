#!/usr/bin/env python
from gimpfu import *

def CompareImageAdva(img,drw,nc,nr,s,par):
    layers = img.layers 
    count=0
    # we copy the width and height of the second layer.
    width = layers[1].width
    height = layers[1].height
    img.resize((width+s)*nc-s,(height+s)*nr-s,0,0)
    if par==True:
        count=1
    for j in range(0,nr):
        for i in range(0,nc):
            layers[count].translate((width+s)*i,(height+s)*j)
            count+=1
            if par==True:
                layer2=layers[0].copy()
                img.add_layer(layer2, 0)
                layer2.translate((width+s)*i,(height+s)*j)
                #if pdb.gimp_drawable_is_text_layer(layer2):
                #    pdb.gimp_text_layer_set_text(layer2,'aaa')
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
