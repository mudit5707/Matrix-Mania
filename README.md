# Matrix-Mania

A curated collection of Python programs implementing various matrix algorithms and patterns.  
This repository is designed to serve as a quick reference, a teaching aid, and a personal portfolio of clean, modular code for commonly used matrix-related tasks.

---

## 🎯 Programs Included

Here’s a breakdown of each script (file) and what it does:

| File | Description |
|------|-------------|
| **`InputMatrix.py`** | Basic utility to read an \(m \times n\) matrix from user input and display it, used as a foundation for further operations. |
| **`DiagnolCheck.py`** | A program (note: spelling of “Diagonal” may be updated) that checks if a given square matrix is diagonal (i.e., all non-diagonal entries are zero and possibly non-zero entries only on the main diagonal). |
| **`MatrixMultiplication.py`** | Multiplies two compatible matrices (e.g., \(A_{m\times p}\) × \(B_{p\times n}\) → \(C_{m\times n}\)) with a step-by-step logic. |
| **`Transpose.py`** | Computes the transpose of a given matrix (switching rows and columns). |
| **`RowColumnSwap.py`** | Swaps the rows and columns of a matrix in some specified way (e.g., interchange two rows, two columns, or fully swap the row vs column indices). |
| **`Sparse Conversion of a Matrix.py`** | Converts a (dense) matrix into a sparse representation (e.g., storing only non-zero entries) and perhaps back, showing memory-efficient handling of large mostly-zero matrices. |
| **`MatrixExponentiation.py`** | Raises a square matrix to a given power (e.g., \(A^k\)), likely using repeated multiplication or a faster method like exponentiation by squaring. |
| **`Number Spiral.py`** | Generates a pattern in matrix form, such as a spiral of numbers (typically filling a matrix in a spiral order) — a visual/pattern exercise rather than purely algebraic. |

---

## 📂 Folder / File Structure

Matrix-Mania/
│
├── InputMatrix.py
├── DiagnolCheck.py
├── MatrixMultiplication.py
├── Transpose.py
├── RowColumnSwap.py
├── Sparse Conversion of a Matrix.py
├── MatrixExponentiation.py
├── Number Spiral.py
└── README.md ← (this file)

yaml
Copy code

---

## 🧠 Concepts Covered

- Linear algebraic basics: transpose, multiplication, exponentiation  
- Data structures & representations: converting dense ↔ sparse matrices  
- Pattern generation & matrix manipulation: row/column swaps, spiral fills  
- Algorithmic thinking: loops, nested structures, indexing, complexity awareness  
- Modular, simple Python implementations — easy to read, adapt and expand

🤝 Contributing
If you’d like to contribute:
Fork the repository
Add new scripts or improve existing ones
Submit a pull request with a clear description
Write code that is clean, well-commented, and follows consistent naming/formatting

⭐ Support

If you find this repository helpful, please star ⭐ it on GitHub!
Your support motivates further improvements and new additions.
