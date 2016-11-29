#https://github.com/Duroktar/cookbook/blob/master/Python/LINKS/Wiki-Search/wikisearch.py

#import os, sys
import time
import wikipedia
"""
try:
    import wikipedia
except ImportError:
    print "Starting initial setup."
    import subprocess
    FNULL = open(os.devnull, 'w')
    retcode = subprocess.call(['pip', 'install', 'wikipedia'], stdout=FNULL, stderr=subprocess.STDOUT)
    import wikipedia
"""  
#query = " ".join(sys.argv[1:])
query=input("Search Wikipedia: ")
print("Searching Wikipedia....Please Be Patient.....")

def main():
    time.sleep(.05)
    result = search_wiki(query)
    print(result)

def search_wiki(text):
    x = wikipedia.search(text)
    y = wikipedia.page(x[0])
    summary = y.summary.replace(';', ',').replace('"', "'").encode('utf-8')
    return summary    
    
if __name__ == '__main__':
    main()
