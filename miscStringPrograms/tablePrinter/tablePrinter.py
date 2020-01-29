kennel_feeding_data = [
    ['Deputy Dewey', 'Lucky', 'Lady', 'Scarlett'],
    ['Alli', 'James', 'LeAnn', 'Nick'],
    ['1/2 Cup or 3/4 Cup', '1 Cup', '3/4 Cup', '1 Cup']
]

def print_table(table_data):
    column_width = [0] * len(table_data)

    for row in range(len(table_data)):
        column = row
        for row_element in range(len(table_data[row])):
            length_of_element = len(table_data[row][row_element])

            if length_of_element > column_width[column]:
                column_width[column] = length_of_element

    for columns in range(len(table_data) + 1):
        for rows in range(len(table_data)):
            print(table_data[rows][columns].rjust(column_width[rows]),
                  end=" " * 8)
            # print(r_justified_text, end="")
        print('')




        # print(f'columnWidth{i}: {columnWidth[i]}')
        # for j in range(len(tableData)):
        #     print(j)
        #     lengthOfString = len(tableData[j][i])
        #     print(tableData[j][i])
        #     print(f'lengthOfString: {lengthOfString}')
        #     if lengthOfString > columnWidth[j]:
        #         columnWidth[j] = lengthOfString
        #     # # print(f'{j}: {lengthOfString}')
        #     # # print(tableData[j])
        #     print(f'columnWidth{i}: {columnWidth[i]}')


    # TODO for i in range(len(tableData) + 1):
    #         for k in range(len(tableData)):
    #             modifiedItem = tableData[k][i]
    #             print(modifiedItem)







    # for i in range(len(kennelFeedingData)):
    #     outerLoop = kennelFeedingData[i]
    #     # print(outerLoop)
    #     for i2 in range(len(outerLoop)):
    #         innerLoop = outerLoop[i2]
    #         # print(f'InnerLoop: {innerLoop}')
    #         print(kennelFeedingData[i], innerLoop)
print_table(kennel_feeding_data)