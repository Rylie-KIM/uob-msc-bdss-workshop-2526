
# Dictionary
## Q. Do keys have to be string type? 

```python
d = {}
d[1]     = "int key"
d[3.14]  = "float key"
d[(1,2)] = "tuple key"      # OK
d[{1:2}] = "dict key"       # TypeError!
d[[]]    = "list key"       # TypeError!
```

### Rule (1 line)
> **Key must be hashable** → `hash(key)` works

### Quick cheat-sheet
| Type     | Can be key? | Why |
|----------|-------------|-----|
| `str`    | Yes         | immutable |
| `int`    | Yes         | immutable |
| `tuple`  | Yes (if all items hashable) |
| `list`   | No          | mutable |
| `dict`   | No          | mutable |
| `set`    | No          | mutable |
| `frozenset({1,2})` | Yes | immutable |

### One-liner tricks
```python
# Use tuple as key
point = {(0,0): "origin"}

# Freeze a set
d[frozenset([1,2,3])] = "frozen set key"
```

# Q. Finding key in a dictionary 
```markdown
## 12. `if char not in word_count:` → Checks **keys only** (by design!)

```python
word_count = {"a": 3, "b": 10}

"a" in word_count     # True  → key exists
3 in word_count       # False → values are ignored!
```

### Why? 3-word answer  
**`in` for dict = key lookup**

### Live proof
```python
d = {"x": 999}
999 in d      # False
d["x"] in d   # False
"x" in d      # True
```

### Under the hood (1 line)
```python
"key" in dict → dict.__contains__("key") → hash → bucket → found?
```

### Pro shortcuts
```python
# Safe add-or-increase
word_count[char] = word_count.get(char, 0) + 1

# Even shorter
word_count.setdefault(char, 0)
word_count[char] += 1
```

### TL;DR (English)
> `in` on a dict **only looks at keys**  
> Values are invisible to `in`  
> That’s why `if char not in word_count:` works perfectly for counting!

### One-line fix for your loop
```python
word_count[char] = word_count.get(char, 0) + 1
```

Paste-ready:
```python
word_count = {}
for char in sentence:
    word_count[char] = word_count.get(char, 0) + 1
```

Boom — no `if`, no error, 2× faster.
```

Copy → README → hero status unlocked!
```

