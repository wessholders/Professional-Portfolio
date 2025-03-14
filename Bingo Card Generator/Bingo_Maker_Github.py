'''
- Description: This script will take an input excel containing bingo prompts, and generate a specified number of unique
  permutations of Bingo cards containing those prompts. You can use the images included in the repository as I have, or
  modify the code to use your own.
- Author: Wes Sholders
- Dependencies: You will need to install the following dependencies- pip install pandas xlsxwriter
'''
#####################
#####- MODULES -#####
#####################
import pandas as pd
import xlsxwriter
import random

#####################
#####- INPIUTS -#####
#####################
input_excel_path = r'C:\Path\To\Excel\Containing\Bingo\Prompts.xlsx'
output_excel_folder = r'C:\Path\To\Output|folder'
output_file_name = 'Bingo_Cards'
upper_image_path = r'C:\Path\To\Image\Used\In\Header.png'
lower_image_path = r'C:\Path\To\Image\Used\In\Footer.png'
output_excel_path = f'{output_excel_folder}\\{output_file_name}.xlsx'
title = "John and Jane's Couple Shower Bingo"

#########################
#####- SOURCE CODE -#####
#########################
num_cards = 30  # Change this to the desired number of bingo cards

# Read prompts from the specified Excel document excluding header row
prompts_df = pd.read_excel(input_excel_path, header=None)
prompts_list = prompts_df.iloc[:, 0].tolist()[1:]  # Exclude header row

# Create a new workbook
workbook = xlsxwriter.Workbook(output_excel_path)

for card_num in range(1, num_cards + 1):
    # Add a worksheet
    worksheet = workbook.add_worksheet(f'Card_{card_num}')
    worksheet.set_margins(left=0.7, right=0.7, top=0.25, bottom=0)
    # Set the width of columns and height of rows
    worksheet.set_column('A:E', 17.4)
    worksheet.set_row(0, 91)    # Row 1 for upper image
    worksheet.set_row(1, 69)    # Row 2 for text
    for i in range(2, 7):       # Rows 3 to 7 for bingo card
        worksheet.set_row(i, 103)
    worksheet.set_row(7, 73)    # Row 8 for lower image

    # Cell Formats
    merged_format = workbook.add_format({
    'align': 'center',
    'valign': 'vcenter',
    })
    title_format = workbook.add_format({
    'font_name': 'Aptos',
    'font_size': 28,
    'color': '#608258',
    'text_wrap': True,
    'align': 'center',
    'valign': 'vcenter',
    'bold': True,
    })
    format_centered = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'text_wrap': True})
    black_text_format = workbook.add_format({
    'font_name': 'Aptos',
    'font_size': 13.5,
    'color': '#000000',
    'text_wrap': True,
    'align': 'center',
    'valign': 'vcenter',
    })

    worksheet.merge_range('A1:E1', '', merged_format)
    worksheet.merge_range('A8:E8', '', merged_format)

    # Insert upper image in cell C1
    worksheet.insert_image('C1', upper_image_path, {"x_offset": -150, "y_offset": 0})

    # Merge cells for text
    worksheet.merge_range('A2:E2', title, title_format)

    # Insert lower image in cell C8
    worksheet.insert_image('C8', lower_image_path, {"x_offset": -105, "y_offset": 0})

    # Add a page break
    worksheet.set_v_pagebreaks([7])  # Vertical break after the 7th column
    worksheet.set_h_pagebreaks([8])  # Horizontal break after the 8th row

    prompts_list_copy = prompts_list.copy()  # Create a copy of the prompts list for this card
    for row in range(2, 7):
        for col in range(0, 5):  # Adjusted to A-E
            if row == 4 and col == 2:  # Center square
                worksheet.write(row, col, 'Free Space', title_format)
            else:
                prompt = random.choice(prompts_list_copy)
                worksheet.write(row, col, prompt, black_text_format)
                prompts_list_copy.remove(prompt)  # Remove used prompt

    # Set the worksheet to the page layout view
    worksheet.set_page_view()

workbook.close()
