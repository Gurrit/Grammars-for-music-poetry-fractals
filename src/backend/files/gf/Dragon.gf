concrete Dragon of Graftal = open Operations in {
    lincat N = {a : Str; b : Str} ;
    lincat S = {s : Str} ;

    lin z = {a = ""; b = ""} ;
    lin s x = {a = x.a ++ L ++ x.b ++ F ++ L; b = R ++ F ++ x.a ++ R ++ x.b} ;
    lin c x = {s = "ang:90" ++ F ++ x.a } ;
}