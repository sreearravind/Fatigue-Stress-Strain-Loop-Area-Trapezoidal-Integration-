# LCF Hysteresis Loop Area (Energy per Cycle)

This project calculates the **area enclosed by stress–strain hysteresis loops** for Low-Cycle Fatigue (LCF) data.  
For each cycle, the loop area approximates the **dissipated energy per cycle**:

W = ∮ σ dε

## Input
- A folder containing **one CSV file per cycle**
- CSV contains strain and stress columns (strain on x-axis, stress on y-axis)
- Current parser assumes:
  - strain = column B
  - stress = column C
  - header rows are skipped

## Method
Numerical integration using the **trapezoidal rule** over the ordered loop points.  
Reported value is the **absolute enclosed area**.

## How to run
1. Install dependencies:
   `pip install -r requirements.txt`

2. Edit `folder_path` inside the script (or update to CLI arguments)

3. Run:
   `python src/lcf_hysteresis_area.py`

## Output
Prints loop area for each file (cycle) in the folder.

## Notes
- Units: Stress (MPa) × Strain (dimensionless) → MPa ≈ MJ/m³ (energy density).
- Use synthetic/anonymized data in `examples/` if experimental data is confidential.
