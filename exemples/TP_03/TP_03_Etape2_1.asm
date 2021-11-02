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
            jsr     StrLen
            movea.l #String2,a0
            jsr     StrLen
            illegal
            ; ==============================
            ; Sous-programmes
            ; ==============================
StrLen      move.l   a0,-(a7)       ; Sauvegarde le registre A0 dans la pile.
            clr.l   d0
\loop       tst.b   (a0)+
            beq     \quit
            addq.l  #1,d0
            bra     \loop
\quit       movea.l  (a7)+,a0       ; Restaure la valeur du registre A0.
            rts
            ; ==============================
            ; Données
            ; ==============================
String1     dc.b    "Cette chaine comporte 36 caracteres.",0
String2     dc.b    "Celle-ci en comporte 24.",0