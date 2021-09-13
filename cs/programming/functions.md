# Functions

## Definition

A mathematical function is a map from any object in type-space $$X$$ to a single object in type-space $$Y$$.

$$
f : X \rightarrow Y
$$

```cpp
// C++

template <typename X, typename Y>

Y function(X input) {
    // function body
}
```

## Transformations

A transformation is a subset of functions, describing one that maps any object in type-space $$T$$ to another object in $$T$$.

$$
t : T \rightarrow T
$$

```cpp
// C++

template <typename T>
  
T transformation(T input)
{
    // function body
}
```

## Terminology

### Onto

A function $$f : X \rightarrow Y$$ is considered **onto** iff:

$$
\forall y \in Y, \ 
\exists \tilde{x} \in X \ \ s.t. \ \ f(\tilde{x}) = y
$$

&lt;-- include graphic here

Under Development

## Programming

In programming, functions are defined by their 'callability' \(ability to be executed\), rather than deterministic mapping. Languages which do not support state mutation are known as 'purely functional', and force the mathematical / mapping definition of functions.

Because function syntax varies significantly in different languages, we will narrow our discussion to Python.

In Python, function definitions are composed of:

1. Function Name: the identifier / variable name that can be used to refer to the function
2. Parameters: the ordered identifiers / variable names that can be used in the function body to refer to the arguments
3. Function Body: the code that will execute when the function is called \(in the below example, the body is empty, so the `pass` keyword is provided instead\)

```python
def function_name(param_1_name, param_2_name, param_3_name):
    pass
```

To call a function definition, you provide the function reference along with its arguments in parentheses.

1. Function Reference: the language reference to the called function
2. Arguments: the ordered **values** that will be used in place of the parameters in the environment function body

```python
function_name(value_1, value_2, value_3)
```

## Pass By Value

Under Development

