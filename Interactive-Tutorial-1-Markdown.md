# Interactive Tutorial 1: Markdown

## Working with Markdown

Press `Ctrl + Shift + M` to open a formatted preview on the right.

## Basic Text

Write two sentences about yourself, each in a different paragraph.

My name is Tommy.

I am on the Dissolved Gas subteam.

## Headers

Make a 3rd level header with your name:

### Thomas Bradford

## Emphasis

Write 4 of your favorite words using each type of emphasis:

*Pie*
**Catastrophe**
***Indentation***
~~epiphany~~

## Lists

Make an ordered list of 3 things you hope to achieve this semester, and elaborate on them with sub items. Then, make an unordered list of 3 classes that you're taking this semester:

1. Determine the fluidization velocity
    1. Determine the corresponding flow rate
3. Evaluate the effectiveness of the reactor.
    1. Acquire DO Meters
    2. Record the system's temperature
3. Consider scaling up a reactor that functions properly.

## Links

Write a sentence describing your major, and insert a link to your major's department website:

&nbsp;I'm going to be a [ChemE](https://www.cheme.cornell.edu/), designing and optimizing chemical processes.

## Images

Insert the Cornell seal image with:
  1. A relative file path(`/images/Cornell_University_seal.png`)
  2. A URL (https://raw.githubusercontent.com/AguaClara/aguaclara_tutorial/master/Images/Cornell_University_seal.svg.png)

![CornellSeal](/images/Cornell_University_seal.png)

Using a URL:
![CornellSeal](https://raw.githubusercontent.com/AguaClara/aguaclara_tutorial/master/Images/Cornell_University_seal.svg.png)

## Code Formatting

Put the name of this file in an in-line (single backtick) code format.

`Interactive-Tutorial-1-Markdown.md`

Put the following text in a Python-formatted code block:

```
def foo():
    print("Particles of a feather...")
    print("...floc together!")
```

```python
def foo():
    print("Particles of a feather...")
    print("...floc together!")
```

## Tables

Create a table listing your 3 favorite animals, books, and places on campus. Use a different alignment for each column.

<p style="text-align: center;">
 **Table of Favorites**
</p>

| Animals   | Books     | Places on campus |
| :--------- | ------------: | :---------: |
| Corgi| Harry Potter | Goldie's  |       
| Koi  | Lord of the Rings  | Cascadilla Gorge  |   
| Sloths   | The Picture of Dorian Gray  |Ivy Room   |   


## Blockquotes

Write your favorite quote. It must be attributed to Albert Einstein.

> "Hello. It's me."
> -- Albert Einstein

## Horizontal Rules

Add a horizontal rule:

---

## LaTeX Formatting

Copy the equation towards the end of the [Markdown tutorial](https://github.com/AguaClara/aguaclara_tutorial/wiki/Markdown#latex-formatting) and paste it here:

$$ a^2 + b^2 = c^2 $$
