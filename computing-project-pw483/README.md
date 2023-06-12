[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10571848&assignment_repo_type=AssignmentRepo)

# Computer Project

## Wavefunction Collapse algorithm

This project focuses on 2D image inputs.

This template should explain my work in chronological order.
The first Jupyter notebooks were created called WFC-Red-Maze.ipynb and WFC-Red-Maze2.ipynb
, where the first attempts to use the wavefunction collapse algorithm from an array of a simple 2D image. There is only a minor difference between the two notebook, which is how the collapsing processes in 'observe()' and 'observe2()' are defined. However, the results from both notebooks are noticeably different, and I believe it is only a mattter of preference to decide which definition is better.

Then, WFC knot.ipynb was created to test the code with imported actual image called 'knot', which is attached in the assests folder. A problem occurred for the second imported example(Flowers.png) because imported images can be in RGB, RGBA etc. After some modifications, the code works well with the imported image as the result agrees with the result from (https://github.com/mxgmn/WaveFunctionCollapse)

Next, a flower image(in the assets folder) was implemented in the WFC flowers.ipynb but returned unexpected outputs. However, the unnatural effects have been mitigated after several modifications.

### Folders explanation

1. Classes_and_Functions folder contains 3 .py files that contain all the Classes and Methods shared between the notebooks
2. animations folder contains mp4 files for the output animations
3. assets folder contains the imported input images used for analysis in the notebooks

### The report

The report was presented in both .ipynb and .pdf. The pdf file should contain everything I have done in a digestible manner while omitting most of the technical programming details.
The .ipynb files are the records of my code. Comments and Docstrings should explain what each section is doing, but for better big picture understanding and analysis please consult the pdf file.

### Disclaimer

Most of the commit commments do not make a whole lot of sense. They are more for myself.
