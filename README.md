
------- INSTALL ENVIRONMENT FOR GRAVITYDESIGNS SERVER (window) ------

----------------------- Installation guide --------------------------

1. Install python-2.7.amd64
2. Install Anaconda2-4.4.0-Windows-x86_64
3. Set PATH in Environment Variables
	
	Right Click This PC > Properties > Advanced system setting > Environment Variables > select PATH > edit
	
	PATH = C:\<installation location>\Anaconda2;C:\<installation location>\Anaconda2\Scripts;C:\<installation location>\Anaconda2\Lib\site-packages;

4. Open Command line and into Clone directory

	pip install django==1.9.5
	pip install notebook==4.2.2
	pip install jupyter-core==4.1.1
	pip install jupyter-client==4.3.0
	pip install django-extensions==1.7.4
	pip install djangorestframework
	pip install numpy
	pip install scikit-learn
	pip install scipy

5. Run Server ( Open Command line and into Clone directory )

	python manage.py migrate
	python manage.py runserver 0.0.0.0:8000

**
	IPServer to use in GravityDesigns Application is IPv4 Address
	( use ipconfig in command line to check IPv4 Address )

----------------------------------------------------------------------"# GravityDesignsServer" 
