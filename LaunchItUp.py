import os

print("""
       ======== What would you like to launch in super sonic speed? =======

    {1} Wordpress            [at port: 8081]				         
    {2} Drupal               [at port: 5555]
    {3} Joomla               [at port: 8888]
    {4} Your Django web app  [at port: 8000]
    {0} EXIT
        """)

choice = int(input("\nYOUR CHOICE: "))
print("here we go ......... ")
os.system("cd")
if choice==1:
    os.chdir("mycompose")
    os.system("docker-compose up")
elif choice==2:
    os.chdir("drupal-compose")
    os.system("docker-compose up")
elif choice==3:
    os.chdir("joomla-compose")
    os.system("docker-compose up")
elif choice==4:
    os.chdir("django-compose")
    os.system("docker-compose up")
elif choice==0:
    exit()
