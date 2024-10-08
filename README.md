#### **Project Overview**

This project analyzes the voting patterns in U.S. counties based on the majority race and other demographic factors. The analysis uses statistical methods to determine the likelihood of a county voting Republican or Democrat. The project is structured into several Python scripts, each handling different parts of the data processing and analysis pipeline.

---

#### **Directory Structure**

-   **`data/`**: Contains the datasets used in the analysis, including the combined dataset of election results and census data.
-   **`output/`**: Contains the output files generated by the scripts, including statistical results and visualizations.
-   **`presentation_and_pdf/`**: Contains the introductory documentation, high-level explanations of the data, and the final presentation in both PDF and PowerPoint formats.

---

#### **Required Libraries**

Before running the project, you need to install the following Python libraries:

-   **pandas**: For data manipulation and analysis
-   **numpy**: For numerical operations
-   **scipy**: For statistical tests
-   **statsmodels**: For advanced statistical models
-   **matplotlib**: For creating visualizations
-   **seaborn**: For enhanced data visualization

You can install all required libraries using pip:

```bash
pip install pandas numpy scipy statsmodels matplotlib seaborn
```

---

#### **How to Run the Project**

1. **Download the Repository**:
   Ensure you have the full project directory structure as outlined above.

2. **Navigate to the Project Directory**:
   Open a terminal or command prompt and navigate to the project directory.

3. **Run the Main Script**:
   The main script (`main.py`) will sequentially execute all necessary scripts to prepare the data, perform the statistical analysis, and generate the outputs.

    ```bash
    python main.py
    ```

    This will execute the following steps:

    - **Data Preparation**: Cleans and merges the election and census data.
    - **Statistical Analysis**: Performs the Z-test, Chi-square test, and T-test, saving results in the `output/` directory.
    - **Output Generation**: Creates visualizations and saves them in the `output/` directory.

---

#### **Output Files**

All outputs generated by the scripts are stored in the `output/` directory, including:

-   **Proportion Test Output**: `proportion_test_output.txt`
-   **Chi-Square Test Output**: `chi_square_test_output.txt`
-   **T-Test Output**: `t_test_output.txt`
-   **Visualizations**:
    -   `count_by_race.png`
    -   `proportion_by_race.png`
    -   `pie_chart_white_majority.png`

---

#### **Presentation and Documentation**

The `presentation_and_pdf/` directory contains:

-   **Introduction and High-Level Explanation**: A document explaining the project’s objectives, the data used, and the methodology.
-   **Final Presentation**: The project’s final presentation in both PowerPoint and PDF formats.

---

#### **Conclusion**

This project provides a comprehensive analysis of how race influences voting patterns in the United States. By following the steps outlined above, you can replicate the analysis and explore the results through the provided outputs and presentation materials.

---

If you have any questions or need further assistance, feel free to contact the project maintainer.
