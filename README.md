# PSČ Konvertor
Jednoduchý PSČ konvertor na okresy a kraje. Zdrojový kód je psaný česky z veřejně nepublikovatelných důvodů :)

## Example (python3)
```python
In [1]: from PscKonvertor import PscKonvertor

In [2]: konvertor = PscKonvertor()

In [3]: konvertor.psc2okres(26601)
Out[3]: 'Beroun'

In [4]: konvertor.psc2kraj(26601)
Out[4]: 'Středočeský kraj'

In [6]: konvertor.okres2kraj('Beroun')
Out[6]: 'Středočeský kraj'
```
