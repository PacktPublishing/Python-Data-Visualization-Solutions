import scipy.misc
import matplotlib.pyplot as plt
lena = scipy.misc.ascent()
plt.gray()
plt.imshow(lena)
plt.colorbar()
plt.show()
print (lena.shape)
print (lena.max())
print (lena.dtype)
