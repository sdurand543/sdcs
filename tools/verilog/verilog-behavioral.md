# Verilog Behavioral





```c
module foo (out, in1, in2);
    input in1, in2;
    output out;

    // assign statement is similar to a logical 'connection' 
    // this is a 'continuous' assignment    
    assign out = in1 & in2;
        
endmodule
```

^ eplicit instantation of bit-wise "and" gate



```c
module FullAdder (a, b, ci, r, co);
    input a, b, ci;
    output r, co;
    
    assign r = a ^ b ^ ci;
    assign co = a&ci | a&b | b&cin;
endmodule
```



```c
module Adder (A, B, R);
    input [3:0] A;
    input [3:0] B;
    output [4:0] R;
    
    wire c1, c2, c3;
    
    FullAdder
    add0(),
    add1(),
    add2(),
    add3()
    --- todo fill-in
endmodule
```

