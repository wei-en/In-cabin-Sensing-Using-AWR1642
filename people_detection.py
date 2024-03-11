from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
colorlist=['tab:blue','tab:orange','tab:red','tab:cyan','tab:purple','tab:grey','tab:brown']

def Avg(lst):
    return sum(lst) / len(lst)

def cluster(detObj,e,m):
    numObj=detObj["numObj"]
    X = np.zeros((numObj,2))

    #construct the input data X of DB scan
    for objectNum in range(numObj):
        X[objectNum][0]=detObj["x"][objectNum]*100
        X[objectNum][1]=detObj["y"][objectNum]*100

    #eps:radius min_samples: min_samples
    #the keypoints is to choose correct eps such that the result could be more ideal
    clustering=DBSCAN(eps=e,min_samples=m).fit(X)
    label=clustering.labels_

    #plot result clustering.labels_
    max_label = -1
    # plt.ion()
    # plt.clf()
    for i in range(numObj):
        if label[i] > max_label:
            	max_label = label[i]

    # find the maximum number of the group
    groupnum = max_label + 1
    # build a group index list
    grpdata=[]

    # there are n grpdatas, n = the number of groups
    # we append a dict to record the x, y and doppler of each group
    # where x, y and doppler are lists
    for i in range(groupnum):
	    grpdata.append({"x":[],"y":[],"doppler":[]})

    # remove the noise and put the data (which are in xlim,ylim range) into each group
    # now we should 
    for i in range(numObj):
        # some condition: x, y in range
        grplabel =label[i]
        x = detObj["x"][i]*100
        y = detObj["y"][i]*100
        doppler = detObj["doppler"][i]*100
        if grplabel!=-1 and x>-75 and x <75 and  y < 150:
            grpdata[grplabel]["x"].append(x)
            grpdata[grplabel]["y"].append(y)
            grpdata[grplabel]["doppler"].append(abs(doppler))

    return grpdata, label, X

def objMovingDetect(groupData,threshhold_l,threshhold_u):
    numOfGroup = len(groupData)
    finalCoordinateList = []
    for group in groupData:
        try:
            #type of group is dictionary
            avg = Avg(group["doppler"])
            num = len(group["doppler"])
            # print("avg",avg)
            if  avg >= threshhold_l and avg <= threshhold_u and num >=5  :
                finalCoordinateList.append({"x":Avg(group["x"]), "y":Avg(group["y"])})
                #print(str(Avg(group["x"])) + "   " + str(Avg(group["y"])))
                
        except:
            continue
    
    return finalCoordinateList 

# def drawbirdview(detObj,label,X,finalcoor,sample_time):

#     # plt.ion()
#     plt.clf()
#     numObj=detObj["numObj"]
#     for i in range(numObj):
#         if label[i] == -1:
#             plt.scatter(X[i,0],X[i,1],c='tab:pink',s=300)
#         else:
#             plt.scatter(X[i,0],X[i,1],c = colorlist[label[i]],s=300)

#     for coordinate in finalcoor:   
#         plt.scatter(coordinate["x"],coordinate["y"],marker='^',c = 'black',s = 2300)
    
#     plt.ylabel('y position (cm)')
#     plt.xlabel('x position (cm)')
#     plt.xlim(-75,75)
#     plt.ylim(0,150)
#     plt.draw()
#     plt.pause(sample_time)

      

        