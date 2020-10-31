 def reconstruct(sinogram,phantom_size=[100,100]):
    detector_len = sinogram.shape[1]
    phantom =np.zeros(phantom_size)
    for i in range(sinogram.shape[0]):
        angle_step = np.deg2rad(360/sinogram.shape[0])*i
        for element in range(detector_len):
            dis = np.floor((detector_len/2)-element)
            point = [np.round(dis*np.cos(angle_step+np.pi/2)),np.round(dis*np.sin(angle_step+np.pi/2))]
            point_start,point_end = draw_line(point,angle_step,phantom_size[0]/2-45,phantom_size[1]/2-45)
            pathCor=get_cells(add_smthng(point_start,phantom_size[0]/2-50),add_smthng(point_end,phantom_size[0]/2-50))
            for p in pathCor:
                phantom[int(p[0]),int(p[1])]+=sinogram[i,element]
        
    return phantom
phantom =  reconstruct(asss,[250,250])
plt.imshow(phantom,cmap=plt.cm.bone)
plt.show()