# Verilog Generators

Used for designing general, synthesizable designs.

```c
module Adder (A, B, R);
    parameter N = 4;
    input [N-1:0] A;
    input [N-1:0] B;
    output [N:0] R;
    wire [N:0] C;
    
    genvar i;
    generate
        for (i = 0; i < N; i = i + 1) begin:bit
            FullAdder add(.a(A[i], .b(B[i]), .ci(C[i]), .co(C[i+1]), .r(R[i]))
        end
    endgenerate
    
    assign C[0] = 1'b0;
    assign R[N] = C[N];
endmodule
```

```c
module gray2bin1 (bin, gray);
    parameter SIZE = 0;
    output [SIZE-1:0] bin;
    input [SIZE-1:0] gray;
    
    genvar i;
    generate for (i = 0; i < SIZE; i = i + 1) begin:bit
        assign bin[i] = ^gray[SIZE-1:i];
    end endgenerate
endmodule
```

