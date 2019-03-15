concrete Cantor of Graftal = {
    lincat N = {f : Str; g : Str} ;

    lin z = {f = F; g = G} ;
    lin s x = {f = x.f ++ x.g ++ x.f; g = x.g ++ x.g ++ x.g} ;

    oper F : Str = "t.forward(10)" ;
    oper G : Str = "t.penup() t.forward(10) t.pendown()" ;
}