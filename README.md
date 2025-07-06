# Algorithm Visualization Tool

A Python-based interactive tool for visualizing and understanding sorting and searching algorithms through ASCII animations.

## 🚀 Features

- **Interactive Menu System**: Easy-to-use command-line interface
- **Visual Animations**: ASCII bar charts with step-by-step algorithm execution
- **Multiple Input Methods**: Manual input, random generation, or predefined arrays
- **Comprehensive Algorithm Coverage**: 
  - Sorting: Bubble, Selection, Insertion, Merge, Quick, Heap Sort
  - Searching: Linear, Binary Search

## 📁 Project Structure

```
algori_vis/
├── main.py                # Entry point, handles user interaction and menu
├── algorithms/
│   ├── sorting.py         # Sorting algorithms (Bubble, Selection, Insertion, Merge, Quick, Heap)
│   ├── searching.py       # Searching algorithms (Linear, Binary)
├── utils/
│   ├── visualizer.py      # Visualization functions (ASCII bars, animations)
│   ├── helpers.py         # Utility functions (input validation, delays)
├── README.md              # Project documentation
```

## 🛠️ Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd algori_vis
   ```

2. **Ensure Python 3.6+ is installed**
   ```bash
   python --version
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 🎮 Usage

1. **Start the application**
   ```bash
   python main.py
   ```

2. **Choose algorithm type**
   - Sorting Algorithms
   - Searching Algorithms

3. **Select specific algorithm**
   - Follow the interactive menu prompts

4. **Input your data**
   - Manual entry: Type numbers separated by spaces
   - Random generation: Specify size and value range
   - Predefined arrays: Choose from preset examples

5. **Watch the visualization**
   - See real-time ASCII animations
   - Observe algorithm steps and comparisons

## 🔧 Algorithm Details

### Sorting Algorithms

| Algorithm | Time Complexity | Space Complexity | Description |
|-----------|-----------------|------------------|-------------|
| Bubble Sort | O(n²) | O(1) | Repeatedly steps through list, compares adjacent elements |
| Selection Sort | O(n²) | O(1) | Finds minimum element and places it at the beginning |
| Insertion Sort | O(n²) | O(1) | Builds final sorted array one item at a time |
| Merge Sort | O(n log n) | O(n) | Divide and conquer algorithm |
| Quick Sort | O(n log n) avg | O(log n) | Partitioning algorithm with pivot |
| Heap Sort | O(n log n) | O(1) | Uses binary heap data structure |

### Searching Algorithms

| Algorithm | Time Complexity | Space Complexity | Description |
|-----------|-----------------|------------------|-------------|
| Linear Search | O(n) | O(1) | Sequentially checks each element |
| Binary Search | O(log n) | O(1) | Divide and conquer on sorted array |

## 🎨 Visualization Features

- **ASCII Bar Charts**: Visual representation of array elements
- **Real-time Updates**: See changes as they happen
- **Element Highlighting**: Track current operations
- **Step-by-step Execution**: Understand each algorithm move
- **Comparison Animations**: See which elements are being compared

## 📝 Example Output

```
==================================================
    ALGORITHM VISUALIZATION TOOL
==================================================
1. Sorting Algorithms
2. Searching Algorithms
3. Exit

🔄 BUBBLE SORT
Initial array:
     Array Visualization
     ================
     ▓▓    ▓▓ ▓▓ 
     ▓▓    ▓▓ ▓▓ 
     ▓▓ ▓▓ ▓▓ ▓▓ 
     ▓▓ ▓▓ ▓▓ ▓▓ 
     -------
      5  2  4  6 
      0  1  2  3 
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📚 Educational Value

This tool is perfect for:
- **Students** learning algorithms and data structures
- **Teachers** demonstrating algorithm concepts
- **Developers** reviewing algorithm implementations
- **Anyone** interested in understanding how algorithms work

## 🔮 Future Enhancements

- [ ] More sorting algorithms (Radix, Counting, Bucket)
- [ ] Graph algorithms visualization
- [ ] Performance benchmarking
- [ ] Save/load array configurations
- [ ] Color-coded terminal output
- [ ] Web-based interface

## 📄 License

This project is open source and available under the MIT License.

## 🙋‍♂️ Support

If you encounter any issues or have suggestions for improvements, please feel free to:
- Create an issue on GitHub
- Submit a pull request
- Contact the development team

---

**Happy Learning! 🎉**

*Visualize → Understand → Master*
