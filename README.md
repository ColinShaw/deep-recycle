# DeepTrash

This is an image segmentation project having to do with identifying 
trash in images.  All the trash that we generate is absolutely disgusting,
so I thought it would be interesting to train an image segmenation model
to try to identify trash in images.  

First problem is training data. There is a script that will download 
a bunch of images from a Google search.  The ones with trash are put
in `/data/trash/` and the ones that are landscapes are put in 
`/data/landscape/`.  The specifics of what search items are used come 
from the `configs/image.yaml` file, so it is simple to change the queries and
get different training data.  You can clean these groups of images 
up with the `cleanup.sh` script in the `/data/` directory.

Once you fetch the data you will need to go through and make sure it 
looks reasonable.  Just get rid of stuff with text in it, transparent
backgrounds, things that are at a way too large or small scale, etc.  Some
categories, like city streets, need additional care since they often 
contain trash, and we don't want the background images to have trash since
we are going to overlay trash on these landscape backgrounds.  For the trash
photos you don't need to keep all that many.  You want to discard the ones that 
have a lot of spaces and distractions.  Once you narrow those down you are
going to want to crop the images so that they contain only trash, as we
will be sampling blobs out of them.


