concrete Sierpinski of Graftal = open Operations in {
    lincat N = {a : Str; b : Str} ;
    lincat S = {s : Str} ;

    lin z = {a = F; b = F} ;
    lin s x = {a = x.b ++ L ++ x.a ++ L ++ x.b; b = x.a ++ R ++ x.b ++ R ++ x.a} ;
    lin c x = {s = "ang:60" ++ "kids:3" ++ x.a} ;

}