def count(file):
    word=file.split()
    dict={
    }
    
    for i in word:
        if i in dict:
            dict[i]+=1
            
        else:
            dict[i]=1
            
    return dict        
            
file=introduction = """
Hi, I'm Someshwar Deore.
I am a 2nd-year Information Technology student and a Data Science Enthusiast.
I am learning Python, SQL, Java, Data Structures, and Data Science.
I enjoy improving my programming fundamentals through problem solving and projects.
My goal is to build strong technical skills and become a skilled Data Science professional.
"""

print(introduction)

print(count(file))                