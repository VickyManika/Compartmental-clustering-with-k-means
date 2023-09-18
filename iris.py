# #Μέσα στον κώδικα ακολοθούνται τα βήματα της εργασίας.

# #Βήμα 1
# from sklearn.datasets import load_iris
# means=load_iris().data # Φόρτωση των δεδομένων iris

# #Βήμα 2 
# from sklearn.cluster import KMeans
# X = means[:, [2,3]] # Eπιλογή των δύο τελευταίων διαστασεων του πίνακα
# k = 3 # Τα δεδομένα θα οργανωθούν σε 3 συστάδες
# kmeans = KMeans(n_clusters=k).fit(X) #Εφαρμογή του αλγόριθμου k-means
# IDX = kmeans.labels_  # Eτικέτες κάθε σημείου του Κ-means
# C = kmeans.cluster_centers_  #Συντεταγμένες των κέντρων των συστάδων του Κ-means
# #Εξ ορισμού, ο αλγόριθμος συσταδοποίησης k-means βασίζεται στην Ευκλείδεια απόσταση

# #Βήμα 3 
# import matplotlib.pyplot as plt 
# plt.figure(1)
# #Παρουσιάζει την κλάση που ανήκει η κάθε παρατήρηση 
# plt.plot(X[IDX==0][:,0],X[IDX==0][:,1],'limegreen',marker='o',linewidth=0,label='C1')
# plt.plot(X[IDX==1][:,0],X[IDX==1][:,1],'yellow',marker='o',linewidth=0,label='C2')
# plt.plot(X[IDX==2][:,0],X[IDX==2][:,1],'c.',marker='o',label='C3')
# plt.scatter(C[:,0],C[:,1],marker='x',color='black',s=150 , linewidth=3 , label="Centroids", zorder=10 ) #Γράφημα διασποράς
# plt.legend() 
# plt.show()



#Βήμα 4
# Ενσωμάτωση των απαραίτητων βιβλιοθηκών
import math
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt 
means=load_iris().data

X = means[:,[0,3]] # Επιλογή διαστάσεων του πίνακα Χ  
numberOfRows, numberOfColumns = X.shape # Ανάθεση τιμών στις μεταβλητες numberOfRows και numberOfcolumns μεσω της συνάρτησης shape 
print('Size of the dataset: ', end="") # Eκτύπωση του μεγέθους του dataset
print(numberOfRows) 

k_val=[] # Αρχικοποίηση λίστας k_val
sse_val=[] # Aρχικοποίηση λίστας sse_val

for k in range(2,11) : # oπου k o αριθμός των συστάδων και παίρνει τιμές απο 2 μέρχρι 10
        kmeans = KMeans(n_clusters=k).fit(X) #Εφαρμογή του αλγόριθμου k-means
        IDX = kmeans.labels_  #Eτικέτες κάθε σημείου του Κ-means
        C = kmeans.cluster_centers_  #Συντεταγμένες των κέντρων των συστάδων του Κ-means
        
        #Εξ ορισμού, ο αλγόριθμος συσταδοποίησης k-means βασίζεται στην Ευκλείδεια απόσταση
        print("\n\nk= %.0f" %k) # Εκτυπώνει τον αριθμό των συτάδων χωρίς δεκαδικά ψηφία
        sse = 0.0 # Αρχικοποίηση του SSE
       
        for i in range(k): # Για κάθε συστάδα 
            # Παρουσίασε την κλαση που ανήκει η κάθε παρατήρηση 
            plt.plot(X[IDX==i][:,0], X[IDX==i][:,1], marker='o', linewidth=0, label = i+1)
            for j in range(numberOfRows): # Για κάθε παρατήρηση
              if IDX[j] == i :#Αν η j παρατήρηση ανήκει στην i συστάδα 
                      # τότε υπολόγισε το sse μέσω του τύπου του
                  sse = sse + math.dist(X[j], C[i])**2
        # Δίαγραμμα διασποράς          
        plt.scatter(C[:,0], C[:,1], marker='x', color='black', s=100, linewidth=1, label="Centroids", zorder=10)
        plt.legend()
        plt.show()        

        
        print("\n\nsse = %.3f" % sse) # Εκτύπωση του sse
        # Υπολογισμός και εμφάνιση σιλουέτας
        if k < numberOfRows:
              print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, IDX))
              
        #Γέμισμα των λιστών με χρήση της συνάρτησης append     
        k_val.append(k)
        sse_val.append(sse)
        
# Παρουσίαση της γραφικής παράστασης του k-SSE        
plt.plot(k_val,sse_val)
plt.title("Plot k-SSE") # Τίτλος γραφήματος
plt.xlabel('k') # Τίτλος του άξονα x
plt.ylabel('SSE') # Τίτλος του άξονα y
plt.show() 

print("\n\nΤέλος προγράμματος")
       





