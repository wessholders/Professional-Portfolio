# Bingo Card Generator

This [Bingo Card Generator script](https://github.com/wessholders/Professional-Portfolio/blob/main/Bingo%20Card%20Generator/Bingo_Maker_Github.py) generates customizable bingo cards in Excel format using prompts from an input Excel file. It creates multiple bingo cards, formats them with images and text, and saves them as an Excel workbook.

My wife and I had the pleasure of hosting a Couple's Shower for some of our best friends recently and we were looking for something fun, low-effort, and competitive for the guests to do during the shower. Bingo seemed like it fit the spot, but we did not want to bother with hand-writing that many bingo cards, so I wrote this script to do it for me.

## Features

- Reads prompts from an input Excel file.
- Generates a specified number of bingo cards.
- Formats the Excel sheets with custom styling.
- Inserts images at the top and bottom of each card.
- Automatically places a "Free Space" in the center.
- Ensures each card has unique prompts.

## Installation

### Prerequisites

Ensure you have Python installed along with the following dependencies:

```bash
pip install pandas xlsxwriter
```
## Usage

### 1. Prepare Input File

Create an Excel file (Input.xlsx) with a list of bingo prompts in the first column.
Save it in the designated input folder.

### 2. Modify Paths and Settings
Update the script with the correct file paths.

### 3. Run the Script

### 4. Check Output

The script generates an Excel file in the specified output folder.
Each sheet in the workbook represents a unique bingo card.

