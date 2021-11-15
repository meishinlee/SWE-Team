<<<<<<< HEAD
LINTER = flake8
API_DIR = API
DB_DIR = db
REQ_DIR = .
PYDOC = python3 -m pydoc -w
TESTFINDER = nose2

export TEST_MODE = 1
# export DEMO_HOME = C:\Users\miche\Desktop\Fall2021\SWE-Team

FORCE:

tests: lint unit

unit: FORCE
	$(TESTFINDER) --with-coverage

lint: FORCE
	$(LINTER) *.py

docs: FORCE
	$(PYDOC) ./*.py
=======
LINTER = flake8
API_DIR = API
DB_DIR = db
REQ_DIR = .
PYDOC = python3 -m pydoc -w
TESTFINDER = nose2

export TEST_MODE = 1
#export DEMO_HOME = "C:\Users\miche\Desktop\Fall2021\SWE-Team"

FORCE:

tests: lint unit

unit: FORCE
	$(TESTFINDER) --with-coverage

lint: FORCE
	$(LINTER) *.py

docs: FORCE
	$(PYDOC) ./*.py
>>>>>>> 86c33112979a40874fcfe91248a4e841106d94ba
	git add ./*.html