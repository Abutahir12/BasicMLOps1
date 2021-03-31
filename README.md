step 1 - Create an environment using below command
            "conda create -n BasicMLops1 python=="3.8"

step 2 - Activate the conda environment using below command
            "conda activate BasicMLops1"      

step 3 - create a requirements.txt in the current directory

step 4 - specify whatever packages need to be installed

step 5 - install the packages in requirements.txt using below command
            "pip install -r requirements.txt"     

step 6 - create a README.md and keep adding steps that you have done till now       

step 7 - run the following command 
            "git init"

step 8 - run the following command 
            "dvc init"

step 9 - run the following command 
            "dvc add data_given/winequality.csv"    

step 10- If you get any error saying "ERROR: unexpected error - DLL load failed while importing win32file: The specified module could not be found."
         Then run the following command 
            "conda install pywin32"

step 11- repeat step 9 after resolving the above issue

step 12- run the following command 
            "git add -A" or "git add . "

step 13- run the following command 
            git commit -m "initial commit" or "git add . && git commit -m "initial commit"

step 14- run the following command 
            "git remote add origin <YOUR_GIT_REPOSITORY URL>"

step 15- run the following command 
            "git branch -M main"

step 16- run the following command 
            "git push origin main"

step 17- run the following command after you have added some code to project
            "dvc repro"     

step 18- run the following command for test cases 
        (you need to install tox and pytest and configure the 
         necessary files before running the below commands)
            "tox" or "pytest -v"

step 19- setup commands "pip install -e . " to install packages in current directory like setup.py
                               
step 20- Commands to build your own tar file and wheel file for created package
            "python setup.py sdist bdist_wheel"
            