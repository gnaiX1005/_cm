# 🧮 計算數學實作全紀錄 (Computational Mathematics Assignments)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Math](https://img.shields.io/badge/Math-Calculus%20%26%20Algebra-red)
![Status](https://img.shields.io/badge/Status-Completed-success)
![AI-Assisted](https://img.shields.io/badge/AI--Assisted-Gemini-purple)

本專案收錄了「計算數學」課程的所有實作作業，內容涵蓋微積分、線性代數、幾何學、密碼學、資訊理論及微分方程。

---

## 📂 課程實作目錄索引

| 單元 | 題目說明 | 實作連結 |
| :--- | :--- | :--- |
| **習題 1** | 微積分基本定理驗證 (FTC) | [Code](homework/hw1/hw1.py) / [ReadMe](homework/hw1/README.md) |
| **習題 2** | 二次多項式求根 (Complex Roots) | [Code](homework/hw2/hw2.py) / [ReadMe](homework/hw2/README.md) |
| **習題 3** | 三次多項式求根 (Cardano Formula) | [Code](homework/hw3/hw3.py) / [ReadMe](homework/hw3/README.md) |
| **習題 4** | N 次多項式思考與數值解 | [Code](homework/hw4/hw4.py) / [ReadMe](homework/hw4/README.md) |
| **Week 2** | 有限體 (Finite Field GF(5)) 運算 | [Code](homework/week2/week2.py) / [ReadMe](homework/week2/README.md) |
| **Week 3** | 幾何學：點、線、圓的建構 | [Code](homework/week3/homework3.py) / [ReadMe](homework/week3/) |
| **Week 9** | 資訊理論：熵、散度與漢明碼 | [Code](homework/week9/homework9.py) / [ReadMe](homework/week9/) |
| **Week 10** | 線性代數：空間、矩陣與 SVD | [Code](homework/week10/homework10.py) / [ReadMe](homework/week10/README.md) |
| **Week 11** | 傅立葉變換 (DFT & IDFT) | [Code](homework/week11/HW10.py) / [ReadMe](homework/week11/) |
| **Week 13** | 常係數齊次常微分方程 (ODE) | [Code](homework/week13/week13.py) / [ReadMe](homework/week13/README.md) |

---

## 📝 重點習題詳解

### 1. 微積分基本定理 (FTC) 
透過數值方式驗證 $\frac{d}{dx} \int_{0}^{x} f(t) dt = f(x)$。
* **實作技術**：設定 $h=0.00001$，利用差分法模擬微分，黎曼和模擬積分。
* **驗證**：以 $f(x)=x^3$ 為例，確認「先積分再微分」後誤差小於 $0.01$。

### 2. 多項式求根演算法 (Polynomial Roots)
* **二次方程**：使用 `cmath` 處理 $b^2-4ac < 0$ 的複數根。
* **三次方程**：透過 $x=t-\frac{b}{3a}$ 轉換為降次形式（Depressed Cubic），套用 **Cardano 公式** 結合單位根 $\omega$ 旋轉求解。
* **N 次方程**：討論**伽羅瓦定理**之侷限（$n \ge 5$ 無公式解），利用 `numpy.roots` 透過伴隨矩陣特徵值求解。

### 3. 有限體 (Finite Field GF(5))
實作代數結構中的體公理：
* 驗證加法與乘法在 $\bmod 5$ 下是否滿足交換群。
* 透過 `GFElement` 類別封裝，支援 `+ - * /` 運算，並驗證分配律 $a(b+c) = ab + ac$。

### 4. 幾何學工具庫 (Geometry Toolkit)
建立二維幾何計算框架，包含：
* **交點計算**：直線與直線（克拉瑪公式）、直線與圓、兩圓交點。
* **幾何變換**：點的平移、縮放、旋轉（旋轉矩陣 $x' = x \cos \theta - y \sin \theta$）。
* **畢氏定理驗證**：檢查三點是否構成直角三角形。

### 5. 資訊理論 (Information Theory)
* **熵與散度**：計算 Entropy $H(P)$、Cross Entropy $H(P, Q)$ 與 KL Divergence。
* **漢明碼 (Hamming Code 7-4)**：實作產生矩陣 $G$ 與校驗矩陣 $H$，達到「偵測 1 bit 錯誤並自動修正」的功能。

### 6. 傅立葉變換 (DFT / IDFT)
從頭實作離散傅立葉變換矩陣運算，不調用現成套件：
* **DFT**: $X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-i 2 \pi k n / N}$
* **IDFT**: $x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] \cdot e^{+i 2 \pi k n / N}$
* **驗證**：計算 $IDFT(DFT(x))$ 的 $L_2$ 誤差，確保變換之可逆性。

### 7. 常係數齊次常微分方程 (ODE)
求解 $a_n y^{(n)} + \dots + a_1 y' + a_0 y = 0$。
* **邏輯**：計算特徵方程的根。
* **處裡**：針對**實根、重根、複數共軛根**自動生成對應的基底函數（如 $e^{\alpha x} \cos(\beta x)$），並組合成通解。

---

## 🧪 技術總結表

| 領域 | 關鍵演算法 / 定理 | Python 關鍵模組 |
| :--- | :--- | :--- |
| **代數** | Cardano Formula, Galois Theory | `cmath`, `numpy` |
| **分析** | FTC, Riemann Sum, DFT | `numpy`, `math` |
| **幾何** | Rotation Matrix, Cramer's Rule | `math` (Geometry logic) |
| **資安** | Hamming Code, RSA | `numpy`, `math` |

---

## 🚀 快速開始
1. 確保安裝必要套件：
   ```bash
   pip install numpy matplotlib
