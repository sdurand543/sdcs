# Verilog Structural

## Netlist

a netlist is a description of the connectivity of an electrical circuit

EDIF \(Electronic Design Interchange Format\)

```c
module xor_gate (out, a, b);
    input a, b;
    output out;
    wire aBar, bBar, t1, t2;
    
    // body (contains instances of lower)
    not invA (aBar, a);
    not invB (bBar, b);
    and and1 (t1, a, bBar);
    and and2 (t2, b, aBar);
    or or1 (out t1, t2);
    
endmodule
```

Instantiated gates are not "executed". They are always active. A description of hardware state.

^ this is a useless example because xor gate made from other primitives.

{% hint style="info" %}
\*\* undeclared variables are assumed to be wires. don't use undeclared variables.
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

{% hint style="info" %}
builtins don't need instance names \(they would then share the 'master name', but non-builtins definitely do.
{% endhint %}

You can specify names explicitly.

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

{% hint style="info" %}
pick little-endian
{% endhint %}

1-off indices and mixed endianness is biggest cause of bugs.

