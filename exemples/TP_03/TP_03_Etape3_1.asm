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
            jsr     SpaceCount
            movea.l #String2,a0
            jsr     SpaceCount
            illegal
            ; ==============================
            ; Sous-programmes
            ; ==============================
SpaceCount  movem.l d1/a0,-(a7)     ; Sauvegarde les registres dans la pile.
            clr.l   d0
\loop       move.b  (a0)+,d1
            beq     \quit
            cmp.b   #' ',d1
            bne     \loop
            addq.l  #1,d0
            bra     \loop
            
\quit       movem.l   (a7)+,d1/a0   ; Restaure les registres.
            rts
            ; ==============================
            ; Données
            ; ==============================
String1     dc.b    "Cette chaine comporte 4 espaces.",0
String2     dc.b    "Celle-ci en comporte 3.",0