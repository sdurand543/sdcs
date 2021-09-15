# Verilog Assignment

```c
wire [3:0] A, X, Y, R, Z;
wire [7:0] P;
wire r, a, cout, cin;
```

Assignments:

```c
assign R = X | (Y & ~Z); // bit-wise bool op
assign r = &X; // reduction op
assign R = (a == 1'b0) ? X : Y; // conditional op
assign P = 8'hff; // constant
assign P = X * Y; // arithmetic op
assign P[7:0] = {4{X[3]]}, X[3:0]}; // sign ext
assign {cout, R} = X.

--todo finish
```

## Non-Continuous Assignment:

`reg` type can 'hold' values. LHS of signals assigned within 'always' statement

`wire` type cannot 'hold' a value and must be driven. Represents connection. LHS of signals assigned outside 'always' statements \(continuous assignment\)

```c
module and_or_gate (out, in1, in2, in3);
    input in1, inn2, in3;
    output out;
    reg out;
    
    // V sensitivity list
    // only evaluate if one of these changes
    always @(in1 or in2 or in3) begin
        out = (in1 & in2) | in3;
    end
    
    // begin-end structure not needed for single line or block
    
    // ^ this example is the same as continuous
    
endmodule
        
```

{% hint style="info" %}
A `reg` type in verilog is not always a register, just a verilog idiosyncracy.
{% endhint %}

```c
module mux4 (in0, in1, in2, in3, select, out);
    input in0, in1, in2, in3;
    input [1:0] select;
    output out;
    reg out;
    
    always @(in0 in1 in2 in3 select)
    case (select)    // case keyword acts like switch
        2'b00: out = in0;
        2'b01: out = in1;
        2'b10: out = in2;
        2'b11: out = in3;
    endcase
endmodule
```

```c
always @ (in0 in1 in2 in3 select)
if (select == 2'b00) out = in0;
    else if (select == 2'b01) out = in1;
        else if (select == 2'b10) out = in2;
            else out = in3;
```

{% hint style="info" %}
Nested `if` structure leads to 'priority logic'. The `case` keyword avoids this.
{% endhint %}

Go over the difference between = and &lt;=.

