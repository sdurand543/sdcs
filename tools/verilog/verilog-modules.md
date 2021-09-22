# Verilog Modules

## Definition

A module is a blueprint for a circuit component. 

Unlike classes \(featured in many other languages\), which describe a collection of attributes and methods, modules describe **relationships** between inputs, outputs, and other modules.

```text
// VERILOG
module and1(a, b, c);
    input a;
    input b;
    output c;
    c = a & b;
endmodule
```

## Syntax

Some key syntactic features of modules:

* Module Declaration
* Module Body

```text
// VERILOG
module <module_name>(<param names>);
    <body>
endmodule
```

## Hierarchy

When building up a system in Verilog, it is a good idea to instantiate a hierarchy of modules. For instance, if we wanted to make a 2-bit and, we might implement it using several 1-bit ands.

```text
// VERILOG
module and2(a, b, c);
    input [1:0] a;
    input [1:0] b;
    output [1:0] c;
    and_1b and1 (.a(a[0]), .b(b[0]), .c(c[0]));
    and_1b and2 (.a(a[1]), .b(b[1]), .c(c[1]));
endmodule
```

