# LCF Hysteresis Loop Area (Energy per Cycle)

This project calculates the **area enclosed by stress–strain hysteresis loops** for Low-Cycle Fatigue (LCF) data.  
For each cycle, the loop area approximates the **dissipated energy per cycle (energy density)**:

`W = ∮ σ dε`

## Input
- A folder containing **one CSV file per cycle**
- Each CSV contains stress–strain loop points:
  - **x-axis:** strain (dimensionless)
  - **y-axis:** stress (MPa)
- Default parser assumptions:
  - strain = **column B** (index 1)
  - stress = **column C** (index 2)
  - header rows skipped = **2** (adjustable)

## Method
Numerical integration using the **trapezoidal rule** over the ordered loop points.  
Reported value is the **absolute enclosed area** per cycle.

## How to run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
