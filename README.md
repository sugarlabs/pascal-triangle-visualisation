The Game
===
The **Pascal Triangle Visualization Activity** provides an interactive and customizable way to explore the properties of Pascal’s Triangle. This activity allows users to visualize the triangle with various settings and experiment with its structure by modifying parameters like **modulo**, **number of rows**, and the **player** setting.

**Features and Gameplay:**
- **Modulo Function:**  
  Players can select a modulo value that defines the digits displayed in each cell of the triangle. For example, selecting modulo 3 will generate a triangle filled with the digits 0, 1, and 2.
  
- **Rows:**  
  The number of rows in the triangle can be customized, allowing players to view smaller or larger triangles depending on their preference.

- **Cell Calculation:**  
  Each cell of the triangle is calculated based on its two neighboring cells from the row above, using the formula:  
  `p = (q1 + q2) mod N`  
  Where **p** is the value of the current cell, **q1** and **q2** are the values from the row above, and **N** is the selected modulo.

- **Number or Color Display:**  
  Players can switch between viewing the triangle as a collection of numbers or a colorful representation. This adds an extra dimension to the visual exploration of Pascal’s Triangle, making it both an educational and visually engaging activity.

With these options, users can experiment with the mathematical properties of Pascal’s Triangle, customize their experience, and discover patterns and insights in an interactive way.


![Image](https://github.com/user-attachments/assets/0a33839b-52d3-47d9-a252-5fb5216ec65a)


How to run
===========

Pascal Triangle Visualisation can be run on the Sugar desktop.

* [How to Get Sugar on sugarlabs.org](https://sugarlabs.org/)

run with `sugar-activity3`
also compatible with `sugar-activity`
