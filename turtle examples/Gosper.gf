concrete Gosper of Graftal = {
    lincat N = {a : Str; b : Str} ;
    lincat S = {s : Str} ; 

    lin z = {a = A; b = B} ;
    lin s x = {a = x.a ++ L ++ x.b ++ L ++ L ++ x.b ++ R ++ x.a ++ R ++ R ++ x.a ++ x.a ++ R ++ x.b ++ L; 
    b = R ++ x.a ++ L ++ x.b ++ x.b ++ L ++ L ++ x.b ++ L ++ x.a ++ R ++ R ++ x.a ++ R ++ x.b} ;
    lin c x = {s = "ang:60" ++ "kids:7" ++ x.a} ;

    oper A : Str = "F" ;
    oper B : Str = "F" ;
    oper R : Str = "r" ;
    oper L : Str = "l" ;
}