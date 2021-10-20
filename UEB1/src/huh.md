*Formatiert in Markdown*

# Aufgabe 5 - `huh`

## **1.** Verhalten von `int huh(int x)`:
> Durch einige Versuche im Interpreter wird schnell klar, dass `huh(int x)` nicht proportional zur Größe von `x` ist.
Sobald man auf die Bit-Darstellung von `x` achtet, stellt man fest, dass die Anzahl von mit `1` gesetzten Bits in `x` mit dem Ergebnis von `huh(x)` übereinstimmt:
```c
--> huh(15);  // ...001111
4 (int)
--> huh(16)); // ...010000
1 (int)
--> huh(32)); // ...100000
1 (int)
--> huh(3));  // ...000011
2 (int)
--> huh(1));  // ...000001
1 (int)
--> huh(0));  // ...000000
0 (int)
```
Somit gibt `huh(x)` die Anzahl von (mit `1`) gesetzten Bits in `x` zurück.
Hier noch einmal Tabellarisch dargestellt:
| `x`       | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    |
|-----------|------|------|------|------|------|------|------|------|------|
| `bits(x)` | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 |
| `huh(x)`  | 0    | 1    | 1    | 2    | 1    | 2    | 2    | 3    | 1    |



## **2.** Wie macht `huh` das? 
```c
int huh(int x) {
  // Zählervariable `c` wird mit `0` initialisiert;
  int c = 0;

  // Whileschleife mit Bedingung `x != 0`.
  while (x != 0) {
    // Inkrement (c)
    c = c + 1;
    // Hier wird´s interessant (*):
    x = x & x - 1;
  }
  // Gebe die Anzahl von Wiederholungen der while-Schleife zurück
  return c;
}
```
> Zuerst wird eine Zählervariable `int c` mit `0` initialisiert.
> Danach wird eine `while`-Schleife mit der Bedingung `x != 0` betreten. Innerhalb dieser wird mit jeder Wiederholung `c` um `1` inkrementiert und ein Statement *(\*)*, auf das ich noch genauer eingehe ausgeführt.
> Nach Verlassen der Schleife endet die Funktion und gibt als Rückgabewert die Zählervariable `c` zurück.
> 
> *(\*)* Schauen wir uns mal den Vorgang in Zeile 6 *(auf AB)* für ein beliebiges `x` an: <br/>
> Nach `while`-Bedingung: `x != 0`!
> ```c
> bits(x)               = "...1{n mal 0}" // n Element von Natürliche Zahlen
> => bits(x-1)          = "...0{n mal 1}"
> => bits(x & (x-1))    = "...0{n mal 0}"
> ```
> Somit wird mit `x = x & (x-1)` die erste `1` von rechts aus *(in der Bitdarstellung)* aus entfernt.
>
> Beispiel:
> ```c
> int x = 37;
> int c = 0;
> // bits(x) = "100101"
> x = x & (x-1);
> /*     100101
>  * AND 100100
>  *   = 100100
>  */
> c = c + 1;
> // bits(x) = "100100"
> x = x & (x-1);
> /*     100100
>  * AND 100011
>  *   = 100000
>  */
> c = c + 1;
> // bits(x) = "100000"
> x = x & (x-1);
> /*     100000
>  * AND 011111
>  *   = 000000
>  */
> c = c + 1;
> // bits(x) = "0" bzw. x = 0
> // c = 3
> ```
> Da also mit jedem Schritt die letzte `1` aus der Bitansicht von `x` entfernt wird, und die Schleife bei `x = 0` abgebrochen wird, wird sie so oft wiederholt, wie `1`en in `x` sind. Da mit jeder Wiederholung `1` zu `int c` addiert wird, speichert dieser nach Beendigung der Schleife die Anzahl von `1`en in x. 
> Da diese auch von der Funktion zurückgegeben wird, gibt die Funktion die Anzahl von mit `1` gesetzten Bits in `x` zurück.