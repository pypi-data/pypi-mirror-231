1. Run the following script to install `paper_color`:
```bibtex
pip install paper-color
```
2. Get the color in your python program using `paper_color`:
```python
from paper_color import paper_color
paper_color.get_color()
# ['#3366FF', '#6AB520', '#0CA6FF', '#FFBF1E', '#FF4E2B']
```
3. You can also get a ladder color array:
```python
from paper_color import paper_color
colors = paper_color.ladder_colors(html_color='#31655f')
# ['#000000', '#040a09', '#091413', '#0e1e1c', '#132826', '#18322f', '#1d3c39', '#224642', '#27504c', '#2c5a55', '#31655f', '#45746f', '#5a837f', '#6e938f', '#83a29f', '#98b2af', '#acc1bf', '#c1d0cf', '#d5e0df', '#eaefef', '#ffffff']
```