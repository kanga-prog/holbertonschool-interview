- A `README.md` file at the root of the project folder is **mandatory**
- Your code must be **documented**
- Your code must follow **PEP 8 style** (version 1.7.x)
- All your files must be **executable**

---

## Tasks

### 0. Lockboxes

You have `n` number of locked boxes in front of you.  
Each box is numbered sequentially from **0 to n - 1** and each box may contain keys to the other boxes.

Write a method that determines if **all the boxes can be opened**.

#### Prototype:
```python
def canUnlockAll(boxes)

## Text Answer

We used a set-based approach:
- Start with box 0 unlocked and collect keys inside.
- Track opened boxes with a set.
- Open boxes corresponding to keys not yet opened.
- Add keys from newly opened boxes to the key set.
- Stop when no new boxes can be opened.
- Return True if all boxes are opened, else False.

