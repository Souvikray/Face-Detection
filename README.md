The idea behind object detection in a video is that a video is nothing but a continous set of images called frames.So if there is a difference in pixel values of two images,we know the images are different.Hence something has been detected in a video.We can calcuate the difference in pixel values of two matrices(images are represented in matrices) by various methods.Three of them are

Sum Square Error

Mean Square Error

and the third one we used here Structural Similarity.

Unlike the other two methods, Structural Similarity compares two matrix on the basis of a group of pixels and then gives a result.The idea is if two images have very few difference in their pixel value,they are still similar image rather than declaring it dissimilar.It is calculated using the below equation.

SSIM(A,B) = l(A,B) * c(A,B) * s(A,B)

l - luminance

c - constant

s - structure

It gives a value between -1 and 1.Closer the value towards 1,similar the images are.

Below is the test result of an object detection in a video file.Its basically me coming in front of webcam all of a sudden.

0.95931292887
0.970093337722
0.972798579749
0.96496445517
0.971427062684
0.96782079374
0.956357507916
0.945002855175
0.972112202123
0.963695434127
0.88608107647
0.764708928834
0.726728482706
0.775370756139
0.749002422764
0.73951190869
0.743099671279
0.779373770211
0.838692254969
0.857351547549
0.860112378521
0.895196849587
0.903938152352
0.931915538307
0.901983911321

If we observe carefully,intially the values are close to 1 as the environment is stable.But once it detects an object,the value decreases rapidly as seen

0.963695434127

0.88608107647

0.764708928834

0.726728482706

This drop of value is detected and the user is immediately sent an alert through text message informing him/her of possible change in the environment.
