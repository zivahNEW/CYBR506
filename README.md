# CYBR506
STEP 1:
-	In your computer, navigate to folder where you have the freeradius folder downloaded and copy the folder’s path. 
STEP 2:
-	In your system, open a cmd terminal window and use the appropriate commands (example below) to navigate to the freeradius directory and begin the image and container build process:

cd C:\User\Name\Documents\freeradius
STEP 3:
-	In cmd terminal, build the freeradius image:

docker build . -t name_of_image --no-cache 

STEP 4:
-	In cmd terminal, build the freeradius container:
docker run -d --name name_of_container -p 1812:1812/udp -p 1813:1813/udp nameofimage_youvejustbuilt

-	Note: if the command doesn’t work, check if anything is running on those ports using the command below and then try building the container again. Docker may have already registered the container name you’d chosen above, so if you encounter another error, try looking for and deleting the container in the Docker app or use a new name for your container. 
docker ps

STEP 5:
-	In your computer, navigate to folder where you have the flaskapp folder downloaded and copy the folder’s path. 
STEP 6:
-	In your system, open a cmd terminal window and use the appropriate commands (example below) to navigate to the flaskapp directory and begin the image and container build process:

docker build . -t name_of_image --no-cache 

STEP 7:
-	In cmd terminal, build the flaskapp container:

docker run -d --name nameof_flaskapp_container -p 5000:5000 nameof_flaskapp_image_youvejustbuilt

-	Note: if it doesn’t work, check if anything is running on those ports using the command below and then follow the directions from “STEP 4’s Note”
docker ps

STEP 8:
-	Now that you’ve built both images and containers, go to the Docker app and stop all running containers. 
-	In your system’s cmd terminal run the following command to ensure no containers are running:
docker ps
-	If results indicate containers are still running, stop them in Docker or run the following command to stop them:
docker stop name_of_running_container

STEP 9:
-	The following instructions are for those who wish to change the username & password, and the radius server secret. Those attempting to simply test the project can skip to STEP 10

STEP 9.1: TO CHANGE USERNAME & PASSWORD
-	In the Docker app, navigate to your freeradius container. Go to Files TAB and look for the following folders:
o	freeradius/mods-config/files/authorize
-	Double click on the authorize file to see its contents and modify the username and password values to whatever you wish. 
-	Save using the floppy disk icon on the right-hand side. 
-	Keep a mental note of your new username and password values. You will need them later!
  
STEP 9.2: TO CHANGE THE RADIUS SECRET:
-	This Step must be done 2x, once in the freeradius container and once in the flaskapp container.
		STEP 9.2.1
-	In the Docker app, navigate to your freeradius container. Go to Files TAB and navigate to: 
o	freeradius/clients.config
-	Double click on the clients.config file to see its contents and modify the secret value to whatever you wish. 
-	Save using the floppy disk icon on the right-hand side. 
-	Keep a mental note of your new secret. You will now input your new secret value in the flaskapp container.
STEP 9.2.2
-	In the Docker app, navigate to your flaskapp container. Go to Files TAB and navigate to:
o	App/app.py
-	Double click on the app.py file to see its contents and modify the RADIUS_SECRET value to the same secret value you used above in STEP 9.2.1 
-	Save using the floppy disk icon on the right-hand side. 
STEP 10:
-	Run or START your freeradius container. From Docker simply click on the container’s Play button or from your computer’s cmd terminal input:
docker start name_of_freeradius_container

-	Run or START your flaskapp container. From Docker simply click on the container’s Play button or from your computer’s cmd terminal input:
docker start name_of_flaskapp_container

STEP 11:
	STEP 11.1: CHECK FREERADIUS IP ADDRESS:

-	Check to see if the IP address assigned to your freeradius container matches the one that has been pre-assigned in the flaskapp container (in the app.py file). In your computer’s cmd terminal input:
Docker inspect name_of_freeradius_container

-	The assigned IP address should be "172.17.0.2” but make note of whichever IP address you do find. 
STEP 11.2: CHECK FLASKAPP IP ADDRESS AND MODIFY IF NECESSARY:
-	In the Docker app, navigate to your flaskapp container. Go to Files TAB and navigate to:
o	app/app.py
-	Double click on the app.py file to see its contents. The IP address listed in RADIUS_SERVER should match the IP address that has been assigned to your running freeradius container, the address that you just took note of above in STEP 11.1. 
-	If the values don’t match, modify the RADIUS_SERVER IP address in app.py
-	Save using the floppy disk icon on the right-hand side.

STEP 12:
-	On your computer, open a new web browser window and navigate to:
http://127.0.0.1:5000
STEP 12.1: FOLLOW IF YOU ARE TESTING MAY’s LAB:
-	In the boxes shown below, type in the May’s username and password:
-	 
-	Username: may
-	Password: ewdavid
-	If successful, you should see the following screen:
 

STEP 12.2: FOLLOW IF YOU ARE TESTING YOUR OWN LAB AND HAVE MODIFIED USERNAME AND PASSSWORD:
-	In the boxes shown below, type in the username and password you created in STEP 9.1

 
-	If successful, you should see the message “Welcome, your_username!”




HANDY TRICKS:
In Docker,  inside of your freeradius container, if you navigate to the terminal tab you can easily double check your assigned username, password, and secret. Input:
Cd etc/raddb-----------> to navigate to correct directory
Cat users -----------> to look for instances of the values username and password
Cat cliets.config -----------> to look through the file and check the secret value

