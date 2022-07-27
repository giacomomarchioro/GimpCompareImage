# Gimp Compare Images plug-in
These are two python GIMP plug-ins to resacle and juxtapose images of the same area.
To use them put the .py file in the GIMP plugin folder see [this guide](http://en.wikibooks.org/wiki/GIMP/Installing_Plugins) for more info. 


#Mac OS
See [this guide](https://medium.com/@tobyliu_blogs/how-to-add-a-python-plug-in-to-gimp-2-10-on-macos-9c7c53bd3807)
```
cd /Applications/GIMP-2.10.app/Contents/Resources/lib/gimp/2.0/plug-ins/
chmod 755 CompareImageAdva.py
```


[![Alt text for your video](http://img.youtube.com/vi/VkfNB5o5G54/0.jpg)](http://www.youtube.com/watch?v=VkfNB5o5G54&feature=youtu.be)

### Important note
The two images must be registered before with an external tool (see [image registration](http://en.wikipedia.org/wiki/Image_registration)).

### ResizeRescaleCenterLayers
In some case (e.g. when you use GIS software) exported images are registered but don't have the same scale.The first plug-in simply center an rescale the images so the can be compared with the second plug-in.

### CompareImageAdv 
It basically allows to place images side by side and eventually automatically palce a marker (arrows, circles, etc. etc.) in every images in the same point over all the images. 

Click on the image to see a youtube tutorial.

