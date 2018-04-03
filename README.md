# Trash Detector

This is a toy image segmentation project having to do with identifying 
trash in images.  All the trash that we generate is absolutely disgusting,
so I thought it would be interesting to train an image segmenation model
to try to identify trash in images.  

First problem is training data. There is a script that will download 
a bunch of images from a Google search.  These need to be manually separated
into a collection of images that are purely trash.  A wide range of 
trashless images are also downloaded.  Sections of the trash images are
artificially superimposed on the trashless images to create training images.  The
image mask is generated at the same time.  Much flipping, changing contrast,
adding noise, etc., goes into the transformations for the training.

The network itself is based on FCN32...

