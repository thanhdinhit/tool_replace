import re

# Replacement text
new_file_name = "ADC_TS_005"
# Your input text
input_text = """
/**
 * @file ADC_TS_006.c
 * Description: This is a sample file.
 */

/**
 * @test_id ADC_TS_006
 * Description: This is a sample test ID.
 */

// Code goes here
"""

# Replace text after * @file and before .c
pattern = r'(?<=\* @file\s)(.*?)(?=\.c)'
output_text = re.sub(pattern, new_file_name, input_text)
# Replace text after * @test_id
pattern = r'(?<=\* @test_id\s)(.*)'
output_text = re.sub(pattern, new_file_name, output_text)

print(output_text)