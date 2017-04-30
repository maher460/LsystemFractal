LsystemFractal
Project for Looking at Shapes

Looking at Shapes
Project: Making Fractals based on an L system
Author: Maher Khan 

  Examples:

    Triad clash of quads (by Maher Khan)
    Axiom: "F+F--F+F+F"
    Rule: "F-F-F-F"
    Number of Iterations: 3
    Angle: 100
    Length: 50
   
    or run:
    main.py "F+F--F+F+F" "F-F-F-F" 3 100 50


    Tiled Square (by Maher Khan)
    Axiom: "F+F--F+F"
    Rule: "F-F-F-F"
    Number of Iterations: 3
    Angle: 90
    Length: 10
    
    or run
    main.py "F+F--F+F+F" "F-F-F-F" 3 90 10

    
    Another Example:
    Axiom: "F-F+F+FF-F-F+F"
    Rule: "F-F-F-F"
    Number of Iterations: 3
    Angle: 90
    Length: 10
    
    or run
    main.py "F-F+F+FF-F-F+F" "F-F-F-F" 3 90 10

    
    Koch Curve:
    Axiom: "F+F--F+F"
    Rule: "F-F-F-F-F-F"
    Number of Iterations: 3
    Angle: 60
    Length: 4
    
    or run
    main.py "F+F--F+F" "F-F-F-F-F-F" 3 60 4
    
    
    Tree:
    Axiom: "F[-F]F[+F]F"
    Rule: "F"
    Number of Iterations: 3
    Angle: 60
    Length: 10
    
    or run
    main.py "F[-F]F[+F]F" "F" 3 60 10
