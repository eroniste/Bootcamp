//  #1.1: inside the funcOne function 3 (let allows reassignment)
// #1.2: Error (const prevents reassignment of a = 3).
// #2.1:
// First funcThree(): inside the funcThree function 0 (global a).
// After funcTwo(): a becomes 5 (global reassignment).
// Second funcThree(): inside the funcThree function 5.
// #2.2: Error (const prevents global reassignment in funcTwo()).
// #3.1: inside the funcFive function hello (window.a sets global variable).
// #4.1: inside the funcSix function test (local a shadows global a).
// #4.2: Same result (const behaves like let here; no reassignment occurs).
// #5.1:
// in the if block 5 (block-scoped a).
// outside of the if block 2 (global a).
// #5.2: Same result (block-scoped const works identically here).