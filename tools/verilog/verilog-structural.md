# Verilog Structural

## Netlist

A netlist is a description of the connectivity of an electrical circuit. Netlists are critical components of EDIFs \(Electronic Design Interchange Format\).

## Structural Verilog

Structural Verilog specifies the connectivity of components, rather than the behavior of the circuit itself. Often you will use Structural Verilog to combine components which were designed using Behavioral Verilog.

```c
module xor_gate (out, a, b);
    input a, b;
    output out;
    wire aBar, bBar, t1, t2;
    
    not invA (aBar, a);
    not invB (bBar, b);
    and and1 (t1, a, bBar);
    and and2 (t2, b, aBar);
    or or1 (out t1, t2);
    
endmodule
```

### Structural 'Existence'

Instantiated modules are not "executed". They are always active. They describe hardware state. In the above example, the output `out` is always assigned the value of `a ^ b`, because our `xor_gate` module describes a hardware component that sets out to `a ^ b`.

{% hint style="info" %}
Undeclared variables are assumed to be wires. It is generally seen as bad practice to use undeclared variables.
{% endhint %}

```c
module mux2 (in0, in1, select, out);
    input in0, in1, select;
    output out;
    wire s0, w0, w1;
    
    not (s0, select);
    and (w0, s0, in0), 
        (w1, select, in);
    or (out, w0, w1);
```

Builtins don't need instance names but non-builtins do.

You can also specify names explicitly.

```c
module mux4 (in0, in1, in2, in3, select, out);
    input in0, in1, in2, in3;
    input [1:0] select;
    output out;
    wire w0, w1;

    mux2 
        m0 (.select(select[0]), .in0(in0), .in1(in1), .out(w0)),
        m1 (.select(select[0]), .in0(in2), .in1(in3), .out(w1)),
        m2 (.select(select[1]), .in0(w0), .in1(w1), .out(out))
endmodule
```

It is good practice to pick a specific endianness for all buses. We will use little-endian.

