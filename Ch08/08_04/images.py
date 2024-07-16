# %%
import cv2

img = cv2.imread('/workspaces/data-science-foundations-python-scientific-stack-3084641/Ch08/08_04/sign.jpg')
img.shape

# %%
import matplotlib.pyplot as plt

plt.imshow(img)

# %%
mpl_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(mpl_img)

# %%
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray)

# %%
plt.imshow(gray, cmap='gray')

# %%
edges = cv2.Canny(gray, 80, 150)
plt.imshow(edges, cmap='gray')
# %%
