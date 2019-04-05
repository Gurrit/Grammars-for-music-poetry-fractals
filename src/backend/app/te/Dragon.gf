concrete Dragon of Graftal = { 
lincat N = {x : Str; y : Str} ; 
lincat S = {s : Str} ; 
 
lin z = {x = ""; y = ""} ; 
lin s x = {x = x.x ++ L ++ x.y ++ F ++ L; y = R ++ F ++ x.x ++ R ++ x.y} ; 
lin c x = {s = "ang:90" ++ "kids:2" ++ F ++ x.x } ; 
 
oper F : Str = "F" ; 
oper R : Str = "r" ; 
oper L : Str = "l" ; 
}