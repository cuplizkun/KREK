import os
if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("exploid").login_kamu()
   except Exception as e:
       exit(str(e))
