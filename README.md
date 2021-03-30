step 1 - Create an environment using below command
        "conda create -n BasicMLops1 python=="3.8"
step 2 - Activate the conda environment using below command
        "conda activate BasicMLops1"      
step 3 - create a requirements.txt in the current directory
step 4 - specify whatever packages need to be installed
step 5 - install the packages in requirements.txt using below command
        "pip install -r requirements.txt"     
step 6 - create a README.md and keep adding steps that you have done till now       
step 7 - run the following command "git init"
step 8 - run the following command "dvc init"
step 9 - run the following command "dvc add data_given/winequality.csv"    
step 10- If you get any error saying "ERROR: unexpected error - DLL load failed while importing win32file: The specified module could not be found."
         Then run the following command "conda install pywin32"
step 11- repeat step 9 after resolving the above issue
step 12- run the following command "git add -A" or "git add . "
step 13- git commit -m "initial commit"        