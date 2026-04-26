# DAY-9
# 🐍 Python Code2Xplore – 60 Days Challenge
## Day 9: Shallow Copy vs Deep Copy – Warehouse Inventory System

**Student:** N.M.S.Jagadiswara Reddy
**Register Number:** AP24110011621
**Course:** Hands on Python (CSE205)
**Institution:** SRM University–AP, Department of Computer Science and Engineering
**Concerned Teacher:** Dr. Yasir Afaq
**Date of Submission:** 26-04-2026

---

## 📌 Problem Statement

We have a warehouse that stores items like **Laptop**, **Phone**, and **Tablet**. Each item has details like price, stock, and supplier rating stored inside a nested dictionary. The task is to understand what happens when we copy this data and make changes to the copy — specifically, whether changing the copy also changes the original data or not, and why.

---

## 🧠 Logic & Approach

1. **Data Creation** — Inventory built as a list of dictionaries with nested `details` and `supplier` fields
2. **Shallow Copy** — `main_data.copy()` copies only the outer list; inner dictionaries are still shared
3. **Deep Copy** — `copy.deepcopy()` creates a fully independent copy of everything including nested data
4. **Personalized Modification** — Roll number used to select which item to modify:
   - `24110011621 % 3 = 0` → index **0** → **Laptop** is modified
   - Price reduced by 10%: `50000 → 45000`
   - Stock increased by 5: `10 → 15`
5. **Comparison** — `check_diff()` compares original vs modified copies to count changed and unchanged items
6. **Summary** — Prints how many items changed and how many stayed the same for each copy type

---

## 🔢 Personalization

| Parameter | Value |
|-----------|-------|
| Roll Number | 24110011621 |
| Inventory Length | 3 |
| index = roll % length | 24110011621 % 3 = **0** |
| Item Modified | Laptop (index 0) |
| Price Change | 50000 → 45000 (10% reduction) |
| Stock Change | 10 → 15 (+5) |

---

## ✅ Test Cases

| Test Case | Expected Output | Actual Output |
|-----------|-----------------|---------------|
| Shallow copy modifies original? | Yes — original Laptop price becomes 45000 | Yes — original Laptop price changed to 45000, stock changed to 15 |
| Deep copy modifies original? | No — original stays unchanged | No — original Laptop price still 50000, stock still 10 |

---

---

## 📦 Dependencies

No external libraries required. Uses Python built-ins only.

```bash
python day_9.py
```

---

## 🧾 Learning Outcomes

- Understood the difference between **shallow copy** and **deep copy** for nested data structures
- Observed how `list.copy()` shares inner dictionary references — modifying the copy silently mutates the original
- Confirmed that `copy.deepcopy()` creates a fully independent clone — changes never affect the original
- Used **modulo arithmetic** on roll number to personalize which inventory item gets modified
- Built a reusable `check_diff()` function to compare two lists of dictionaries and classify changed vs unchanged items

---

## 📜 Declaration

I hereby declare that this submission is my own original work. I have not used AI tools, copied code from the internet, or shared code with others. I understand that plagiarism will result in ZERO marks.

**Signed:** N.M.S.Jagadiswara Reddy
**Date:** 26-04-2026
