concrete Sierpinski of Graftal = {
    lincat N = {a : Str; b : Str} ;
    lincat S = {s : Str} ;

    lin z = {a = A; b = B} ;
    lin s x = {a = x.b ++ L ++ x.a ++ L ++ x.b; b = x.a ++ R ++ x.b ++ R ++ x.a} ;
    lin c x = {s = "ang:60" ++ "kids:3" ++ x.a} ;

    oper A : Str = "A" ;
    oper B : Str = "B" ;
    oper R : Str = "r" ;
    oper L : Str = "l" ;
}