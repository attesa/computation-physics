import os
a='./'
for root,dis,files in os.walk('./'):
    for file in files:
        print root,file,dis
    
