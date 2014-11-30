# Call to rules:
	# input rules 
	# Parse rules under the assumption that they 
	# Hardcoded for now, will implement as taking in stuff later 
	#rule1 = limitTotalSum(">", 10, values, intermediateSumRow+1 )
	#ws.write(freeRow+5, 3, xlwt.Formula(rule1))

	
## Rule Creation Methods (to change after grammar)
## Return Strings right now
# =IF(SUM(B6:D6)>10,0,1)
# If the total sum is greater than 10, "GOOD" otherwise bad 
def limitTotalSum(operator, totalValue, values, intermediateSumRow):
	rowStart = 1
	rowStartStr = EXCEL_ROW_MAPPING[rowStart] + str(intermediateSumRow)
	rowEnd = rowStart + len(values) -1
	rowEndStr = EXCEL_ROW_MAPPING[rowEnd] + str(intermediateSumRow)


	innerFormulaStr = "SUM(" + rowStartStr + ":" + rowEndStr + ")"
	formulaStr = "IF(" + innerFormulaStr + operator + str(totalValue) \
		 + "," + "0" + "," + "1" + ")"
	return formulaStr
