concrete Hilbert of Graftal = {
    lincat N = {a : Str; b : Str} ;
    lincat S = {s : Str} ;

    lin z = {a = ""; b = ""} ;
    lin s x = {a = L ++ x.b ++ F ++ R ++ x.a ++ F ++ x.a ++ R ++ F ++ x.b ++ L; b = R ++ x.a ++ F ++ L ++ x.b ++ F ++ x.b ++ L ++ F ++ x.a ++ R} ;
    lin c x = {s = "ang:90" ++ x.a} ;

    oper L : Str = "l" ;
    oper F : Str = "F" ;
    oper R : Str = "r" ;
}