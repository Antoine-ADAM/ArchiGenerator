            ; ==============================
            ; Initialisation des vecteurs
            ; ==============================
            org     $4
vector_001  dc.l    Main
            ; ==============================
            ; Programme principal
            ; ==============================
            org     $500
Main        movea.l #String1,a0
            jsr     LowerCount
            movea.l #String2,a0
            jsr     LowerCount
            illegal
            ; ==============================
            ; Sous-programmes
            ; ==============================
LowerCount  ; ...
            ; ...
            ; ...
            ; ==============================
            ; Données
            ; ==============================
String1     dc.b    "Cette chaine comporte 28 minuscules.",0
String2     dc.b    "Celle-ci en comporte 16.",0