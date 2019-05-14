concrete Koch of Graftal = { 
lincat N = {f : Str} ; 
lincat S = {s : Str} ;
 
lin z = {f = F} ; 
lin s x = {f = x.f ++ R ++ x.f ++ L ++ x.f ++ L ++ x.f ++ R ++ x.f} ; 
lin c x = {s = "ang:90" ++ x.f ++ R ++ x.f ++ R ++ x.f ++ R ++ x.f} ;
 
oper F : Str = "F" ; 
oper R : Str = "r" ; 
oper L : Str = "l" ; 
}