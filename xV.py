# #Μέσα στον κώδικα ακολοθούνται τα βήματα της εργασίας.
# Ενσωμάτωση των απαραίτητων βιβλιοθηκών
import math
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt

#Βήμα 1
import numpy as np
import scipy.io
 
mat_file = scipy.io.loadmat('xV.mat') # Φόρτωση των δεδομένων απο το αρχείο xV.mat
xV=np.array(mat_file['xV']) # Δημιουργία πίνακα xV με το σύνολο των δεδομέμων 

#Βήμα 2
X=xV[:,[0,1]] # Απο τον πίνακα xV χρησιμοποιούμε τα δύο πρώτα χαρακτηριστικά
k=3 # Ο αριθμός των συστάδων
numberOfRows, numberOfColumns = X.shape # Ανάθεση τιμών στις μεταβλητες numberOfRows και numberOfcolumns μεσω της συνάρτησης shape

kmeans=KMeans(n_clusters=k).fit(X) # Εφαρμογή του αλγόριθμο k-means
IDX=kmeans.labels_ # Eτικέτες κάθε σημείου του Κ-means
C=kmeans.cluster_centers_ # Συντεταγμένες των κέντρων των συστάδων του Κ-means

#Εξ ορισμού, ο αλγόριθμος συσταδοποίησης k-means βασίζεται στην Ευκλείδεια απόσταση
#Παρουσιάζει την κλάση που ανήκει η κάθε παρατήρηση
plt.plot(X[IDX==0][:,0],X[IDX==0][:,1],'limegreen',marker='o',linewidth=0,label='C1')
plt.plot(X[IDX==1][:,0],X[IDX==1][:,1],'yellow',marker='o',linewidth=0,label='C2')
plt.plot(X[IDX==2][:,0],X[IDX==2][:,1],'c.',marker='o',label='C3')
plt.scatter(C[:,0],C[:,1],marker='x',color='black',s=150 , linewidth=3 , label="Centroids", zorder=10 ) # Γράφημα διασποράς
plt.legend()
plt.show()

sse=0.0 # Αρχικοποίηση του sse
# Υπολογισμός του sse 
for i in range(k): # Για κάθε συστάδα
      for j in range(numberOfRows): # Για κάθε δείγμα 
        if IDX[j] == i : #Αν το j δείγμα ανήκει στην i συστάδα 
                # τότε υπολόγισε το sse μέσω του τύπου του 
                sse = sse + math.dist(X[j], C[i])**2
                
# Εξω απο το for εκτύπωσε το τελικό see            
print("\n\nsse = %.3f" % sse) 




# #Βήμα 3
# #Εισαγωγή των απαραίτητων βιβλιοθηκών
# import math
# from sklearn.cluster import KMeans 
# import matplotlib.pyplot as plt


# import numpy as np
# import scipy.io

# mat_file = scipy.io.loadmat('xV.mat') # Φόρτωση των δεδομένων απο το αρχείο xV.mat
# xV=np.array(mat_file['xV']) # Δημιουργία πίνακα xV με το σύνολο των δεδομέμων 


# X=xV[:,[296,305]] # Απο τον πίνακα xV χρησιμοποιούμε τα χαρακτηριστικά [296,305]
# k=3 # Ο αριθμός των συστάδων
# numberOfRows, numberOfColumns = X.shape # Ανάθεση τιμών στις μεταβλητες numberOfRows και numberOfcolumns μεσω της συνάρτησης shape

# kmeans=KMeans(n_clusters=k).fit(X) # Εφαρμογή του αλγόριθμο k-means
# IDX=kmeans.labels_ # Eτικέτες κάθε σημείου του Κ-means
# C=kmeans.cluster_centers_ # Συντεταγμένες των κέντρων των συστάδων του Κ-means

# #Εξ ορισμού, ο αλγόριθμος συσταδοποίησης k-means βασίζεται στην Ευκλείδεια απόσταση
# #Παρουσιάζει την κλάση που ανήκει η κάθε παρατήρηση
# plt.plot(X[IDX==0][:,0],X[IDX==0][:,1],'limegreen',marker='o',linewidth=0,label='C1')
# plt.plot(X[IDX==1][:,0],X[IDX==1][:,1],'yellow',marker='o',linewidth=0,label='C2')
# plt.plot(X[IDX==2][:,0],X[IDX==2][:,1],'c.',marker='o',label='C3')
# plt.scatter(C[:,0],C[:,1],marker='x',color='black',s=150 , linewidth=3 , label="Centroids", zorder=10 ) # Γράφημα διασποράς
# plt.legend()
# plt.show()

# sse=0.0 # Αρχικοποίηση του sse
# # Υπολογισμός του sse 
# for i in range(k): # Για κάθε συστάδα
#       for j in range(numberOfRows): # Για κάθε δείγμα 
#         if IDX[j] == i : #Αν το j δείγμα ανήκει στην i συστάδα 
#                 # τότε υπολόγισε το sse μέσω του τύπου του 
#                 sse = sse + math.dist(X[j], C[i])**2
                
# # Εξω απο το for εκτύπωσε το τελικό see            
# print("\n\nsse = %.3f" % sse) 



