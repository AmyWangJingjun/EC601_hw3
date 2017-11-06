import cv2
import numpy as np
import sys

def add_gaussian_noise(noise_img,m,s):
    img=noise_img.copy()
    cv2.randn(noise_img,m,s)
    gaussian=cv2.add(noise_img,img)
    cv2.imwrite("Gaussian Noise.png",gaussian)
    return gaussian
    
def add_sp_noise(img,pa,pb): 
    salt=img.copy()
    amount1=img.shape[0]*img.shape[1]*pa
    amount2=img.shape[0]*img.shape[1]*pb
    num_salt=int(amount1)
    num_pepper=int(amount2)
    for i in range(num_salt):
        r=np.random.randint(0,img.shape[0]-1)
        c=np.random.randint(0,img.shape[1]-1)
        salt[r,c]=0
    for i in range(num_pepper):
        r=np.random.randint(0,img.shape[0]-1)
        c=np.random.randint(0,img.shape[1]-1)
        salt[r,c]=255
        cv2.imwrite("s_vs_p Noise.png",salt)
        return salt
def main():  
    pa=np.array([0.01,0.03,0.05,0.4])
    pb=np.array([0.01,0.03,0.05,0.4])
    mean=np.array([0,5,10,20])
    sigma=np.array([0,20,50,100])
    ksize=np.array([3,5,7])
    img=cv2.imread('Lenna.png',0)
    row,col=img.shape
    for i in range(3):
        for j in range(4):
            noise_img=img.copy()
            noise_dst=add_gaussian_noise(noise_img,int(mean[j]),int(sigma[j])).copy()
            name='Gaussian_noise{}.png'.format(j)
            cv2.imwrite(name,noise_dst)
            blured=cv2.blur(noise_dst,(ksize[i],ksize[i]))
            name1='box_filter_gss{}_kernal{}.png'.format(j,ksize[i])
            cv2.imwrite(name1,blured)
            
            gauss_blur=cv2.GaussianBlur(noise_dst,(ksize[i],ksize[i]),0)
            name2='Gaussian_filter_gss{}_kernal{}.png'.format(j,ksize[i])
            cv2.imwrite(name2,gauss_blur)
      
            median_blur=cv2.medianBlur(noise_dst,ksize[i])
            name3='median_filter_gss{}_kernal{}.png'.format(j,ksize[i])
            cv2.imwrite(name3,median_blur)
            
    for i in range(3):
        for j in range(4):
            noise_copy2=img.copy()
            noise2_dst=add_sp_noise(noise_copy2,pa[j],pb[j]).copy()
            name='sp_noise{}.png'.format(j)
            cv2.imwrite(name,noise2_dst)
            blured=cv2.blur(noise2_dst,(ksize[i],ksize[i]))
            name1='box_filter_sp{}_kernal{}.png'.format(j,ksize[i])
            cv2.imwrite(name1,blured)
              
            gauss_blur=cv2.GaussianBlur(noise2_dst,(ksize[i],ksize[i]),0)
            name2='Gaussian_filter_sp{}_kernal{}.png'.format(j,ksize[i])
            cv2.imwrite(name2,gauss_blur)
              
            median_blur=cv2.medianBlur(noise2_dst,ksize[i])
            name3='median_filter_sp{}_kernal{}.png'.format(j,ksize[i])
            cv2.imwrite(name3,median_blur)   
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__=="__main__":
    main()

    
    
    
    