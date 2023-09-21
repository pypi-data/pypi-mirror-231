# Optimization Framework 

This is a framework for linear and non-linear optimization developed by ENACOM Group.

It solves a problem in the form:

```
min  f(x)

s.t. g(x) <= 0
     h(x)  = 0
     x_min <= x <= x_max
```

where `x` is an n-dimensional vector, `f(x)` maps the n-dimensional space to the o-dimensional space,
with `o` being the number of objectives. 
## Prerequisites

What you need to be able to run:

* Python 3.6 +

All requirements are in the file `requirements.txt`.
To install all packages at once: 
```shell
$ pip install -r requirements.txt
```

## Installing science-optimization

Building science-optimization requires the following software installed:

1. Python 3
    - Make sure that distutils is installed before continuing. For example in Debian GNU/Linux, disutils is included in the python3-dev package.
2. PyBind11
    - Note  that this is PyBind11, not PyBind.
3. GNU C Compiler version >= 5.0

To install the package in any environment:

- clone this repo
- `$ pip install ./science-optimization`

## Conventions

### Development

- In Python programming, it is a common practice to initialize "private" methods/attributes with an underscore 
(e.g. _private_method(), _private_attribute). This framework follows this convention

- Attributes sets and gets are implemented using the native 
[`@property`](https://www.programiz.com/python-programming/property) decorator

- An abstract base class inherits from `abc.ABCMeta`

- Google is the default Docstring format

- A package must contain an `__init__.py` file with the package initialization

- PyCharm 2017+ is highly recommended

A detailed explanation of code development can be found [here](https://github.com/LucasSubli/EnacomPythonExample) and 
[here](https://sourcemaking.com/design_patterns).

Tutorials on Python programming can be found 
[here](https://www.digitalocean.com/community/tutorial_series/object-oriented-programming-in-python-3).

### Optimization

Given that `n` is the problem dimension and `m` is the number of points:

- A single point is a `nx1` matrix

- Multiple points are a `nxm` matrix

- Gradient is a `nxm` matrix

- Hessian is a `nxnxm` matrix

## Packages

### Builder

This package is responsible for building an optimization problem. It was built based on the 
[Builder Design Pattern](https://sourcemaking.com/design_patterns/builder) and it has the following classes.

1. `OptimizationProblem()`: the base class of every optimization problem.

    - Attributes:

        * `objective`: `Objective()` instance
    
        * `constraints`: `Contraints()` instance
    
        * `variables`: `Variables()` instance
    
    - Methods:

        * `_build_problem(builder)`: receives a `BuilderOptimizationProblem()` instance, checks problem
    consistency and sets attributes
    
        * `_check_consistency(variables, objectives, constraints)`: receives attributes and check problem
    consistency
    
        * `info()`: prints to user the assembled problem
        
        * `__call__()`: overloaded method that turns an `OptimizationProblem` instance a callable function, that
        evaluates `f, g, h, df, dg, dh, hf, hg, hh` for a given point `x`

2. `BuilderOptimizationProblem()`: abstract class responsible for defining the builder's methods of the 
optimization problem.

    - Abstract methods:
    
        * `build_objectives()`: abstract method responsible for building the problem's objectives
        
        * `build_constraints()`: abstract method responsible for building the problem's constraints
        
        * `build_variables()`: abstract method responsible for building the problem's variables

3. `Objective()`: container class of objectives functions.

    - Attributes:
    
        * `objective_functions`: a list with all functions of the problem. Each function
        is a `FunctionComposite()` instance.
        
    - Methods:
    
        * `C()`: return the matrix C of linear objectives coefficients
        
        * `d()`: return the vector d of linear objectives constants

4. `Contraints()`: container class of constraints functions.

    - Attributes:
    
        * `equality_contraints`: a list with equality constraints functions. Each function
        is a `FunctionComposite()` instance.
        
        * `inequality_contraints`: a list with inequality constraints functions. Each function
        is a `FunctionComposite()` instance.
        
    - Methods:
    
        * `equality_contraints_feasibility(x)`: evaluates the feasibility of `x` on these constraints
        
        * `inequality_contraints_feasibility(x)`: evaluates the feasibility of `x` on these constraints
        
        * `A()`: returns the matrix `A` of linear inequality constraints coefficients
        
        * `b()`: returns the vector `b` of linear inequality constraints bounds
        
        * `Aeq()`: returns the matrix `Aeq` of linear equality constraints coefficients
        
        * `beq()`: returns the vector `beq` of linear equality constraints bounds

5. `Variables()`: container class of the problem variables.

    - Attributes:
        
        * `x_min`: variables' lower bounds
        
        * `x_max`: variables' upper bounds
        
        * `x_type`: list with variables' type ('c': continuous or 'd': discrete)
        

### Function

This package has the definitions of a function. Is was base on the 
[Composite](https://sourcemaking.com/design_patterns/composite) design pattern and 
contains the following classes:

1. `BaseFunction()`: base class of every other class inside this package.

    - Attributes:
    
        * `parameters`: abstract attribute for functions parameters (e.g. coefficients)
        
        * `eps`: precision for numerical calculations
        
    - Methods:
    
        * `eval(x)`: abstract method for the evaluation of `x`
        
        * `gradient(x)`: numerical calculation of the Gradient of `x`
        
        * `hessian(x)`: numerical calculation of the Hessian of `x`
        
        * `dimension()`: function dimension `n`

2. `FunctionsComposite()`: container class of `BaseFunction()`'s children.

    - Attributes:
    
        * `functions`: a list of functions
        
    - Methods:
    
        * `eval(x)`: abstract method for the evaluation of `x` in `functions`
        
        * `gradient(x)`: numerical calculation of the Gradient of `x` in `functions`
        
        * `hessian(x)`: numerical calculation of the Hessian of `x` in `functions`
        
        * `add(f)`: adds function `f` to `functions`
        
        * `remove(idx)`: removes element `functions[idx]`
        
        * `clear()`: removes all functions from list
        
         
3. `LinearFunction()`: implements a function in the form `f(x) = c'x + d`

    - Attributes:
    
        * `parameters`: dictionary with `c` and `d` keys
        
    - Methods:
        
        * `eval(x)`: method for the evaluation of `x`
        
        * `gradient(x)`: analytical calculation of the Gradient of `x`
        
        * `hessian(x)`: analytical calculation of the Hessian of `x`    

4. `QuadraticFunction()`: implements a function in the form `f(x) = x'Qx + c'x + d`

    - Attributes:
    
        * `parameters`: dictionary with `Q`, `c` and `d` keys
        
    - Methods:
        
        * `eval(x)`: method for the evaluation of `x`
        
        * `gradient(x)`: analytical calculation of the Gradient of `x`
        
        * `hessian(x)`: analytical calculation of the Hessian of `x`

5. `PolynomialFunction()`: implements a polynomial function

    - Attributes:
    
        * `parameters`: dictionary with exponents `e` and `c` coefficients
        
    - Methods:
        
        * `eval(x)`: method for the evaluation of `x`
        
        * `gradient(x)`: analytical calculation of the Gradient of `x`
        
        * `hessian(x)`: analytical calculation of the Hessian of `x`

### Problems

This package is responsible for creating the interface of `BuilderOptimizationProblem()` for each optimization problem
instance. The classes must follow the format:

1. `Problem(BuilderOptimizationProblem)`: inherits from BuilderOptimizationProblem

    - Attributes: necessary problem attributes
    
    - Methods:
    
        * `build_objectives()`: concrete method responsible for building the problem's objectives
        
        * `build_constraints()`: concrete method responsible for building the problem's constraints
        
        * `build_variables()`: concrete method responsible for building the problem's variables

The class `Generic(BuilderOptimizationProblem)` builds a generic optimization problem in the canonical
format defined at the beginning of this document. However, it also possible to implement customized 
optimization problems inheriting from `BuilderOptimizationProblem` class, such as `Diet` and `KleeMinty`.

For linear programming, the problem `MIP` is a straightforward abstraction of a problem in the format:

```
    min  c'  @ x
    s.t. A   @ x <= b
         Aeq @ x == beq
         x_min  <= x <=  x_max
```

### Algorithms

This package contains the implementations of the optimization algorithms. It is organized in sub-packages according
to algorithm's families. Each sub-package contains one abstract implementation of the algorithm's family, it is named
`BaseAlgorithmFamily()`

1. `BaseAlgorithms()`: base class for every `BaseAlgorithmFamily()`

    - Attributes:
    
        * `eps`: algorithms' numerical precision
        
    - Methods:
    
        * `optimize()`: abstract method for the implementation core
        
This framework currently supports the following optimization algorithms:

* Cutting-plane family:
    * Ellipsoidal (Multiobjective)

* Decomposition :
    * Nonlinear dual decomposition
    
* Derivative-free :
    * Nelder-Mead simplex (constrained)

* Lagrange (constrained):
    * Augmented lagrangian method (using Quasi Newton)

* Linear programming:
    * Scipy simplex and interior-point
    * GLOP for LP
    * CBC for MIP

* Unidimensional search:
    * Enhanced golden section
    * Multimodal golden section

* Search direction family (unconstrained):
    * Gradient method
    * Modified Newton method
    * Quasi Newton method
    

### Solvers

This package contains the interface to optimization solvers implemented in the framework.

1. `Optimizer()`: optimization for built-in methods, i.e. `algorithms`.

    - Attributes
    
        * `optimization_problem`: `OptimizationProblem()` instance
        
        * `algorithm`: a concrete algorithm implementation instance (e.g. `GradientAlgorithm()`)
        
    - Methods
    
        * `solve`: implements `algorithm.optimize()`

2. `OptimizationResults()`: container for optimization results

    - Attributes
    
        * `x`: the solution of the optimization
        
        * `fx`: function value at solution point
        
        * `sucess`: whether or not the solvers exited successfully
        
        * `message`: description of the cause of termination
        
        * `n_iterations`: number of iterations
        
        * `n_function_evaluations`: number of function evaluations
    
    - Methods
    
        * `info()`: displays optimization results info.

3. `pareto_samplers package`: used to find the pareto border of a multiobjective problem, the implemented
                              sampling strategies are:

    - Lambda sampler
    - Epsilon sampler
    - Nondominated sampler
    - Mu sampler

### Examples

This package contains modules implementing examples of building and solving an optimization problem. It can also
be used for profiling via `@profiling` decorator.

### Profiling

Implementation of the `@profiling` decorator.
