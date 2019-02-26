##from urllib.request import urlretrieve
import re 
##urlretrieve ('https://s3.amazonaws.com/tcmg476/http_access_log', 'awslog.txt')

linenum = 0 
##months = ["error", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
log = open("testlog.txt" , "r")

janlog = open("janlog.txt", "w+")
#janlog.close()
feblog = open("feblog.txt", "w+")
#feblog.close()
marlog = open("marlog.txt", "w+")
#marlog.close()
aprlog = open("aprlog.txt", "w+")
#aprlog.close()
maylog = open("maylog.txt", "w+")
#maylog.close()
junlog = open("junlog.txt", "w+")
#junlog.close()
jullog = open("jullog.txt", "w+")
#jullog.close()
auglog = open("auglog.txt", "w+")
#auglog.close()
seplog = open("seplog.txt", "w+")
#seplog.close()
octlog = open("octlog.txt", "w+")
#octlog.close()
novlog = open("novlog.txt", "w+")
#novlog.close()
declog = open("declog.txt", "w+")
#declog.close()
octnum = 0
novnum = 0
decnum = 0
jannum = 0
febnum = 0
marnum = 0
aprnum = 0
maynum = 0
junnum = 0
julnum = 0
augnum = 0
sepnum = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0



## this goes through the lines, prints and counts them. 
for line in log:
    #print (line)
    
    
    if re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Oct\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)
        octnum += 1
        octlog.write(line)
        
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Nov\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)
        novnum += 1
        novlog.write(line)
        
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Dec\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)
        decnum += 1  
        declog.write(line)
        
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Jan\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)
        jannum += 1 
        janlog.write(line)
        
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Feb\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)
        febnum += 1       
        feblog.write(line)
        
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Mar\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)        
        marnum+= 1
        marlog.write(line)
    
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Apr\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)        
        aprnum+= 1
        aprlog.write(line)
    
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/May\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)        
        maynum+= 1
        maylog.write(line)
    
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Jun\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)        
        junnum+= 1
        junlog.write(line)
    
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Jul\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)        
        julnum+= 1
        jullog.write(line)
    
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Aug\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)        
        augnum+= 1
        auglog.write(line)
        
    
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/Sep\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )([0-9]..)( [0-9-]+)"), line):
        #print (line)        
        sepnum+= 1
        seplog.write(line)
        
    if re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/...\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )(3[0-9]+)( [0-9-]+)"), line): 
        cnt3 += 1
            
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/...\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )(4[0-9]+)( [0-9-]+)"), line): 
        cnt4 += 1
            
    elif re.search(("([a-z]+)( - )[a-z.-]+( \[)(..\/...\/[0-9:]+)( [0-9-]+\])( .[a-zA-Z]+ )([a-z0-9.]+)( [a-zA-Z0-9./]+. )(5[0-9]+)( [0-9-]+)"), line): 
        cnt5 += 1        
           
       

    
    ##this answers number 1
    #linenum = linenum + 1
    #print (linenum)
    
print ("oct num =" , octnum)
print ("nov num =" , novnum)
print ("dec num =" , decnum)
print ("jan num =" , jannum)
print ("feb num =" , febnum)
print ("mar num =" , marnum)
print ("apr num =" , aprnum)
print ("may num =" , maynum)
print ("jun num =" , junnum)
print ("jul num =" , julnum)
print ("aug num =" , augnum)
print ("sep num =" , sepnum)

janlog.close()
feblog.close()
marlog.close()
aprlog.close()
maylog.close()
junlog.close()
jullog.close()
auglog.close()
seplog.close()
octlog.close()
novlog.close()
declog.close()

print ("there are ", cnt3, " 3XX errors")
print ("there are ", cnt4, " 4XX errors")
print ("there are ", cnt5, " 5XX errors")