To run:
1. Install java
2. Execute: `python3 run.py ../input/Complicated.java`, where parameter is path to analyzed java file.


Java file sample:

```
public class Complicated {
  public void example() { // This method has a cyclomatic complexity of 12
    int x = 0, y = 1, z = 2, t = 2;
    boolean a = false, b = true, c = false, d = true;
    if (a && b || b && d) {
      if (y == z) {
        x = 2;
      } else if (y == t && !d) {
        x = 2;
      } else {
        x = 2;
      }
    } else if (c && d) {
      while (z < y) {
        x = 2;
      }
    } else {
      for (int n = 0; n < t; n++) {
        x = 2;
      }
    }
  }
}
```

Output: `Total cyclomatic complexity:  12`
