# 📊 Matplotlib & Streamlit - Comprehensive Guide

This repository contains a comprehensive collection of Jupyter notebooks and Streamlit applications covering Matplotlib data visualization and Streamlit web app development. Perfect for beginners and intermediate learners who want to master data visualization and interactive web applications in Python.

## 📚 Notebooks Overview

### 1. Matplotlib Fundamentals (`Ch-10 Matplotlib.ipynb`)
**Focus: Complete Matplotlib Visualization Library**

#### Basic Plotting 📈
- **Line Charts**: Simple to multi-line plots with customization
- **Markers and Line Styles**: `o`, `v`, `-`, `--`, `-.`, `:`
- **Colors and Styling**: RGB, HEX, named colors, color maps
- **Labels and Titles**: `xlabel()`, `ylabel()`, `title()`, `suptitle()`
- **Grid Customization**: `grid()`, colors, styles

#### Advanced Charts 📊
- **Scatter Plots**: Color mapping, size variation, transparency
- **Bar Charts**: Vertical and horizontal bars, grouped bars
- **Histograms**: Bins customization, frequency distribution
- **Pie Charts**: Explode, autopct, shadow, startangle
- **Area Plots**: Fill between, stacked area charts
- **Stacked Plots**: Multiple layer visualization

#### Subplots and Layout 🎯
- **Multiple Subplots**: `subplot(rows, cols, index)`
- **Figure Customization**: `figure(figsize=[width, height])`
- **Axis Control**: `axis('off')`, limits, scales
- **Legends**: Location, labels, customization

#### Practical Examples 💡
- Random data generation with NumPy
- Custom color maps (tab20b, tab20c, etc.)
- Interactive color bars
- Real-world data visualization

---
# Streamlit UI - Comprehensive Guide

This notebook (`Streamlit UI.ipynb`) contains a complete collection of Streamlit examples demonstrating UI creation, layout fundamentals, input widgets, file handling, data display, and chart integration. Perfect for beginners learning to build interactive web applications with Streamlit.

## 📁 Files Generated in This Notebook

| File | Description |
|------|-------------|
| `hello.py` | Basic text and code display |
| `hello2.py` | Faculty profile with sidebar and columns |
| `hello3.py` | Text input and text area demo |
| `hello4.py` | Number input and slider |
| `hello5.py` | Selection widgets (selectbox, multiselect, radio, checkbox) |
| `notice.py` | Interactive notice board with filters |
| `date_time_file.py` | Date, time pickers and file upload |
| `download_button.py` | Generate and download CSV data |
| `display_data.py` | DataFrame, Table, and JSON display |
| `media_display.py` | Image, audio, and video embedding |
| `status_element&progress.py` | Progress bars and status messages |
| `chart.py` | Matplotlib integration with Streamlit |
| `streamlit_graph.py` | Inbuilt Streamlit charts |
| `Task_Student_data.py` | Complete student marks & feedback form |
---

### 2. Practice Exercises (`Practice_MatplotLib.ipynb`)
**Focus: Hands-on Matplotlib Practice**

#### Course Enrollment Visualization 🎓
```python

data = {"C":20, "C++":11, "JAVA":15, "Python":30, "Maths":45}
# Bar chart with green bars and grid
# Pie chart with explode effect

