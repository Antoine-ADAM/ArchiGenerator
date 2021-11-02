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
            jsr     AlphaCount
            movea.l #String2,a0
            jsr     AlphaCount
            illegal
            ; ==============================
            ; Sous-programmes
            ; ==============================
LowerCount  ; ...
UpperCount  ; ...
DigitCount  ; ...
AlphaCount  ; ...
            ; ==============================
            ; Données
            ; ==============================
String1     dc.b    "Cette chaine comporte 46 caracteres alphanumeriques.",0
String2     dc.b    "Celle-ci en comporte 19.",0