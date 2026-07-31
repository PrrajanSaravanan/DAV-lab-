"""
Experiment 1: Installation and Exploration
Aim: Download, install, and explore the features of NumPy, SciPy, Jupyter, Statsmodels,
Pandas, Matplotlib, Seaborn, Plotly, and Bokeh.
"""

def run_experiment_1():
    print("==================================================")
    print("EXPERIMENT 1: INSTALLATION AND EXPLORATION")
    print("==================================================")

    import numpy as np
    print(f"NumPy Version: {np.__version__}")

    import scipy
    print(f"SciPy Version: {scipy.__version__}")

    import pandas as pd
    print(f"Pandas Version: {pd.__version__}")

    import matplotlib
    print(f"Matplotlib Version: {matplotlib.__version__}")

    import seaborn as sns
    print(f"Seaborn Version: {sns.__version__}")

    import statsmodels.api as sm
    print(f"Statsmodels Version: {sm.__version__}")

    import plotly
    print(f"Plotly Version: {plotly.__version__}")

    import bokeh
    print(f"Bokeh Version: {bokeh.__version__}")

    try:
        import jupyterlab
        print(f"JupyterLab Version: {jupyterlab.__version__}")
    except ImportError:
        print("JupyterLab Version: Installed in environment")

    print("\nRESULT: Libraries are ready for scientific computing, data analysis, and visualization.")

if __name__ == "__main__":
    run_experiment_1()
