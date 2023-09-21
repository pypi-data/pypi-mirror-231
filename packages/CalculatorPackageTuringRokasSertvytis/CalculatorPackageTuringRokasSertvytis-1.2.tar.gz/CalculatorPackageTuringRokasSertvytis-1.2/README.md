## CalclculatorPackage

### Description
'Calculator' is a simple python package that allows users to perform the most basic arithmetic functions.

### Available functions:
- Addition (`.add(n)`)
- Subtraction (`.subtract(n)`)
- Multiplication (`.multiply(n)`)
- Division (`.divide(n)`)
- N Root (`.n_root(n)`)
- Reset memory (`.reset()`)

### Prerequisites
- Python
- Git

### Installation and test run
Package can be installed and tested in the following way:
##### 1. Create a Virtual Environment
Open your Command Prompt (CMD) and execute:
```
python -m venv {environment_name}
```
Replace `{environment_name}` with the desired name for your virtual environment.
##### 2. Activate the Virtual Environment
In CMD, type:
```
{environment_name}\Scripts\activate
```
##### 3. Install the package
With the virtual environment active, install the package using pip:
```
pip install CalculatorPackageTuringRokasSertvytis==1.2
```
##### 4. Navigate to your .py script directory
Change your directory to where your Python script (that will use the package) is located:
```
cd {PATH_TO_PYTHON_SCRIPT_DIRECTORY}
```
Replace `{PATH_TO_PYTHON_SCRIPT_DIRECTORY}` with the path to your script.
##### 5. Import package to the script (in .py file)
```
from calculator import Calculator
```
##### 6. Create Calculator object (in .py file)
```
{calculator_variable_name} = calculator.Calculator()
```
Replace `{calculator_variable_name}` with a suitable variable name.
##### 7. Use Calculator Functions (in .py file)
As an example, you can add numbers like so:
```
{calculator_variable_name}.add(2)
```
##### 8. Run the script from Command Prompt (CMD)
```
python {python_script_name}.py
```
Replace `{python_script_name}` with the name of your Python script.


Package could also be imported more elegantly by just running the following command in the command line
`pip install git+https://github.com/TuringCollegeSubmissions/rsertv-DWWP.1#egg=Calculator`
,but since the project is currently in a private GitHub directory, this method will not work.

### Function tests
Here are the expected results of each function:
```
calculator.add(5)      #OUTPUT: 0 + 5 = 5  
calculator.subtract(2) #OUTPUT: 5 - 2 = 3  
calculator.multiply(9) #OUTPUT: 3 * 9 = 27  
calculator.divide(3)   #OUTPUT: 27 / 3 = 9  
calculator.nRoot(2)    #OUTPUT: 9 ^ (1/2) = 3  
calculator.reset()     #OUTPUT: Memory cleared
```

### Tests
Package also includes tests which are located inside tests/calculator_test.py. One of the ways to run the test is to simply run `calculator_test.py` from command line when inside the test directory.
