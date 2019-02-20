concrete Dragon of Graftal = { 
lincat N = {x : Str; y : Str} ; 
--lincat S = {s : Str} ; 
 
lin z = {x = ""; y = ""} ; 
lin s x = {x = x.x ++ R ++ x.y ++ F ++ R; y = L ++ F ++ x.x ++ L ++ x.y} ; 
--lin c x = {s = "newpath 300 550 moveto" ++ F ++ x.x ++ "stroke showpage"} ; 
 
oper F : Str = "t.forward(20)" ; 
oper L : Str = "t.right(90)" ; 
oper R : Str = "t.left(90)" ; 
}