# #Βήμα 4
# # Εισαγωγή των απαραίτητων βιβλιοθηκών
# import math
# from sklearn.cluster import KMeans 
# import matplotlib.pyplot as plt


# import numpy as np
# import scipy.io

# mat_file = scipy.io.loadmat('xV.mat') # Φόρτωση των δεδομένων απο το αρχείο xV.mat
# xV=np.array(mat_file['xV']) # Δημιουργία πίνακα xV με το σύνολο των δεδομέμων 


# X=xV[:,[467,468]] # Απο τον πίνακα xV χρησιμοποιούμε τα δύο τελευταία χαρακτηριστικά 
# k=3 # Ο αριθμός των συστάδων
# numberOfRows, numberOfColumns = X.shape # Ανάθεση τιμών στις μεταβλητες numberOfRows και numberOfcolumns μεσω της συνάρτησης shape

# kmeans=KMeans(n_clusters=k).fit(X) # Εφαρμογή του αλγόριθμο k-means
# IDX=kmeans.labels_ # Eτικέτες κάθε σημείου του Κ-means
# C=kmeans.cluster_centers_ # Συντεταγμένες των κέντρων των συστάδων του Κ-means

# #Εξ ορισμού, ο αλγόριθμος συσταδοποίησης k-means βασίζεται στην Ευκλείδεια απόσταση
# #Παρουσιάζει την κλάση που ανήκει η κάθε παρατήρηση
# plt.plot(X[IDX==0][:,0],X[IDX==0][:,1],'limegreen',marker='o',linewidth=0,label='C1')
# plt.plot(X[IDX==1][:,0],X[IDX==1][:,1],'yellow',marker='o',linewidth=0,label='C2')
# plt.plot(X[IDX==2][:,0],X[IDX==2][:,1],'c.',marker='o',label='C3')
# plt.scatter(C[:,0],C[:,1],marker='x',color='black',s=150 , linewidth=3 , label="Centroids", zorder=10 ) # Γράφημα διασποράς
# plt.legend()
# plt.show()

# sse=0.0 # Αρχικοποίηση του sse
# # Υπολογισμός του sse 
# for i in range(k): # Για κάθε συστάδα
#       for j in range(numberOfRows): # Για κάθε δείγμα 
#         if IDX[j] == i : #Αν το j δείγμα ανήκει στην i συστάδα 
#                 # τότε υπολόγισε το sse μέσω του τύπου του 
#                 sse = sse + math.dist(X[j], C[i])**2
                
# # Εξω απο το for εκτύπωσε το τελικό see            
# print("\n\nsse = %.3f" % sse) 



# #Βήμα 5
# # Εισαγωγή των απαραίτητων βιβλιοθηκών
# import math
# from sklearn.cluster import KMeans 
# import matplotlib.pyplot as plt


# import numpy as np
# import scipy.io

# mat_file = scipy.io.loadmat('xV.mat') # Φόρτωση των δεδομένων απο το αρχείο xV.mat
# xV=np.array(mat_file['xV']) # Σύνολο των δεδομέμων


# X=xV[:,[205,175]] # Απο τον πίνακα xV χρησιμοποιούμε τα δύο πρώτα χαρακτηριστικά
# k=3 # Ο αριθμός των συστάδων
# numberOfRows, numberOfColumns = X.shape # Μέγεθος του πίνακα Χ

# kmeans=KMeans(n_clusters=k).fit(X) # Εφαρμογή του αλγόριθμο k-means
# IDX=kmeans.labels_ # Eτικέτες κάθε σημείου του Κ-means
# C=kmeans.cluster_centers_ # Συντεταγμένες των κέντρων των συστάδων του Κ-means

# #Εξ ορισμού, ο αλγόριθμος συσταδοποίησης k-means βασίζεται στην Ευκλείδεια απόσταση
# #Παρουσιάζει την κλάση που ανήκει η κάθε παρατήρηση
# plt.plot(X[IDX==0][:,0],X[IDX==0][:,1],'limegreen',marker='o',linewidth=0,label='C1')
# plt.plot(X[IDX==1][:,0],X[IDX==1][:,1],'yellow',marker='o',linewidth=0,label='C2')
# plt.plot(X[IDX==2][:,0],X[IDX==2][:,1],'c.',marker='o',label='C3')
# plt.scatter(C[:,0],C[:,1],marker='x',color='black',s=150 , linewidth=3 , label="Centroids", zorder=10)  #Γράφημα διασποράς
# plt.legend()
# plt.show()

# sse=0.0 # Αρχικοποίηση του sse
# # Υπολογισμός του sse 
# for i in range(k): # Για κάθε συστάδα
#       for j in range(numberOfRows): # Για κάθε δείγμα 
#         if IDX[j] == i : #Αν το j δείγμα ανήκει στην i συστάδα 
#                 # τότε υπολόγισε το sse μέσω του τύπου του 
#                 sse = sse + math.dist(X[j], C[i])**2
                
# # Εξω απο το for εκτύπωσε το τελικό see            
# print("\n\nsse = %.3f" % sse) 
