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

### Installation
Package can be installed by running the following command:
```
pip install CalculatorPackageTuringRokasSertvytis==1.1
```

Package could also be imported more elegantly by just running the following command in the command line
`pip install git+https://github.com/TuringCollegeSubmissions/rsertv-DWWP.1#egg=Calculator`
,but since the project is currently in a private GitHub directory, this method will not work.

### How to use
After successfully importing the package to the project, a `Calculator()` object must be created by running the following command:
`calculator = Calculator()`.
Now to use the calculator user can run the aforementioned commands as such:
```
calculator.add(5)  # OUTPUT: 0 + 5 = 5  
calculator.subtract(2) #OUTPUT: 5 - 2 = 3  
calculator.multiply(9) #OUTPUT: 3 * 9 = 27  
calculator.divide(3)   #OUTPUT: 27 / 3 = 9  
calculator.nRoot(2)    #OUTPUT: 9 ^ (1/2) = 3  
calculator.reset()     #OUTPUT: Memory cleared
```

### Tests
Package also includes tests which are located inside tests/calculator_test.py. One of the ways to run the test is to simply run `calculator_test.py` from command line when inside the test directory.
