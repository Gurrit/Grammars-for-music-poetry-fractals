--
-- "The L-system is a grammar formalism which is used to describe
-- graftals (recursive graphical objects). It is an interesting 
-- coincidence that every L-System grammar could be redefined 
-- as PMCFG grammar. This demo shows how to generate graftals 
-- using GF. The output from every concrete syntax is a string 
-- to be read in Python. 

abstract Graftal = {
    flags startcat = N;
    cat N; S;
    fun z : N ;
        s : N -> N ;
        c : N -> S ;
}