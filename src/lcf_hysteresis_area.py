import os
import argparse
import pandas as pd


def trapezoidal_rule(x, y):
    """Compute integral using trapezoidal rule for ordered (x, y) data."""
    area = 0.0
    for i in range(1, len(x)):
        dx = x[i] - x[i - 1]
        area += dx * (y[i] + y[i - 1]) / 2.0
    return area


def calculate_area_from_csv(file_path, skiprows=2, strain_col=1, stress_col=2):
    """
    Read one cycle CSV and compute absolute hysteresis loop area ∮σ dε
    Assumes strain is in `strain_col` and stress is in `stress_col` (0-based index).
    """
    df = pd.read_csv(file_path, skiprows=skiprows)

    x = pd.to_numeric(df.iloc[:, strain_col], errors="coerce").dropna().to_list()
    y = pd.to_numeric(df.iloc[:, stress_col], errors="coerce").dropna().to_list()

    if len(x) < 2 or len(y) < 2:
        raise ValueError(f"Not enough numeric data in file: {file_path}")

    # If x and y got different lengths due to dropna, align by trimming
    n = min(len(x), len(y))
    x, y = x[:n], y[:n]

    return abs(trapezoidal_rule(x, y))


def calculate_areas_from_folder(folder_path, skiprows=2, strain_col=1, stress_col=2):
    """Compute hysteresis loop area for all CSV files in a folder."""
    results = []

    for filename in sorted(os.listdir(folder_path)):
        if filename.lower().endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            try:
                area = calculate_area_from_csv(
                    file_path, skiprows=skiprows, strain_col=strain_col, stress_col=stress_col
                )
                results.append({"file": filename, "area": area})
            except Exception as e:
                results.append({"file": filename, "area": None, "error": str(e)})

    return pd.DataFrame(results)


def main():
    parser = argparse.ArgumentParser(
        description="Compute hysteresis loop area (energy per cycle) from cycle-wise stress–strain CSV files."
    )
    parser.add_argument("--folder", required=True, help="Folder containing cycle CSV files")
    parser.add_argument("--skiprows", type=int, default=2, help="Header rows to skip in each CSV")
    parser.add_argument("--strain_col", type=int, default=1, help="0-based column index for strain")
    parser.add_argument("--stress_col", type=int, default=2, help="0-based column index for stress")
    parser.add_argument("--out", default="outputs/hysteresis_areas.csv", help="Output CSV path")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    df_out = calculate_areas_from_folder(
        args.folder, skiprows=args.skiprows, strain_col=args.strain_col, stress_col=args.stress_col
    )
    df_out.to_csv(args.out, index=False)

    print(df_out)
    print(f"\nSaved results -> {args.out}")


if __name__ == "__main__":
    main()
